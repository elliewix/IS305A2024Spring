# messing with while loops


# count to 10
# what cond is True while we want to do it?
# count < 10
# and when False it stop

count = 0
while count < 10:
    # print("not met", count)
    if count == 3:
        count += 2 #let's skip 4
        continue
    count += 1

import random

numsum = 0
# while sum != 100: # you might skip 100 exactly
numbers_picked = 0
while numsum < 100:
    numsum += random.randint(0, 10)
    numbers_picked += 1
    # print("ongoing total:", sum)

# print("final", sum, numbers_picked)
sample_size = 1000
all_numbers_picked = [] #store all samples
for _ in range(sample_size): # take 1000 samples
    numsum = 0
    # while sum != 100: # you might skip 100 exactly
    numbers_picked = 0
    while numsum < 100:
        numsum += random.randint(0, 10)
        numbers_picked += 1
        # print("ongoing total:", sum)
    all_numbers_picked.append(numbers_picked)
    # print("final", sum, numbers_picked)

# print(all_numbers_picked)
# print(sum(all_numbers_picked) / sample_size)


count = 0

while True:
    if count >= 10:
        break
    else:
        count +=1

print(count)