import os
import cv2
from Preprocessing.Contours import BorderAnalyser as ba
from Preprocessing.Contours import PixelAnalyser as pixel
from Preprocessing.Contours import Filters as filters
from Preprocessing.Contours import ContourManipulator as cntmanip

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
            roi = cntmanip.get_roi(original, x, y, w, h)
            string_filename = os.path.join(sample_folder, name_prefix + str(i) + "_stringseg_" + ".png")
            cv2.imwrite(string_filename, roi)
            filenames.append(string_filename)
    return filenames

def extract_word_segments(filename, sample_folder):
    original = cv2.imread(filename)
    img = cv2.imread(filename)

    name_prefix = cntmanip.get_name(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, 1, 1, 11, 2)

    img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    filenames = []
    for i in range(0, len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])
        if w*h > 100:
            roi = cntmanip.get_roi(original, x, y, w, h)
            string_filename = os.path.join(sample_folder, name_prefix + "_" + str(i) + "_wordseg_" + ".png")
            cv2.imwrite(string_filename, roi)
            filenames.append(string_filename)
    return filenames

def extract_character_segments(filename, sample_folder):
    original = cv2.imread(filename)
    img = cv2.imread(filename)
    columns = pixel.get_pixel_columns(img)
    column_brightness = pixel.get_brightness_distribution(columns)
    height, widht, channels = img.shape
    final_borders = filters.get_character_borders(img,column_brightness,columns)
    cntmanip.draw_vertical_borders(final_borders, height, img)
    return [0]

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