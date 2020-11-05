from sys import argv
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
dir_path = os.path.dirname(os.path.realpath(__file__))

print("Current dir: %r" % dir_path)
print("Files in %r: %s" % (cwd, files))


script, filename = argv
fileOpen = dir_path + '/' + filename
txt = open( fileOpen )

print ("Here's your file %r:" % filename)
print (txt.read())

print ("Type the filename again:")
file_again = input("> ")
file_open_again = dir_path + '/' + file_again
txt_again = open(file_open_again)

print (txt_again.read())

# run command line: python .\ex\ex15_reading_files.py ex15_file_sample.txt