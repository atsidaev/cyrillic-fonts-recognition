#!/usr/bin/python3

import os

from fontTools import ttLib
from fontTools.unicode import Unicode

def sort_by_alphabet(input):
    return input[0]

class Font:
    def __init__(self, file):
        self.path = file
        self.type = self.get_font_type(self.ttf)
        self.family, self.name = self.get_fontname(self.path)
        self.is_cyrillic = self.check_cyrillic_symbols(self.path)

    def get_fontname(font):
        name = ""
        family = ""
        FONT_SPECIFIER_NAME_ID = 4
        FONT_SPECIFIER_FAMILY_ID = 1
        for record in font['name'].names:
            if b'\x00' in record.string:
                name_str = record.string.decode('utf-16-be', 'ignore')
            else:
                name_str = record.string.decode('utf-8', 'ignore')
            if record.nameID == FONT_SPECIFIER_NAME_ID and not name:
                name = name_str
            elif record.nameID == FONT_SPECIFIER_FAMILY_ID and not family:
                family = name_str
            if name and family: break
        return name, family

    def check_cyrillic_symbols(filename):
        ISO_CMAP_TABLE = 0
        tt = ttLib.TTFont(filename)
        k = tt["cmap"].tables[ISO_CMAP_TABLE]
        charsList = []
        for x in k.cmap.items():
            charsList.append([x[0], x[1], (Unicode[x[0]])])
        charsList.sort(key=sort_by_alphabet)
        cyrilicSymbolsRange = [int("0x401", 16)] + list(range(int("0x410", 16), int("0x42F", 16) + 1, 1)) + list(
            range(int("0x430", 16), int("0x44F", 16) + 1, 1)) + [int("0x451", 16)]
        counter = 0
        for x in charsList:
            if x[0] in cyrilicSymbolsRange:
                counter += 1
        return counter == 66

'''

def normalize_ttf_filename(directory_path):
    dir = os.getcwd()
    os.chdir(os.path.abspath(directory_path))
    for filename in enumerate(os.listdir()):
#         apath = os.path.abspath(directory_path + "/" + filename[1])
         x,y = get_fontname(filename[1])
         extention = filename[1][-4:]
         os.rename(filename[1], x + extention)
    os.chdir(dir)

def remove_non_cyrillic_fonts(directory_path):
    for filename in enumerate(os.listdir(directory_path)):
        if not check_cyrillic_symbols(directory_path + "/" + filename[1]):
            os.remove(directory_path + "/" + filename[1])
'''