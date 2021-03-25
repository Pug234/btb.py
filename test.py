import btbpython
client = btbpython.client("Gww3.XPWIDQAdahXyNXsGn0Xw")

print(client.word())
info = client.info()
print(info.used)
