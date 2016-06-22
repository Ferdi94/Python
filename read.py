from sys import argv

script, file = argv

if file != null:
    txt = open(file, "r") # 'r' for read
else:
    print("no file specified. \n Please enter a new file name: ")
    file = input('> ')
    txt = open(file, "r")

print txt.read()