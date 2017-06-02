import os
import numpy as np
import cv2
from matplotlib import pyplot as plt


def extract_string_segments(filename, sample_folder):
    original = cv2.imread(filename)
    img = cv2.imread(filename)
    name_prefix = os.path.splitext(filename)[0]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, 1, 1, 11, 2)
    thresh = cv2.dilate(thresh, None, iterations=3)
    thresh = cv2.erode(thresh, None, iterations=2)
    img, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    filenames = []
    for i in range(0, len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])
        if w*h > 100:
            roi = get_roi(original, x,y,w,h)
            string_filename = os.path.join(sample_folder, name_prefix + str(i) + "_stringseg_" + ".png")
            cv2.imwrite(string_filename, roi)
            filenames.append(string_filename)
    return filenames

def extract_word_segments(filename, sample_folder):
    original = cv2.imread(filename)
    img = cv2.imread(filename)
    name_prefix = get_name(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, 1, 1, 11, 2)

    img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    filenames = []
    for i in range(0, len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])
        if w*h > 100:
            roi = get_roi(original, x,y,w,h)
            string_filename = os.path.join(sample_folder, name_prefix + "_" + str(i) + "_wordseg_" + ".png")
            cv2.imwrite(string_filename, roi)
            filenames.append(string_filename)
    return filenames

def extract_character_segments(filename, sample_folder):
    original = cv2.imread(filename)
    img = cv2.imread(filename)
    columns = get_pixel_columns(img)
    column_brightness = []
    for c in columns:
        average_brightness = get_average_brightness(c)
        column_brightness.append(average_brightness)
    height, widht, channels = img.shape

    partlength = int(0.3*height)
    candidates = find_local_mins(column_brightness, partlength)#, partition)

    brightness_mean = find_image_brightness(original)
    borders = filter_candidates(candidates, column_brightness, brightness_mean)
  #  draw_vertical_borders(candidates, height, img)
    return [0]

def find_image_brightness(image):
    height, width, channels = image.shape
    sum = 0
    size = height*width
    for i in range(0, height):
        for j in range(0, width):
            sum += np.mean(image[i][j])
    return sum/size

def filter_candidates(candidates, brightness, border):
    filtered = []
    for c in candidates:
        if check_neighbours(c, brightness, border):
            filtered.append(c)
    return filtered

def check_neighbours(candidate, brighness, border):
    is_bright_enough = candidate[1] < border
    right_neighbour = candidate[0] + 2 < len(brighness) and brighness[candidate[0]+2] > border
    left_neighbour = candidate[0] - 2 >= 0 and brighness[candidate[0]+2] > border
    return is_bright_enough and (right_neighbour or left_neighbour)


def find_local_mins(brighness, partlength):
    i = 0
    n = len(brighness)
    local_mins = []
    while(i <= n):
        if i+partlength < len(brighness):
            d = brighness[i:i+partlength]
            k = d.index(min(d))
            local_mins.append((i+k,brighness[i+k]))
            i = i+k+1
        else: break
    return local_mins

def get_pixel_columns(img):
    height, widht, channels = img.shape
    columns = []
    partitions = range(0, widht)
    for i in range(0, widht):
        columns.append(get_roi(img, partitions[i], 0, 1, height))
    return columns

def get_average_brightness(column):
    brightness = []
    for pixel in column:
        brightness.append(get_pixel_brighness(pixel))
    return np.mean(brightness)

def get_pixel_brighness(pixel):
    return np.mean(pixel)

def get_roi(img,x,y,w,h):
    roi = img[y:y + h, x:x + w]
    return roi

def get_name(path):
    base = os.path.basename(path)
    return os.path.splitext(base)[0].replace("_stringseg_","")


def draw_vertical_borders(borders, height, img):
    for b in borders:
        cv2.line(img, ( b[0], 0), (b[0], height-1), (0,255,0))
    show_image_pyplot(img)

def show_image_pyplot(img):
    plt.imshow(img, cmap='gray')
    plt.show()
'''
def open_image(filename):
    img = cv2.imread(filename, cv2.CV_8UC1)
    img = cv2.GaussianBlur(img, (3, 3), 0);
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    return img

def extract_all_countours(img):
    cv2.bitwise_not(img, img)
    img, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)
    return img, contours, hierarchy

def draw_bounding_boxes(img, contours, hierarchy):
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        thickness = 2
        if w*h < 40:
            thickness = 3
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), thickness)
    return cv2.bitwise_not(img,img)

def get_roi(img,x,y,w,h):
    roi = img[y:y + h, x:x + w]
    return roi

def write_sample_image(image, contour, prefix, name, sample_size, sample_folder):
    x, y, w, h = cv2.boundingRect(contour)
    roi = get_roi(image, x, y, w, h)
    temp_name = os.path.join(sample_folder, name + "_temp_.png")
    cv2.imwrite(temp_name, roi)
    img = cv2.imread(temp_name, 0)
    height, width = img.shape
    temp_img = cv2.imread(temp_name, 1)
    pts1 = np.float32([[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]])
    pts2 = np.float32([[0, 0], [sample_size[0], 0], [0, sample_size[1]], [sample_size[0], sample_size[1]]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(temp_img, M, (sample_size[0], sample_size[1]))
    filename = os.path.join(sample_folder,prefix + "_" + name + "_sample.png")
    cv2.imwrite(filename, dst)
    os.remove(temp_name)
'''