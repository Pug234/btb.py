import requests
from typing import Union
from .request import request

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
