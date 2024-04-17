import random

all_critters = {}
for i in range(10):
    level = random.randint(1, 30) #stop inclusive
    # hp = level * 5
    # hp = random.randint(5, level * 5)
    # damage = random.randint(2, level * 2)
    mod = random.random()
    print(mod)
    # mim overall hp should be 5
    critter_id = str(i).zfill(3)
    d = {'level': level,
         'hp': level * 5 * mod,
         'damage':level * 2}
    all_critters[critter_id] = d

print(all_critters)

import json
with open('critters.json', 'wt', encoding='utf-8') as outfile:
    json.dump(all_critters, outfile, indent=4)



# casting something to a set

word = "he is a happy horse"
letters = list(word)
print(letters)
print(set(letters))