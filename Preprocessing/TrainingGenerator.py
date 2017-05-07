#!/usr/bin/python3
import sys
import os
import Preprocessing.TTF.Font as Font
import Preprocessing.TTF.FontPainter as painter

#тут мы собираем все вместе, собираем рисуем и соединяем
'''
def prepare_sample_from_dir(src, dest):
    files = [f for f in os.listdir(src) if os.path.isfile(os.path.join(src, f)) and (f.endswith(".otf")or f.endswith(".ttf"))]
    for font in files:
        painter.draw_all_symbols(os.path.join(src, font), dest,fontsize = 52, image_size = (3000, 3000))
    samples = os.listdir(dest)
    for sample in samples:
        img, countours, hierarchy = extract_all_countours(os.path.join(dest, sample))
        write_countours(img, countours, os.path.basename(sample), dest)

if __name__ == "__main__":
    prepare_sample_from_dir(sys.argv[1], sys.argv[2])
'''

if __name__ == "__main__":
    src = os.path.abspath(sys.argv[1])
    dest = os.path.abspath(sys.argv[1])
    files = [f for f in os.listdir(src) if os.path.isfile(os.path.join(src, f)) and (f.endswith(".otf") or f.endswith(".ttf"))]
    fonts = []
    for f in files:
        fonts.append(Font.Font(os.path.join(src, f)))

    text = str.join(painter.get_lower_cyrillic(), painter.get_upper_cyrillic(), painter.get_digits(), "")
    text = text.replace("", " ")[1: -1]

    cyrillic_fonts = [c for c in fonts if c.is_cyrillic == True]
#    for font in cyrillic_fonts:




