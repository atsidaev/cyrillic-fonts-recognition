#!usr/bin/python
from PIL import Image, ImageDraw, ImageFont
import os
#TODO:Перенести эти штуки в Sample Extractor чтобы как-то по-человечески все было 
def get_lower_cyrillic():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def get_upper_cyrillic():
    return get_lower_cyrillic().upper()

def get_digits():
    return "1234567890"

def ttf_to_sample(filename):
    image = Image.new('RGBA', (2048, 320),(255,255,255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(os.getcwd() + "/SampleFonts/" + filename,size=54)
    lower_letters = get_lower_cyrillic().replace("", " ")[1:-1]
    upper_letters = get_upper_cyrillic().replace("", " ")[1:-1]
    digits = get_digits().replace("", " ")[1:-1]

    draw.text((64, 64), lower_letters,(0, 0, 0), font=font)
    draw.text((64, 128), upper_letters,(0, 0, 0), font=font)
    draw.text((64, 192), digits, (0, 0, 0), font=font)

    image.save(os.getcwd() + "/SampleImages/" + filename + "_alltogether.png")