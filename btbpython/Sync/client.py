import requests
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
