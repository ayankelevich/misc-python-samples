#BASIC STRUCTURES

# Case
if 1 > 2 or 4 < 4:
    print("Greater")
elif 5 == 5 and 7 != 7:
    print("Equal")
elif 7 < 8 < 9:
    print(not False)
else:
    print("Less"[0])

# Iterator
my_iterator = iter('12345')
next(my_iterator)
next_item = next(my_iterator)



# Map, Filter, Reduce
l9 = ['blah', 'yadda']
l10 = list(map(lambda x: x.upper(), l9))
# l10 = [map(lambda x: x.upper(), l9)] list of map object
print(l10)

l11 = list(filter(lambda x: 'd' not in x, l9))
print(l11)

from functools import reduce
# Get Max value
list17 = [5, 3, 4, 6, 2]
# list17 = []
# list17 = [9]
max1 = reduce((lambda x, y: x if x > y else y), list17) if list17 else None
print(max1)


# MISCELLANEOUS


#res = set(1, 3, 5, 6, 7)
#print(res)

# Medial values and division examples
def get_median(input_list):
    maxv = reduce(lambda x, y: x if x > y else y, input_list)
    minv = reduce(lambda x, y: x if x < y else y, input_list)
    input_list.remove(minv)
    input_list.remove(maxv)
    sorted_input_list = sorted(input_list)
    print('-'*12)
    print(sorted_input_list)
    if len(input_list) % 2 == 0: # even number of elements
        first_ind = len(input_list) // 2 - 1
        second_ind = first_ind + 1
    else:
        first_ind = second_ind = len(input_list) // 2
    print(first_ind, second_ind)
    return (sorted_input_list[first_ind]+sorted_input_list[second_ind])/2


print(get_median(list17))
# List and Set from range
# yield returns an iterator object, not a list
def my_range(upper: int):
    for i in range(upper):
        yield i     # returns value without resetting the local vars and continues

squares_list = [i ** 2 for i in list(my_range(6))]  # list comprehension
squares_set = {i ** 2 for i in list(my_range(6))}
squares_dict = {i: i**2 for i in list(my_range(6))}
print(squares_dict)

# Split and Join
bla = '-'.join(str(i).upper() for i in [1, 'a', 'b', 3])
bla1 = '-'.join(map(lambda k: str(k).upper(), [1, 'a', 'b', 3]))
#  This won't work, because whatever you pass to Lambda, must be iterative.  String is, int is not
# bla2 = '-'.join(map(lambda k: k.upper(), i) for i in [1, 'a', 'b', 3])
in_v = int(1)
# You can, however, convert int to string to simulate the effect
bla3 = '-'.join(map(lambda k: str(k).upper(), str(in_v)))
print(bla, bla3)  # 1-A-B-3

import re
print(re.split(r'\s+', "    one   two three   ".lstrip().rstrip()))


var = 'xxaxxaxxaxx'
count = 0
i = 0
print(var[-2:])
while True:
    pos = var.find(var[-2:], i)
    if pos == -1:
        break
    else:
        count += 1
        i = pos+1
    print(pos, count)

# Bricks
small = 6
big   = 1
goal  = 10
print(((big * 5 + small) >= goal) and (goal % 5 <= small))


#  Who wore it better ???
print(map(lambda k: k ** 2, [2, 3, 4]))
print(k ** 2 for k in [2, 3, 4])

print([map(lambda k: k ** 2, [2, 3, 4])])
print([k ** 2 for k in [2, 3, 4]])
print({k**2 for k in [2, 3, 4]})

print(list(map(lambda k: k ** 2, [2, 3, 4])))
print(list(k ** 2 for k in [2, 3, 4]))

print(__file__)

text = "bla yaddah"
split_list = text.split(' ')
# joined_list = split_list.join(' ')
joined_list = ' '.join(split_list)
print(split_list, joined_list)
# conditional comprehension
print([num for num in [2, 3, 4] if num != 2])

# ALL and ANY

print(all([1, 0]), any([1, 0]))

res_4 = "Yeah" if any(i in (1, 6) for i in [6, 0, 7, 5]) else "Nah"
print(res_4)

# For some reason, all(empty_list[]) is True
print(all([]), any([]))
# To correct, check the list itself
print(bool([]) and all([]), any([]))

print(__name__)





