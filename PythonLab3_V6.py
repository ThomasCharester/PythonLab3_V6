def CreateAnyCost(fileName):
    global f
    try:
        f = open(fileName,'x')
    except:
        os.remove(fileName)
        f = open(fileName, 'x')

def OpenRead(fileName):
    global f
    f.close()
    f = open(fileName, 'r')


vowels = "aeiouyAEIOUY"

import os

CreateAnyCost("F1.txt")

line = '8=>'

print("Now you will enter data until you will send empty line")
while line:
    line = input()
    f.write(line + '\n')

    
OpenRead("F1.txt");
text = f.read()

f.close()
CreateAnyCost('F2.txt')
k = int(input("Enter K: "))     ##################################

counter = 1
for ch in text:
    if counter >= k and counter<k+5: f.write(ch)
    elif counter > k+5: break
    if ch == '\n': counter += 1

OpenRead('F2.txt')
text = f.read()

count = 0
for ch in text:
    if ch in vowels: count += 1

print('\nVowels count: ' + str(count))

    







