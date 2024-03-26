words = ("chair headphones "
         "books æther řust "
         "DUDERÖ EKÅS").split()

# print(list(words))
print(words)
#let's get unique values

# letters = []
# for w in words:
#     l = list(w)
#     # print(l)
#     # letters.append(l) #not what we want, we don't want the interal list
#     # letters += l # list concat
#     letters.extend(l) # same as +, just a method
#
# print(letters)

# equiv
import string
letters = []
#add in all the a-z ascii characters
letters += list(string.ascii_lowercase)
[ letters.extend(list(w)) for w in words]

print(letters)
lower_letters = [ l.lower() for l in set(letters)]
# print(set(letters))
print(lower_letters)
print(len(lower_letters))
# these are the headers we would want

