#!usr/bin/python
from PIL import Image, ImageDraw, ImageFont
import os

def get_lower_cyrillic():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def get_upper_cyrillic():
    return get_lower_cyrillic().upper()

def get_digits():
    return "1234567890"

class FontPainter():
    def draw_all_font_symbols(font, fontsize, image_size, output_dir):
        image = Image.new('RGBA', (image_size[0], image_size[1]), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        img_font = None
        if font.type == "TTF":
            img_font = ImageFont.truetype(font.path, size=fontsize)
        elif font.type == "OTF":
            img_font = ImageFont.FreeTypeFont(font.path, size=fontsize)

        lower_letters = get_lower_cyrillic().replace("", " ")[1:-1]
        upper_letters = get_upper_cyrillic().replace("", " ")[1:-1]
        digits = get_digits().replace("", " ")[1:-1]

        draw.text((64, 64), lower_letters,(0, 0, 0), font=font)
        draw.text((64, 128), upper_letters,(0, 0, 0), font=font)
        draw.text((64, 192), digits, (0, 0, 0), font=font)

        image.save(generate_name(output_dir, font.name, "_all"))

#        image.save(os.path.join(output, os.path.basename(font)[:-4] + "_alltogether.png"))

    def draw_text(font, text, fontsize, image_size, soutput):
        '''
        image = Image.new('RGBA', (image_size[0], image_size[1]),(255,255,255))
        draw = ImageDraw.Draw(image)
        if os.path.basename(input).endswith(".ttf"):
            font = ImageFont.truetype(input, size=font_size)
        else:
            font = ImageFont.FreeTypeFont(input, size = font_size)
        draw.text((64, 64), str,(0, 0, 0), font=font)
        image.save(os.path.join(output, os.path.basename(input)[:-4] + "_alltogether.png"))
        '''
    def generate_name(dir, font_name, text):
        return os.path.join(dir, font_name, text, ".png")