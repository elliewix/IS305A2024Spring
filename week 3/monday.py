# prep for hw1

## assert statements

word1 = "hello"
word2 = "cats"

print(len(word1), len(word2))
## we don't want to program to move forward
## unless these words are the same length

## enter assert statements

word1 = "hello"
word2 = "cats!"

assert len(word1) == len(word2), \
    ("lengths should match, got: " +
    str(len(word1)) + " " + str(len(word2)))

## functions

# syntax overview
def name_goes_here(para1, para2):
    # you'll do stuff
    result = "whatever you did...."
    return result # note no ()

# example....
# we have two lists, they each have numbers
# we want a new list with the smallest number
# for each position, collect the nums into a new list
# return that new list

# need to use mutual index pattern

def get_smallest(left, right):
    # we're presuming the same length

    length = len(left)
    smalls = []
    for i in range(length):
        x = left[i]
        y = right[i]
        smallest = min(x, y)
        smalls.append(smallest)
    return smalls
# print(get_smallest([5, 10, 2, 20], [7, 2, 3, 50]))

# let's talk about zip

l = [5, 10, 2, 20]
r = [7, 2, 3, 50]

print(zip(l, r))
print(list(zip(l, r)))