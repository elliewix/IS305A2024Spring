import csv
from collections import Counter

with open('query.csv', 'rt', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

# dupes = [k for k, v in dict(Counter([r[0] for r in data])).items() if v != 1]
# with open('dupes.txt', 'w', encoding = 'utf-8') as outfile:
#     for d in dupes:
#         outfile.write(d + "\n")

# load the dupe file and read the content into a list of the dupe URLs
# remember: these are the unique wd uris that are duplicated, so the num
# should be lower than the actual number collected
with open('dupes.txt', 'rt') as infile:
    dupes = infile.read().split()

# print(dupes)

all_dupes = []
formatted_data = {}

for row in data:
    wd_id = row[0]
    # we want to save all duplicated data rows into another list
    # and omit them from our data
    # but proceed with the others
    if wd_id in dupes:
        # print("dupe!")
        all_dupes.append(row)
    else:
        # let's add this into a dictionary now
        filename = wd_id.split('/')[-1] + ".txt"
        # let's not be too fancy and just keep the original row of data
        # but for hw2 you would put the description text here
        formatted_data[filename] = row


# take care of this filtering first, since there are far fewer to handle.
print(len(dupes), len(all_dupes)) # we can see the count differences
print(formatted_data)
print(len(all_dupes) + len(formatted_data), len(data)) # these should be equal

# pretend that you are using this info to hit the wikidata api service to get the description of this horse
# and that's what would appear in these files. We aren't going to do that, but this setup would let us

# now that we have this dictionary, we can loop through it to save these text files

import pathlib

target = pathlib.Path('horse_data')

target.mkdir(exist_ok=True)

for fname, row in formatted_data.items():
    p = target / pathlib.Path(fname)
    p.write_text(str(row)) # deeply dumb example here, but punting this element
    # we could always go back through and format the text nicer when we added it to the dict