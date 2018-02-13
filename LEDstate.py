# random number generator for array of 4 LEDs
import random

ledstates = [(0,0,0,0), (0,0,0,1), (0,0,1,0), (0,0,1,1),
            (0,1,0,0), (0,1,0,1), (0,1,1,0), (0,1,1,1),
            (1,0,0,0), (1,0,0,1), (1,0,1,0), (1,0,1,1),
            (1,1,0,0), (1,1,0,1), (1,1,1,0), (1,1,1,1)]
maxloop = 10000
loop = 0
count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

while (loop <= maxloop):
    randomstate = random.randint(0,15)
    #print(str(randomstate), end='\t', flush=False)
    #print(ledstates[randomstate])
    loop += 1
    count[randomstate] += 1
print(*count)