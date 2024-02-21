with open('unis.txt', 'rt', encoding='utf-8') as infile:
    lines = [r.strip() for r in infile.readlines()]

#
# for line in lines:
#     has_uni = "university" in line.lower()
#     has_coll = "college" in line.lower()
#     has_school = "school" in line.lower()
#     has_inst = "institute" in line.lower() or "institution" in line.lower()
#     has_edu = "education" in line.lower()
#     has_acad = "academy" in line.lower()
#     has_reg = "regents" in line.lower()
#     # at first this seems okay but we're getting schools and inst
#
#     if not any([has_uni, has_coll, has_school, has_inst, has_edu, has_acad, has_reg]):
#         print(line)

## lol nope

with open('states.txt', 'rt', encoding='utf-8') as infile:
    states = [r.strip() for r in infile.readlines()]

for l in lines:
    if l in states:
        print(l)
        del states[states.index(l)]

print(states)
# so we know these are empty

with open('states.txt', 'rt', encoding='utf-8') as infile:
    states = [r.strip() for r in infile.readlines()]

schools = {}
state = "error"
for l in lines:
    if l in states:
        schools[l] = []
        state = l
        # ya this presumes the first one will be a label
    else:
        schools[state].append(l)

print(schools)

