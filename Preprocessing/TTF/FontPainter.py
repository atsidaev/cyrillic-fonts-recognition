#!usr/bin/python
from PIL import Image, ImageDraw, ImageFont
import Preprocessing.TTF.FontManipulator as manipulator
import os

def get_lower_cyrillic():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def get_upper_cyrillic():
    return get_lower_cyrillic().upper()

def get_digits():
    return "1234567890"

def draw_all_font_symbols(font, fontsize, image_size, output_dir):
    image = Image.new('RGBA', (image_size[0], image_size[1]), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    img_font = None
    if os.path.splitext(font)[1] == ".ttf":
       img_font = ImageFont.truetype(font, size=fontsize)
    elif os.path.splitext(font)[1] == ".ttf":
       img_font = ImageFont.FreeTypeFont(font, size=fontsize)

    lower_letters = get_lower_cyrillic().replace("", " ")[1:-1]
    upper_letters = get_upper_cyrillic().replace("", " ")[1:-1]
    digits = get_digits().replace("", " ")[1:-1]

    draw.text((64, 64), lower_letters,(0, 0, 0), font=img_font)
    draw.text((64, 128), upper_letters,(0, 0, 0), font=img_font)
    draw.text((64, 192), digits, (0, 0, 0), font=img_font)

    image.save(generate_name(output_dir, manipulator.get_fontname(font)[0], "_all"))

def draw_text(filename, text, fontsize, image_size, output_dir):
    image = Image.new('RGBA', (image_size[0], image_size[1]),(255,255,255))
    draw = ImageDraw.Draw(image)
    draw_font = None

    file, extension = os.path.splitext(filename)
    extension = extension.lower()

    if extension == ".ttf":
       draw_font = ImageFont.truetype(filename, size=fontsize)
    elif extension == ".otf":
        draw_font= ImageFont.FreeTypeFont(filename, size = fontsize)

    draw.text((64, 64), text,(0, 0, 0), font=draw_font)

    image.save(generate_name(output_dir, manipulator.get_fontname()[0], "sample"))
#have to test
def draw_sign(filename, sign, fontsize, image_size, output_dir):
    image = Image.new('RGBA', (image_size[0], image_size[1]),(255,255,255))
    draw = ImageDraw.Draw(image)
    draw_font = None
    file, extension = os.path.splitext(filename)
    extension = extension.lower()
    if extension == ".ttf":
       draw_font = ImageFont.truetype(filename, size=fontsize)
    elif extension == ".otf":
        draw_font= ImageFont.FreeTypeFont(filename, size = fontsize)
    w, h = draw.textsize(sign.encode('utf-8').decode('latin-1'), font = draw_font)
    x = (image_size[0] - w) / 2
    y = (image_size[1] - h) / 2
    draw.text((x, y), sign, (0, 0, 0), font = draw_font)
    image.save(os.path.join(output_dir, sign + "_" + os.path.basename(filename)[:-4] + ".png"))

def generate_name(dir, font_name, text):
    return os.path.join(dir, font_name + text + ".png")