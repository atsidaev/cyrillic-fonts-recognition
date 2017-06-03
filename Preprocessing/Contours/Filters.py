#!/usr/bin/python3

from Preprocessing.Contours import BorderAnalyser as ba
from Preprocessing.Contours import PixelAnalyser as px
import cv2

def get_character_borders(img, brightness_distribution, img_columns):
    height, widht, channels = img.shape
    partlength = int(0.3*height)
    brightness_mean = px.get_image_average_brightness(img)
    candidates = ba.get_local_mins(brightness_distribution, partlength)
    borders = borders_brightness_filter(candidates, brightness_distribution, brightness_mean)
    final_borders = borders_connectivity_filter(borders, img_columns)
    final_borders = [(0, brightness_distribution[0])] + final_borders + [(len(brightness_distribution) - 1, brightness_distribution[-1])]
    final_borders = borders_distance_filter(final_borders, img_columns)
    return final_borders



def borders_brightness_filter(candidates, brightness, border):
    filtered = []
    for c in candidates:
        if ba.check_neighbours(c, brightness, border):
            filtered.append(c)
    return filtered

def turtle_filter(candidates, columns):
    filtered = []
    for c in candidates:
        is_valid = ba.turtle_check(c, columns[c[0]])
        if is_valid:
            filtered.append(c)
        else: continue
    return filtered

def borders_connectivity_filter(candidates, columns):
    filtered = []
    if candidates == []:
        return candidates
    filtered.append(candidates[0])
    for i in range(1, len(candidates)-1):
        if ba.brightness_connectivity_check(candidates[i][0], columns):
            continue
      #  elif second_border_connectivity_check(i, candidates, columns,filtered):
       #     continue
        else:
            filtered.append(candidates[i])
    return filtered

def borders_distance_filter(candidates, columns):
    filtered = []
    filtered.append((0, px.get_average_brightness(columns[0])))
    for i in range(1, len(candidates)-1):
        if ba.distance_connectivity_check(candidates[i][0], candidates, columns, filtered):
            continue
        else:
            filtered.append(candidates[i])
    filtered.append((len(columns)-1, px.get_average_brightness(columns[len(columns)-1])))
    return filtered