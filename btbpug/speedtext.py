from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
import requests

class SpeedText:
    def __init__(self):
        self.speedtext = requests.get('https://api.bytestobits.dev/speedtext2/').json()

    @property
    def text(self):
        return self.speedtext

    @property
    def image(self, backgroundColor:str='white', textColor:str='black'):
        lines = textwrap.wrap(self.speedtext, width=60)

        img = Image.new('RGB', (600, (len(lines) * 25 + 15)), backgroundColor)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("./font/arial.ttf", 20)



        y_text = 0
        for line in lines:
            width, height = font.getsize(line)
            draw.text((5, y_text + 5), line, textColor, font=font)
            y_text += 25


        return img