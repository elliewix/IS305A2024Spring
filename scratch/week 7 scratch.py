with open('fav_fruit.txt', 'rt', encoding='utf-8') as infile:
    data = infile.read().split('\n')

all_chunks = []
temp_chunk = []

for item in data:
    if item == "done": #check if condition is met
        all_chunks.append(temp_chunk) # pack up
        temp_chunk = [] # reset
    else:
        temp_chunk.append(item) # gather data so long as we aren't the

# this works but unless there's something at the end

print(all_chunks) # missing the last chunk

# let's add enumerate in

all_chunks = []
temp_chunk = []

for i, item in enumerate(data):
    if item == "done": #check if condition is met
        all_chunks.append(temp_chunk) # pack up
        temp_chunk = [] # reset
    elif i == len(data) - 1:
        temp_chunk.append(item) #gather the current
        all_chunks.append(temp_chunk) # pack up
        # no need to reset
    else:
        temp_chunk.append(item) # gather data so long as we aren't the



with open('dodec_mangled.dat', 'rt', encoding='utf-8') as infile:
    coords = infile.read().split('\n')


all_xyz = []
temp = []

for point in coords:
    temp.append(point) # we can presume gather
    if len(temp) == 3:
        all_xyz.append(temp)
        temp = []

print(all_xyz)
print(temp) # this should be empty
# okay it kind of isn't because there's that last string there.
# we can fix this by running strip on the data before splitting it.

with open('dodec_mangled.dat', 'rt', encoding='utf-8') as infile:
    coords = infile.read().strip().split('\n')


all_xyz = []
temp = []

for point in coords:
    temp.append(point) # we can presume gather
    if len(temp) == 3:
        all_xyz.append(temp)
        temp = []

print(all_xyz) # last one should have
print(temp) # should actually be empty now
