priceList = dict()

f = open('Flowers.txt', 'r')

for line in f:
    flowerName = ''
    step = False
    flowerPrice = ''

    for ch in line:
        if ch == ' ':
            step = True
            continue
        if not step:
            flowerName += ch
        else: 
            flowerPrice += ch

    priceList[flowerName] = int(flowerPrice)

avgPrice = 0
print("More than 10: ")
for item in priceList:
    if priceList[item] > 10 : print(item)
    avgPrice += priceList[item]

avgPrice /= len(priceList)

print("Average price is: "+ str(avgPrice))
