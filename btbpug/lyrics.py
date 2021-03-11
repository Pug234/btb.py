import requests

def lyrics(token, song: str, artist: str = None):
  song = song.replace(" ", "+")

  song = f'https://api.bytestobits.dev/lyrics/?song={song}'

  if artist != None:
      artist = artist.replace(" ", "+")
      song += f'&artist={artist}'

  song = requests.get(song, headers=token).json()

  if song == {"GeniusError": "Not Found"}:
      raise TypeError("GeniusError: Song not found")


  return song
