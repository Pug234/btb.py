from btbpug import BytesToBits

btb = BytesToBits()

#print(btb.word())

#print(btb.lyrics(song="My ")

#madlib = btb.MadLibs(random = True, text='One time {0} said to me {1}, what a joker {0} was', title='joke', variables = ['Person', 'Joke'])

#print(madlib.raw())


st = btb.SpeedText()
st.image.save('speedtext.png')
print(st.text)

#print(btb.reddit(subreddit='pugs', limit = 3).post(number=2))

#meme = btb.meme()

#print(meme.raw())
