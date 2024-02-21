with open('fav_fruit.txt', 'rt', encoding='utf-8') as infile:
    text = infile.read()

# print(text) # so this is just one string, we need to split it
lines = text.split("\n")
print(lines)
print(len(lines)) # always check your data, should be 35
print(len(text.split())) # so this gives us an extra one

# how I would normally split it into chunks
# chunks = [c.split('\n') for c in text.split("done\n")]
# print(chunks)

# print(lines)

# the long version of getting index position
i = 0
for l in lines:
    # print(l, i)
    i += 1

# with enumerate

done_is = []
for i, l in enumerate(lines):
    # print(i, l)
    if l.lower() == "done":
        # print(i, l) # check that it looks good
        done_is.append(i)
print(done_is)

# now that we have this list of i pos
# we can loop over those vals and see the data

for i in done_is:
    print(lines[i]) # and use it to look up the data