import requests

def request(url, token):
    r = requests.get(url, headers=token)

    if r.status_code == 429:
      raise Exception(f'API response: {r.status_code}: To many request')

    return r.json()
