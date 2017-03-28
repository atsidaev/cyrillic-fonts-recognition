import os
import cv2
import matplotlib
import fontpainter as painter
import argparse
matplotlib.use('Qt5Agg')
#from matplotlib import pyplot as plt

#TODO: Добавить обработку всех шрифтов в директории, чтобы доставались из всех изображений все символы, а потом полученные раскидывать в файлы

#TODO: Добивать каждый сэмпл до определенного размера, чтобы потом скармилвать их системе
'''
Как это работает:
Берем директорию, вытаскиваем оттуда все ttf-файлы, из которых берем только кириллические символы 
и цифры, а затем печатаем их в png-alltogether файлы, из которых берем и с помощью opencv достаем
контуры и записываем их в png-файлы с названием %fontname-char-n.png%
'''
def get_countours(filename):
    img = cv2.imread(filename,  cv2.CV_8UC1)
    img = cv2.GaussianBlur(img, (3,3), 0);
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.bitwise_not(img, img);
    img2, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)
    return img2, contours, hierarchy

def write_countours(img, contours, name, dest):
    idx = 0
    for cnt in contours:
        idx += 1
        x, y, w, h = cv2.boundingRect(cnt)
        roi = img[y:y + h, x:x + w]
        cv2.imwrite(os.path.join(dest, str(idx) + '_' + name[:-4].replace("_alltogether","") + '.png'), cv2.bitwise_not(roi, roi))

def prepare_sample_from_dir(src, dest):
    files = [f for f in os.listdir(src) if os.path.isfile(os.path.join(src, f)) and (f.endswith(".otf")or f.endswith(".ttf"))]
    for font in files:
        painter.draw_all_symbols(os.path.join(src, font), dest)
    samples = os.listdir(dest)
    print(samples)
    for sample in samples:
        img, countours, hierarchy = get_countours(os.path.join(dest, sample))
        write_countours(img, countours, os.path.basename(sample), dest)


