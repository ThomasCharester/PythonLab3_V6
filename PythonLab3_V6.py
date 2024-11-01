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


cons = "qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM"

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
n = int(input("Enter N: "))     ##################################
k = int(input("Enter K: "))     ##################################

counter = 1
for ch in text:
    if counter >= n and counter < k: f.write(ch)
    elif counter > k: break
    if ch == '\n': counter += 1

OpenRead('F2.txt')
text = f.read()

count = 0
for ch in text:
    if ch in cons: count += 1

print('\nVowels count: ' + str(count))

    







