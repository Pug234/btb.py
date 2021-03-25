import requests, textwrap
from typing import Union
from PIL import Image, ImageFont
from typing import Union

def request(url, token):
    r = requests.get(url, headers=token)


    if r.status_code == 429:
      raise Exception(f'API response: {r.status_code}: To many request')


    return r.json()


class client:
    def __init__(self, token):
      self.token = {"Authorization": token}

    def lyrics(self, song: str, artist: str = None):
      song = song.replace(" ", "+")

      song = f'https://api.bytestobits.dev/lyrics/?song={song}'

      if artist != None:
          artist = artist.replace(" ", "+")
          song += f'&artist={artist}'

      song = request(song, self.token)

      if song == {"GeniusError": "Not Found"}:
          raise TypeError("GeniusError: Song not found")

      return song

    def word(self):
        return request("https://api.bytestobits.dev/word", self.token)

    def MadLibs(self, random:bool=True, title:str=None, variables:Union[tuple, list]=None, text:str=None, questions:int=None):
      return madlibs(random=random, title=title, variables=variables, text=text, questions=questions, token = self.token)

    def Text(self):
      return text(token = self.token)

    def Reddit(self, subreddit:str, limit:int=1):
      return reddit(subreddit=subreddit, limit=limit, token = self.token)

    def Meme(self):
      return meme(token=self.token)

    def Info(self):
      return info(token=self.token)

class text:
    def __init__(self, token):
        self.rantext = request('https://api.bytestobits.dev/text/', token)

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
        font = ImageFont.truetype("../font/arial.ttf", 20)



        y_text = 0
        for line in lines:
            width, height = font.getsize(line)
            draw.text((5, y_text + 5), line, textColor, font=font)
            y_text += 25


        return img

class madlibs:
    def __init__(self, random:bool=True, title:str=None, variables:Union[tuple, list]=None, text:str=None, questions:int=None, token:str=None):
        self.token = token

        if random:
            self.madlib = request("https://api.bytestobits.dev/madlibs", self.token)

            self.title = self.madlib['title']
            self.variables = self.vars = self.madlib['variables']
            self.questions = self.madlib['questions']
            self.text = self.madlib['text']

        else:
            if not (title and variables and text and questions):
                raise ValueError("Missing Required Parameters. Must include 'title', 'variables', 'text', 'questions'")
            self.madlib = {
                "title": title,
                "variables": variables,
                "text": text,
                "questions": questions
            }
            self.text = text
            self.questions = questions
            self.variables = variables
            self.title = title

    def questionList(self):
        return tuple(self.vars)

    def convert(self, answers:Union[list, tuple]):
        text = self.text
        for i in range(self.q):
            print(1)
            text = text.replace("{" + str(i) + "}", answers[i])
        return text

class meme:
    def __init__(self, token):
        self.r = request(f"https://api.bytestobits.dev/meme/", headers=token)

    @property
    def title(self):
        return self.r['title']

    @property
    def link(self):
        return self.r['link']

    @property
    def image(self):
        return self.r['url']

    @property
    def subreddit(self):
        return self.r['subreddit']

    @property
    def image(self):
        return self.r['url']

    @property
    def comments(self):
        return self.r['comments']

    @property
    def score(self):
        return (self.r['upvotes'], self.r['downvotes'])

    def raw(self):
        return self.r



class reddit:
    def __init__(self, token, subreddit:str, limit:int=1):
        self.r = request(f"https://api.bytestobits.dev/reddit/?subreddit={subreddit}&limit={limit}", token)

        if self.r == {"message": "Internal Server Error"}:
            raise Exception(f"Subreddit {subreddit} not found")

    def raw(self):
        return self.r

    def post(self, index:int):
        return self.r[index]

class info:
    def __init__(self, token):
        self.request = request(f"https://api.bytestobits.dev/info/", token)

    @property
    def used():
        return self.request['used']

    @property
    def limit():
        return self.request['limit']

    @property
    def untill_reset():
        return self.request['next_reset']

    def raw():
        return self.request
