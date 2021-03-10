import requests
from typing import Union
#Ill add support for custom madlibs when I feel like it
class MadLibs:
    def __init__(self, random:bool=True, text:str=None, title:str=None, variables:list=None):

        if random == False and not isinstance(variables, list):
            raise TypeError('Object "variables" must be type list')

        if text == None:
            raise TypeError("Missing argument text")

        if title == None:
            raise TypeError("Missing argument title")

        if random == True:
            self.madlib = requests.get("https://api.bytestobits.dev/madlibs").json()
            self.title = self.madlib['title']
            self.vars = self.vars = self.madlib['variables']
            self.q = self.madlib['questions']
            self.text = self.madlib['text']
        else:
            self.madlib = {"title": title, "variables": variables, "text": text, "questions": len(variables)}
            self.text = text
            self.q = len(variables)
            self.vars = variables
            self.title = title

    def questions(self):
        return tuple(self.vars)

    def convert(self, answers:Union[list, tuple]):
        text = self.text
        for i in range(self.q):
            print(1)
            text = text.replace("{" + str(i) + "}", answers[i])
        return text

    def raw(self):
        return self.madlib
