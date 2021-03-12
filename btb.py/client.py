import requests
from typing import Union
from .madlibs import madlibs
from .lyrics import lyrics as lyric
from .word import word as w
from .text import Text as text
from .reddit import reddit
from .meme import meme

class client:
  def __init__(self, token:str):
      self.token = {"Authorization": token}

  def word(self):
      return w(token=self.token)

  def lyrics(self, song: str, artist: str = None):
      return lyric(song=song, artist=artist, token=self.token)

  def MadLibs(self, random:bool=True, title:str=None, variables:Union[tuple, list]=None, text:str=None, questions:int=None):
      return madlibs(random=random, title=title, variables=variables, text=text, questions=questions, token = self.token)

  def Text(self):
      return text(token = self.token)

  def Reddit(self, subreddit:str, limit:int=1):
      return reddit(subreddit=subreddit, limit=limit, token = self.token)

  def Meme(self):
      return meme(token=self.token)
