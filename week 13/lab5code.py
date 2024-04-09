import string

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

critters = ["Pikachu", "Mr. Mime", "Mega Charizard"]

parts = []

for name in critters:
    parts += ngram_letters(name, 2)

print(parts)
