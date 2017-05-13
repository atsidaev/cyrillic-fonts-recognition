#!/usr/bin/python3
import sys
import os
import Preprocessing.TTF.FontManipulator as manipulator
import Preprocessing.TTF.FontPainter as painter


if __name__ == "__main__":
    src = os.path.abspath(sys.argv[1])
    dest = os.path.abspath(sys.argv[2])

    files = [f for f in os.listdir(src) if os.path.isfile(os.path.join(src, f)) and (f.endswith(".otf") or f.endswith(".ttf"))]
    s = ""
    text = s.join((painter.get_lower_cyrillic(), painter.get_upper_cyrillic(), painter.get_digits()))
    for f in files:
        manipulator.normalize_ttf_filename(os.path.join(src, f))
        for i in text:
            painter.draw_sign(os.path.join(src, f), i, 40, [64,64], dest)