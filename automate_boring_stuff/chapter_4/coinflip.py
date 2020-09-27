import random

numberOfStreaks = 0
for experimentNumber in range(100):
    coinFlip = []
    for i in range(100):
        coinFlip.append(random.randint(0,1) == 1 and 'H' or 'T')
    count = 0

    for i in range(1, len(coinFlip)):
        if (coinFlip[i] == coinFlip[i-1]):
            count+=1
        else:
            count = 0
        if count >= 6:
            numberOfStreaks+=1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))