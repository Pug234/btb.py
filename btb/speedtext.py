from PIL import Image, ImageFont, ImageDraw
import textwrap
import requests

class SpeedText:
    def __init__(self):
        self.speedtext = requests.get('https://api.bytestobits.dev/speedtext2/').json()

    def text(self):
        return self.speedtext

    def image(self):
        img = Image.new('RGB', (600, 400), color = 'white')
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("./font/arial.ttf", 20)

        lines = textwrap.wrap(self.speedtext, width=60)

        y_text = 0
        for line in lines:
            width, height = font.getsize(line)
            draw.text((5, y_text), line, (0, 0, 0), font=font)
            y_text += 25


        return img
