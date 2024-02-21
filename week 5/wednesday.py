for num in range(5,20):
    print(str(num).zfill(3))

roughtext = "Mega Pikachu[4], Jr."

cleantext = ""
for character in roughtext:
    if character.isalnum():
        cleantext += character

print(cleantext)

import math

math.sqrt()