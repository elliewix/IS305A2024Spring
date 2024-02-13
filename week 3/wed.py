import numpy

l = [11, 5, 10, 2, 20, -10, 5]
r = [16, 7, 12, -13, 50, 50, 15]

print(zip(l, r))
print(list(zip(l, r)))

nums = []
for x, y in zip(l, r):
    # add in some logic
    x_invalid = (x < 0) or (x > 20)
    y_invalid = (y < 0) or (y > 20)
    # if x < 0 or y < 0 or x> 20 or y > 20:
    # #long but gets the job done
    if x_invalid or y_invalid:
        nums.append(-1)
        # print("-1")
    elif (x <= 10) and (y <= 10):
        nums.append(min(x,y))
        # print(min(x, y))
    # elif (x <= 20) and (y <= 20): #oops
    elif (x > 10) and (y > 10):
        nums.append(max(x,y))
        # print(max(x,y))
    else:
        nums.append(-1)
        # print("-1")

print(nums)