import json
import string

# read in a json file

infile = open('example.json', 'rt', encoding='utf-8')
data = json.load(infile)
infile.close()

# print(data)
print(data.keys()) # remmeber that data is a dict, so keys() will work
print(data['num_terms'])
print(data["cat"]) # first get into the node
print(data["cat"]['count'])
print(data["dome"]['count'])
print(data["cat"]["lines"])

# increment a list accumulator
data["cat"]['lines'].append("hello there I'm new")
print(data["cat"]["lines"])

# increment a counter

print(data["dome"]["count"])
print(data["dome"]["count"] + 1) # it really becomes the int

# normally counter = counter + 1
data["dome"]["count"] = data["dome"]["count"] + 1
print(data["dome"]["count"])
# alternatively, counter += 1
data['dome']['count'] += 1
print(data['dome']['count'])

# writing out a new json file

outfile = open("newdata.json", 'wt', encoding='utf-8')
json.dump(data, outfile, indent=4)
outfile.close()

print(data["cat"]["lines"])
