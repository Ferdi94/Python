# imports the (arg)ument(v)ariable
from sys import argv

# unpack the argv
script, filename = argv

# load the given file frim argv in txt, to read ('r') 
txt = open(filename, "r")

# print the filename
print("Here's your file: %r" % filename)

# print the filen on console
print(txt.read())

# in the next two lines, asking
# for re-iput the filname
print("Type the filename again: ")
file_again = input('> ')

# print the text of the user file again
txt_again = open(file_again, "r")
print(txt_again.read())