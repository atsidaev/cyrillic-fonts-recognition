#!usr/bin/python

import sys

import os
from fontTools import ttLib
from fontTools.unicode import Unicode

def normalize_ttf_filename(directory_path):
    for filename in enumerate(os.listdir(directory_path)):
        print(filename)
        os.chdir(directory_path)
        x,y = getFontName(filename[1])
        os.rename(filename[1], x + ".ttf")
        os.chdir("..")

def getFontName(filename):
    tt = ttLib.TTFont(filename)
    name = ""
    family=""
    FONT_SPECIFIER_NAME_ID = 4
    FONT_SPECIFIER_FAMILY_ID = 1
    for record in tt['name'].names:
        if b'\x00' in record.string:
            name_str = record.string.decode('utf-16-be')
        else:
            name_str = record.string.decode('utf-8')
        if record.nameID == FONT_SPECIFIER_NAME_ID and not name:
            name = name_str
        elif record.nameID == FONT_SPECIFIER_FAMILY_ID and not family:
            family = name_str
        if name and family: break
        tt.close()
    return name, family

def isCyrillicFont(filename):
    ISO_CMAP_TABLE = 2
    tt = ttLib.TTFont(filename)
    k = tt["cmap"].tables[ISO_CMAP_TABLE]
    charsList = []
    for x in k.cmap.items():
        charsList.append([x[0],x[1],(Unicode[x[0]])])
    charsList.sort(key=sortByAlphabet)
    cyrilicSymbolsRange = [int("0x401", 16)] + list(range(int("0x410",16), int("0x42F",16)+1,1)) + list(range(int("0x430",16),int("0x44F",16)+1,1)) + [int("0x451",16)]

    counter = 0
    for x in charsList:
            if x[0] in cyrilicSymbolsRange:
                counter += 1
    return counter == 66


def sortByAlphabet(input):
    return input[0]
