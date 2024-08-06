import functools


letters = ['a','z','x','p','q','s','b']
print(letters.sort())
print(letters)


print(sorted(letters))

print(sorted(letters,reverse=True))

nums = [5,8,1,9,2,3,10,6]

def compare_nums(a,b):
    return b - a

# In the case


def comparison(a,b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

comparison(3,100) # will return negative value...
comparison(100,3) # will return positive value
# or is a < b true? 

## if the comparison function accepts a and b and returns positive => swap the positions of a and b, b first followed by a

result = sorted(nums, key=functools.cmp_to_key(compare_nums))
print(result)


# 