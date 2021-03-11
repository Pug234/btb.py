import requests

def word(token):

    return requests.get('https://api.bytestobits.dev/word', headers=token).json()
