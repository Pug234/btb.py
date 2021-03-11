from PIL import Image, ImageFont, ImageDraw
import textwrap
import requests

class Text:
    def __init__(self, token):
    
        self.rantext = requests.get('https://api.bytestobits.dev/text/', headers=token).json()


    @property
    def text(self):
        return self.rantext

    def image(self, text:str=None, backgroundColor:str='white', textColor:str='black'):
        if text == None:
            text = self.rantext
        else:
            text = text


        lines = textwrap.wrap(text, width=60)

        img = Image.new('RGB', (600, (len(lines) * 25 + 15)), backgroundColor)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("./font/arial.ttf", 20)



        y_text = 0
        for line in lines:
            width, height = font.getsize(line)
            draw.text((5, y_text + 5), line, textColor, font=font)
            y_text += 25


        return img
