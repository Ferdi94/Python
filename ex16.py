from sys import argv

script, filename = argv

print("We're going to erase %r" % filename)
print("If you don't want to delete press CTRL+C (^C)")
input("?")

print("Opening file...")
target = open(filename, "w")

print("Truncating this file, GOOD BY!")
target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("line 1: > ")
line2 = input("line 2: > ")
line3 = input("line 3: > ")

complete_string = line1 + "\n" + line2 + "\n" + line3 

target.write(complete_string)
target.close
target = open(filename, "r")
print("New file: ")
print(target.read())

print("Finaly the file would be closed!")
target.close