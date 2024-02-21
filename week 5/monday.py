import csv

with open('query.csv', 'rt', encoding= 'utf-8') as infile:
    headers, *rows = csv.reader(infile)

# headers is 1D list of col headers as strings
# rows is a 2D list of row content as strings

# let's load the dupes text file

with open('dupes.txt', 'rt', encoding='utf-8') as infile:
    dupes = infile.read().split()

# print(dupes)

# let's get into the data
all_dupes = []
all_data = {}
for r in rows:
    #let's knock out the failures
    # print(r)
    # if r in dupes: # would this work? no, because r is the whole row
    uri = r[0] # get the uri out
    if uri in dupes: # yes! check if that data point is there
        # print(uri)
        all_dupes.append(r)
    else: # for all the good ones
        # key is the file name (fname)
        # the "value" should be the row (r)
        # print(uri.split("/")[-1] + ".txt") # always print first
        fname = uri.split("/")[-1] + ".txt"
        all_data[fname] = r

# print(all_data)

#####
# wednesday
#####

# with open('dupe_failures.csv', 'w', encoding='utf-8', newline="") as outfile:
#     csvout = csv.writer(outfile)
#     csvout.writerow(headers) # takes 1D list, headers
#     csvout.writerows(all_dupes) # takes 2D list, our data
#


# print(all_data)

import pathlib

target = pathlib.Path('horse_files')
# print(target.exists())
target.mkdir(exist_ok=True)

for fname, content in all_data.items():
    f = pathlib.Path(fname)
    output_path = target / f
    # print(output_path.absolute())
    output_path.write_text(str(content))