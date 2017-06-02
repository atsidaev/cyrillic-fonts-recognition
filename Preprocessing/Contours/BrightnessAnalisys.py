#!/usr/bin/python3
import numpy as np
from Preprocessing.Contours import ContourHelper as helper

def borders_brightness_filter(candidates, brightness, border):
    filtered = []
    for c in candidates:
        if check_neighbours(c, brightness, border):
            filtered.append(c)
    return filtered

def check_neighbours(candidate, brighness, border):
    is_bright_enough = candidate[1] < border
    right_neighbour = candidate[0] + 2 < len(brighness)
    if right_neighbour:
        if brighness[candidate[0] + 2] > border:
            right_neighbour == True
    left_neighbour = candidate[0] - 2 >= 0
    if left_neighbour:
        if brighness[candidate[0] - 2] > border:
            left_neighbour == True
    return is_bright_enough and (right_neighbour or left_neighbour)

def borders_connectivity_filter(candidates, columns):
    filtered = []
    for i in range(1, len(candidates)-1):
        if first_border_connectivity_check(candidates[i][0], columns):
            continue
        elif second_border_connectivity_check(i, candidates, columns):
            continue
        else:
            filtered.append(candidates[i])
    return filtered

def first_border_connectivity_check(candidate_index, columns):
    left_index = candidate_index - 1
    roi = columns[left_index:left_index+3]
    return column_connectivity_check( roi[1], roi[0]) and column_connectivity_check(roi[1], roi[2])

def column_connectivity_check(candidate, neighbour):
    high1, middle1, low1 = get_max_brightness_lvl(candidate)
    high2, middle2, low2 = get_max_brightness_lvl(neighbour)
    first_crit = high1==high2 or middle1 == middle2 or low1 == low2

    candidate_brightness = get_average_brightness(candidate)
    neighbour_max_brightness = get_max_brightness(neighbour)
    second_crit = candidate_brightness < neighbour_max_brightness

    max_candidate_brightness = get_max_brightness(candidate)
    third_crit = max_candidate_brightness > (2*abs(max_candidate_brightness - neighbour_max_brightness))

    return first_crit and second_crit and third_crit

def second_border_connectivity_check(candidate_index, candidates, columns):
    if candidates[candidate_index][0] == 0:
        return False
    n = len(columns[0])
    dmin = int(0.4*n)
    dk = abs(candidate_index - candidates[candidate_index-1][0])
    return dk < dmin


def get_local_mins(brighness, partlength):
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
        columns.append(helper.get_roi(img, partitions[i], 0, 1, height))
    return columns

#brightness

def get_image_brightness(image):
    height, width, channels = image.shape
    sum = 0
    size = height*width
    for i in range(0, height):
        for j in range(0, width):
            sum += get_pixel_brighness(image[i][j])#np.mean(image[i][j])
    return sum/size

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



