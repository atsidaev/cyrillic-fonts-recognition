#!/usr/bin/python3

from Preprocessing.Contours import PixelAnalyser as pixel

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

def turtle_check(candidate, pixel_column):
    avg = pixel.get_average_brightness(pixel_column)
    for p in pixel_column:
        brightness = pixel.get_pixel_brighness(p)
        if brightness > avg:
            return False
    return True


def brightness_connectivity_check(candidate_index, columns):
    left_index = candidate_index - 1
    roi = columns[left_index:left_index+3]
    return column_connectivity_check(roi[1],  roi[0]) and column_connectivity_check(roi[1], roi[2])

def column_connectivity_check(candidate, neighbour):
    high1, middle1, low1 = pixel.get_max_brightness_lvl(candidate)
    high2, middle2, low2 = pixel.get_max_brightness_lvl(neighbour)
    first_crit = high1==high2 or middle1 == middle2 or low1 == low2

    candidate_brightness = pixel.get_average_brightness(candidate)
    neighbour_max_brightness = pixel.get_max_brightness(neighbour)
    second_crit = candidate_brightness < neighbour_max_brightness

    max_candidate_brightness = pixel.get_max_brightness(candidate)
    third_crit = max_candidate_brightness > (2*abs(max_candidate_brightness - neighbour_max_brightness))

    return first_crit and second_crit and third_crit

def distance_connectivity_check(candidate_index, candidates, columns, filtered):
    n = len(columns[0])
    dmin = int(0.4*n)
    dk = abs(candidate_index - filtered[-1][0])
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
