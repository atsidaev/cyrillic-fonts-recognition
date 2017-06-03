#!/usr/bin/python3
import numpy as np
from Preprocessing.Contours import ContourManipulator as cntmnp


def get_image_average_brightness(image):
    height, width, channels = image.shape
    sum = 0
    size = height*width
    for i in range(0, height):
        for j in range(0, width):
            sum += get_pixel_brighness(image[i][j])
    return 0.6*(sum/size)

def get_max_brightness_lvl(column):
    high_mark = 0 + int(0.3*len(column))
    middle_mark = high_mark + int(0.4*len(column))
    low_mark = len(column)

    high = get_max_brightness(column[0:0 + high_mark])
    middle=get_max_brightness(column[high_mark:high_mark + int(middle_mark - high_mark)])
    low = get_max_brightness(column[middle_mark:middle_mark + int(low_mark - middle_mark)])

    return high, middle, low

def get_max_brightness(column):
    brightness = []
    for p in column:
        brightness.append(get_pixel_brighness(p))
    return max(brightness)

def get_average_brightness(column):
    brightness = []
    for pixel in column:
        brightness.append(get_pixel_brighness(pixel))
    return np.mean(brightness)

def get_pixel_brighness(pixel):
    return abs(255 - np.mean(pixel))

def get_pixel_columns(img):
    height, widht, channels = img.shape
    columns = []
    partitions = range(0, widht)
    for i in range(0, widht):
        columns.append(cntmnp.get_roi(img, partitions[i], 0, 1, height))
    return columns

def get_median_brightness(column):
    brightness = []
    for pixel in column:
        brightness.append(get_pixel_brighness(pixel))
    return np.median(brightness)

def get_brightness_distribution(columns):
    column_brightness = []
    for c in columns:
        average_brightness = get_average_brightness(c)
        column_brightness.append(average_brightness)
    return column_brightness