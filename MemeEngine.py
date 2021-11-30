"""Module for meme image generation."""
from PIL import Image, ImageDraw, ImageFont
from time import strftime
import random


class MemeEngine:
    """Class to generate meme image."""

    def __init__(self, path):
        """Initiate meme engine with path to file storage."""
        self.tmp = path

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Generate meme with given image(img), body, and author."""
        out_path = f'{self.tmp}/meme_{strftime("%Y%m%d%H%M%S")}'\
                   f'_{random.randint(0, 1000000)}.png'

        if width > 500:
            width = 500
        try:
            with Image.open(img_path) as img:
                ratio = img.height / img.width
                height = width * ratio
                img = img.resize((int(width), int(height)))
                font_size = int(img.height/20)

                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype('./_data/arial.ttf', font_size)

                x = random.randint(0, int(img.width/4))
                y = random.randint(0, int(img.height-font_size*2))

                draw.text((x, y),
                          text,
                          font=font,
                          stroke_width=2,
                          stroke_fill=(0, 0, 0),
                          fill=(255, 255, 255))
                draw.text((int(x*1.2), y+font_size),
                          '- '+author,
                          font=font,
                          stroke_width=2,
                          stroke_fill=(0, 0, 0),
                          fill=(255, 255, 255))
                img.save(out_path)

        except Exception:
            print('Invalid image file path.')
            pass

        return out_path
