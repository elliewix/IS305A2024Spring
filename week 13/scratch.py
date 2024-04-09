import string
import random

def ngram_letters(name, num):
    name = name.lower()
    nameparts = [n.strip(string.punctuation) for n in name.split()]

    grams = []
    if len(nameparts) > 1:
        for part in nameparts:
            grams += ngram_letters(part,num)
    else:
        for i in range(len(name)):
            if i + num > len(name):
                break
            grams.append(name[i:i + num])
    return grams


names = ['Bulbasaur','Ivysaur','Venusaur','Charmander',
         'Charmeleon','Charizard','Squirtle','Wartortle',
         'Blastoise']

grams = []

[grams.extend(ngram_letters(name, 2)) for name in names]

print(grams)
from collections import Counter
print(Counter(grams))

many_names = []

for _ in range(20):
    random_duos = []
    for _ in range(3):
        random_duos.append(random.choice(grams))

    # print("".join(random_duos))

# random.seed(10)
name_with_rules = random.choice(grams)

while len(name_with_rules) < 6:
    last = name_with_rules[-1]
    choice = random.choice(grams)
    while choice[0] != last:
        choice = random.choice(grams)
    print("current name", name_with_rules, "choice was", choice)
    name_with_rules += choice[-1]
print(name_with_rules)


