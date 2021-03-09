import requests

def word(self):
    return requests.get('https://api.bytestobits.dev/word').json()
