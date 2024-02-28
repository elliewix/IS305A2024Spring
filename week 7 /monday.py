with open('dodec_mangled.dat', 'rt', encoding='utf-8') as infile:
    # reads in, strips space at front and end, then splits into newline
    coords = infile.read().strip().split("\n")

all_coords = [] # to hold all coord chunks
temp = [] # to hold a single x,y,z group

# we need groups of 3, because xyz coordinates
for point in coords:
    temp.append(point)
    # print(temp)
    # print(len(temp), temp) # so when len is 3, that's our trigger to collect/reset
    if len(temp) == 3: # temp being "full"
        all_coords.append(temp) # collect it up
        temp = [] # now reset temp to empty

# print(len(all_coords))
# print(temp) # check that this is empty

#######


with open('fav_fruit.txt', 'rt', encoding='utf-8') as infile:
    data = infile.read().split("\n")

# print(data)

# all_chunks = []
# temp = []
#
# for item in data:
#     if item == "done":
#         # print("found done") #let's just make sure we're seeing it
#         all_chunks.append(temp)
#         temp = []
#     else:
#         temp.append(item)

# # we can see that chunks are appearing
# print(all_chunks)
# # but is this everything?
# print(temp)

# not done! missing the last chunk!

# let's add a lookahead pattern

all_chunks = []
temp = []
last_pos = len(data) - 1

for i, item in enumerate(data):
    # we've got i as our current position
    if item == "done":
        # print("found done") #let's just make sure we're seeing it
        all_chunks.append(temp)
        temp = []
    elif i == last_pos: # checking if we're at the end of the list
        temp.append(item) # add the final item
        all_chunks.append(temp) # collect up the last temp
        # do we need to reset temp here?
    else:
        temp.append(item)
# so we kind of looked ahead, in that we are checking if we are at the last thing
# print(all_chunks)

# now for a proper lookahead
# instead of checking if the current value is done,
# we can check if the next value is done

all_chunks = []
temp = []
last_pos = len(data) - 1
for i, item in enumerate(data):
    # look ahead to the next value and check if done
    current = item #data[i] if you weren't using enumerate
    if current == "done":
        continue # let's ignore it
    elif i != last_pos: # if not the last one
        next_one = data[i + 1] # next one is only created in this conditon
        print(current, next_one)
        # take care of business here
        temp.append(item)
        if next_one == "done":
            all_chunks.append(temp)
            temp = []
    else:
        # print("wrapup")
        temp.append(item)
        all_chunks.append(temp)

print(all_chunks)

