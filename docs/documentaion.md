# btbpython Documentation


Welcome to the btbpython docs, here is where you will find all the information about btbpython.

## Client

`class btbpython.client(token)`

As of a new BytesToBits API update you now require tokens, client is a way for the wrapper to keep track of you and your token. (making more then 50 request per minutes to the API will get you rate limited)

**Parameters**
 - token[str] An API token that can make gotten from https://api.bytestobits.dev/account/


## Word


```
  btbpython.client().word()
```

Returns a random word as a string.

## Lyrics


`
  class btbpython.client().Lyrics(song, artist)
`

Returns information about a song

`title`
Returns the title of the song as a string

`artist`
Returns the name of the songs artist as a string

`lyrics`
Returns the lyrics of the song as a string

`raw()`
Returns a dictionary with all the information as gotten from the API

**Parameters**
 - song[str] The title of the song
 - artist(Optional[str]) The artist of the song (Recommended; increases accuracy)

## Speed text


`
  class btbpython.client().Text()
`

Represents a random paragraph of text

`
  text
`

Returns the contents of Text() as a string

`
  image(text, backgroundColor, textColor)
`

Returns the contents of Text() as an image

**Parameters**
 - text(Optional[str]) Overrides the random text and replaces it with inputted text.
 - backgroundColor(Optional[str]) Sets the background color of the image ('blue', 'green', 'black', etc)
 - textColor(Optional[str]) Sets the text color of the image ('blue', 'green', 'black', etc)

## madlibs

`class MadLibs(random, title, variables, text, questions)`

Represents a Madlib and its variables

**Parameters**
 - random(Optional[bool]) Defults to true. If set to false, it uses custom a madlib
 - title(Optional[str]) title of the madlib; required if random is set to false
 - variables(Optional[list/tuple]) A list of inputs you want from the user (Ex: ['noun', 'adverb']); required if random is set to false
 - text(Optional[str]) The text for the madlib. Replace anywhere you want your variables to go with {variable_index}; required if random is set to false
 - questions(Optional[int])

 `questions()`

Returns the questions of the madlib (Ex: ['verb', 'noun', 'place'])

`convert(answers)`

Returns the madlibs with all of the questions({number}) filled out

**Parameters**
 - answers[list/tuple] A list of answers you want to fill the madlibs out with

## reddit

`class btbpython.client().Reddit(subreddit, limit)`

Represents a list of reddit posts

**Parameters**
 - subreddit[str] The subreddit you want to pull posts from.
 - limit[Optional(int)] The number of posts you want to pull from the subreddit, defaults to 1.

 `raw()`

Returns the full list of posts

`post(index)`

Returns one post from the list

**Parameters**
 - index[int] The index of the post that will be returned

## meme

`class btbpython.client().Meme()`

Represents a random meme

**WARNING**: MEME ENDPOINT IS CURRENTLY EXTREMELY SLOW, RESULTS WILL TAKE A LONG TIME TO RETURN

`title`
Returns the title of the reddit post the meme is from as a string

`link`
Returns a link to the reddit post of the meme as a string

`image`
Returns the url of the meme's image as a string

`comments`
Returns the amount of comments the post has as an integer

`score`
Returns the score of the reddit post the meme is from as a list (Ex: [upvotes, downvotes])

`raw()`
Returns the information from the API as a dictionary

## info

`class btbpthon.client().Info`

Info bout the provided token

`used`
Returns the amount of request made in the last 60 seconds

`limit`
Returns the max amount of uses allowed in 60 seconds (returns none if the token has no limits)

`next_reset`
Returns the mount of time untill the token uses resets in seconds

`raw()`
Returns a dictionary with all the information as gotten from the API

#Async
Bytes to Bits now supports async. The async client is more bare bones and requires the user to filter more of the data.

To start a client you can use

example:
```
import btbpython, asyncio
client = btbpython.asyncClient("TOKEN")

async def test():
    print(await client.word())
    #dog

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(test())
finally:
    loop.close()
```

The async module supports

`await client.word()`

Returns a random word

`await client.text()`

Returns a paragraph of random text

`await client.reddit(subreddit:str, limit:int=None)`

Returns a list with a for each dictionary post that includes title, url, image link, subreddit name, upvotes, downvotes, amount of comments, and text.

`await client.meme()`

Returns a dictionary that includes title, url, image link, subreddit name, upvotes, downvotes, amount of comments, and text.

`await client.info()`

Returns a dictionary that includes, current amount of request to the API, max amount of request allowed, and time until amount of request reset in seconds

`await client.lyrics(song:str, artist:str=None)`

Returns a dictionary that includes the title of the song, the artist of the song, and the lyrics to the song.
