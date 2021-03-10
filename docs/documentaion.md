# btbpug Documentation


Welcome to the btbpug docs, here is where you will find all the information about btbpug.


## Word


```
  btbpug.word()
```

Returns a random word as a string.

## Lyrics


`
  btbpug.lyrics(song, artist)
`

Returns the lyrics to a song as a string.

**Parameters**
 - song[str] The title of the song
 - artist(Optional[str]) The artist of the song (Recommended; increases accuracy)

## Speed text


`
  class btbpug.SpeedText()
`

Represents a random paragraph of text

`
  text
`

Returns the contents of SpeedText() as a string

`
  image(text, backgroundColor, textColor)
`

Returns the contents of SpeedText() as a image

**Parameters**
 - text(Optional[str]) Overrides the random text and replaces it with inputed text.
 - backgroundColor(Optional[str]) Sets the background color of the image ('blue', 'green', 'black', etc)
 - textColor(Optional[str]) Sets the text color of the image ('blue', 'green', 'black', etc)

**Example**

```
  import btbpug as btb
  speedText = btb.SpeedText()

  print(speedText.text)
  #The example of painting can teach us not only how to manage our own work, but how to work together. A lot of the great art of the past is the work of multiple hands, though there may only be one name on the wall next to it in the museum.

  sp.image.save("speedText.png")
  #Saves an image of the text as a png
```

## madlibs.py

`class MadLibs(random, title, variables, text, questions)`

Represents a Madlibs and it's variables

**Parameters**
 - random(Optional[bool]) Defults to true, if set to false uses custom madlibs
 - title(Optional[str]) title of the madlibs; required if random is set to false
 - variables(Optional[list/tuple]) A list of inputs you want from the user (Ex: ['noun', ['adverb']]); required if random is set to false
 - text(Optional[str]) The text for the madlibs, replace anywhere you want your variables to go with {variable index}; required if random is set to false
 - questions(Optional[int])

 `questions()`

Returns the questions of the madlibs (Ex: ['verb', 'noun', 'place'])

`convert(answers)`

Returns the madlibs with all of the questions({number}) filled out

**Parameters**
 - answers[list/tuple] A list of answers you want to fill the madlibs out with

## reddit

`class btbpug.reddit(subreddit, limit)`

Represents a list of reddit post(s)

**Parameters**
 - subreddit[str] The subreddit you want to pull post from.
 - limit[Optional(int)] The number of post you want to pull from the subreddit, defaults to 1.

 `raw()`

Returns the full list of post

`post(index)`

Returns one post from the list

**Parameters**
 - index[int] The index of the post that will be returned

## meme

`class btbpug.meme()`

Represents a random meme

`title`
Returns the title of the reddit post the meme was gotten from as a string

`link`
Returns a link to the reddit post the meme was gotten from as a string

`image`
Returns the url of the memes image as a string

`comments`
Returns the amount of comments of the post as a integer

`score`
Returns the score of the reddit post the meme is from as a list (Ex: [upvotes, downvotes])

`raw()`
Returns the information as gotten from the API as a dictionary
