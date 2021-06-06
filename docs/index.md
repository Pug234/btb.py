# Welcome to btbpug

btbpug is a feature rich way to interact with the [BytesToBits API](https://api.bytestobits.dev/)

## Getting started

A guide on how to get btbpug up and running
First things first you will need a API token go to https://api.bytestobits.dev/account/ and sign up. Once you have your API token we can get started on installing the wrapper

### Installing


To install btbpug from PyPI use

`python3 -m pip install btbpython`


### Usage


Now that you have installed btbpug, lets start writing some code to see what we can do with it

Lets start simple by just returning a word

```
  import btbpug
  btb = btbpug.client(token=YOUR_TOKEN)
  print(btb.word())
  #citifications
```

Great, that all worked! For information on what you can do with this library look though the rest of the [documentation](https://github.com/Pug234/btb.py/blob/main/docs/documentaion.md). For more examples of using this library check out [Examples](https://github.com/Pug234/btb.py/tree/main/examples).
