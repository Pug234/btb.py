from .request import request

def word(token):

    return request("https://api.bytestobits.dev/word", token)
