"""import random
coin = random.choice(["heads","tails"])
print(coin)"""

"""from random import randint
list = randint(1,10)
print(list)"""

import random
cards = ["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)