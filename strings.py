import functools

char = 'A'
print(ord(char))

char = 'a'
print(ord(char))

print('A' < 'a')
# because 'A' has ascii code 65 and 'a' has ascii code 97

def compare_chars(char1,char2):
        if (char1.lower() == char2.lower()):
              return - 1 if char1 < char2 else 1
        else:
              return  - 1 if char1.lower() < char2.lower() else 1


def herd_the_babies(string):
    sorted_list = sorted(list(string), key=functools.cmp_to_key(compare_chars))
    return ''.join(sorted_list)


print(herd_the_babies('aabbbAAAbbAABbaBaBa'))