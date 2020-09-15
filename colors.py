"""
	#Author - Arvind Krishna
	#GitHub - github.com/ArvindAROO
	#LinkedIn - linkedin.com/in/aroo
	15 Sep 2020 - 17:42:20
"""
#NOTE: This is honestly not a project, many exist similar to this.
#NOTE: I was trying to implement this in DENO, didn't work out, so I decided to free hand in python
from sty import fg, bg, ef, rs
from sty import Style, RgbFg
import sys

#Get the file as Command Line Arguement itself
if len(sys.argv) == 1:
	print("Please enter filename to continue")
	sys.exit(0)
elif len(sys.argv) == 2:
	#The second arguement will be the filename
	file = sys.argv[1]
try:
	File = open(file, 'r')
except FileNotFoundError as F:
	print(F)
	sys.exit(0)
	#If such a File doesnt exist in the directory
file = open('colors.csv', 'r')
#Load the colors into the array,
#Just edit the 'colors.csv' to change colors
colorArray = []
for i in file.readlines():
	i.strip()
	i = [int(k) for k in i.split(',')]
	colorArray.append(i)
file.close()
File = File.readlines()
#Create a list of lines in the required file
for line in File:
	for i in range(len(line)):
		#Get the color for the particluar element in ascending order
		thisColor = colorArray[i%len(colorArray)]
		character = line[i]
		print(fg(thisColor[0], thisColor[1], thisColor[2])+ character + fg.rs, end = "")
	#After each Line, the list is rotated to give the effect of transition
	first = colorArray[0]
	colorArray.remove(first)
	colorArray.append(first)

#Credits: The beautiful poetry in the screenshot was written by Tim Peters,\
	  #You can view it by typing `import this` in Interactive console or running a .py file which contains `import this`