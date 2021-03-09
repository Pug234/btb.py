from btb import BytesToBits
btb = BytesToBits()

#print(btb.word())

#print(btb.lyrics(song="My ", artist='AJR'))

#madlib = btb.MadLibs(random = True, text='One time {0} said to me {1}, what a joker {0} was', title='joke', variables = ['Person', 'Joke'])

#print(madlib.raw())


st = btb.SpeedText()
st.image().save('speedtext.png')
print(st.text())
