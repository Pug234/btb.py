# btbpug Documentation


Welcome to the btbpug docs, here is where you will find all the information about btbpug.


## Word


```
  btbpug.word()
```

Returns a random word as a string.

## Lyrics


```
  btbpug.lyrics(song, artist)
```

Returns the lyrics to a song as a string.

**Parameters**
 - song[str] The title of the song
 - artist(Optional[str]) The artist of the song (Recommended; increases accuracy)

## Speed text


```
  class btbpug.SpeedText()
```

Represents a random paragraph of text

```
  text
```

Returns the contents of SpeedText() as a string

```
  image
```

Returns the contents of SpeedText() as a image

**Example**

```
  import btbpug as btb
  speedText = btb.SpeedText()

  print(speedText.text)
  #The example of painting can teach us not only how to manage our own work, but how to work together. A lot of the great art of the past is the work of multiple hands, though there may only be one name on the wall next to it in the museum.

  sp.image.save("speedText.png")
  #Saves an image of the text as a png
```
