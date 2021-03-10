import requests
from typing import Union

class MadLibs:
    def __init__(self, random:bool=True, title:str=None, variables:Union[tuple, list]=None, text:str=None, questions:int=None):

        if random:
            self.madlib = requests.get("https://api.bytestobits.dev/madlibs").json()
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

    def questions(self):
        return tuple(self.vars)

    def convert(self, answers:Union[list, tuple]):
        text = self.text
        for i in range(self.q):
            print(1)
            text = text.replace("{" + str(i) + "}", answers[i])
        return text
