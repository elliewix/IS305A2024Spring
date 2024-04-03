import string
from collections import Counter

headers = list(string.ascii_lowercase)

word = dict(Counter("deoxyribonucleic"))

base = [0] * len(headers)

print(base)

for c, count in word.items():
    i = headers.index(c)
    base[i] = count

print(base)


import random

letters = list("abcdefg")

data = [[random.choice(letters) for _ in range(20)] for i in range(100)]

dict_data = {'round ' + str(i): dict(Counter(r)) for i, r in enumerate(data)}

headers = ['round'] + letters

rows = []

for round, counts in dict_data.items():
    template = [0] * len(headers)
    counts['round'] = round
    for key, count in counts.items():
        i = headers.index(key)
        template[i] = count
    rows.append(template)

print(rows)