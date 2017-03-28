#!usr/bin/python
from PIL import Image, ImageDraw, ImageFont
import os

def get_lower_cyrillic():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def get_upper_cyrillic():
    return get_lower_cyrillic().upper()

def get_digits():
    return "1234567890"

def draw_all_symbols(font_name, dest, fontsize, image_size):
    image = Image.new('RGBA', (image_size[0],image_size[1]),(255,255,255))
    draw = ImageDraw.Draw(image)
    font = None
    if os.path.basename(font_name).endswith(".ttf"):
        font = ImageFont.truetype(font_name, size=fontsize)
    else:
        font = ImageFont.FreeTypeFont(font_name, size = fontsize)
    lower_letters = get_lower_cyrillic().replace("", " ")[1:-1]
    upper_letters = get_upper_cyrillic().replace("", " ")[1:-1]
    digits = get_digits().replace("", " ")[1:-1]

    draw.text((64, 64), lower_letters,(0, 0, 0), font=font)
    draw.text((64, 128), upper_letters,(0, 0, 0), font=font)
    draw.text((64, 192), digits, (0, 0, 0), font=font)

    image.save(os.path.join(dest, os.path.basename(font_name)[:-4] + "_alltogether.png"))
'''
def draw_symbol(filename, symbol, dest):
    image = Image.new('RGBA', (2048, 320),(255,255,255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(filename,size=25)
    lower_letters = get_lower_cyrillic().replace("", " ")[1:-1]
    upper_letters = get_upper_cyrillic().replace("", " ")[1:-1]
    digits = get_digits().replace("", " ")[1:-1]

    draw.text((64, 64), lower_letters,(0, 0, 0), font=font)
    draw.text((64, 128), upper_letters,(0, 0, 0), font=font)
    draw.text((64, 192), digits, (0, 0, 0), font=font)

    image.save(os.path.join(dest, os.path.basename(filename)[:-4] + "_alltogether.png"))
'''
