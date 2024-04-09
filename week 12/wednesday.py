import random
from collections import Counter

letters = list("abcde")
# print(letters)
# just seeing how it works
# row = [ random.choice(letters) for _ in range(10)]
# print(row)

data = []
for i in range(100):
    row = [ random.choice(letters) for _ in range(10)]
    counted_row = dict(Counter(row))
    name = "Round " + str(i) # this needs to be in the 0 pos
    # don't change 0th, but add new elem at 0
    # row.insert(0, name) # put name in at 0t # hw4 will use insert, but not like this
    # data.append(dict(Counter(row))) # maybe not the best place to cast
    counted_row['round'] = name
    data.append(counted_row)

print(data)

####

# make the temp row?

headers = ['round'] + letters
print(headers)

print([0] * len(headers))


for entity in data:
    print(entitiy)
    # remember that entity is a dict
    temp = [0] * len(headers)
    for key, value in entity.items():
        # key is col name
        # value goes into temp
        i = headers.index(key) # get index position of column
        temp[i] = value # set value in that index position
        print(temp)
    print(entity, temp)