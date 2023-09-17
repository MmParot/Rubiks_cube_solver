#this is the idea section
#Add a number for each colour eg: 1 = red, 2 = blue etc.
#we could just muddle up the numbers but then 90% of the time the cube/position wouold be unsolvable.
#make a list  noting each side accordingly and then take 012(list figures)from the list and move
#them to the next.
#
#
#

#this is the upload section

import random
#this is the section where all the variables are set

time = 15

Notation = ["U", "D", "L", "R", "U'", "D'", "L'", "R'", "U2", "D2", "L2", "R2", "U2'", "D2'", "L2'", "R2'"]

white = ["0", "0", "0", "0", "0", "0", "0", "0", "0"]
yellow = ["1", "1", "1", "1", "1", "1", "1", "1", "1"]
blue = ["2", "2", "2", "2", "2", "2", "2", "2", "2"]
green = ["3", "3", "3", "3", "3", "3", "3", "3", "3"]
red = ["4", "4", "4", "4", "4", "4", "4", "4", "4"]
orange = ["5", "5", "5", "5", "5", "5", "5", "5", "5"]

scramble = []

#This is the code section
def scramble_notation(time,scramble):
    while  time >0:
        t = random.choice(Notation)
        scramble.append(t)
#       print(time)
        time = time - 1
    print(scramble)
    
scramble_notation(time = 15,scramble = [],  )h
    
    
