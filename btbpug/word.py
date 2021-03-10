import requests

def word():
    return requests.get('https://api.bytestobits.dev/word').json()
