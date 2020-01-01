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

#List initaliation
l1 = [1, 2, 3, 7]
l1.append(4)
l1 += [5, 6]
l1.sort()  # does not return an object
l2 = sorted(l1, reverse=True)
l3 = list()

# Iterator
my_iterator = iter('12345')
next(my_iterator)
next_item = next(my_iterator)

# While a Tuple is immutable, you can create a new object and assign the pointer to it
t1 = ('a','b', 'c')
t1 = (t1[0], 'd', t1[2])

#Unpacking the tuple will NOT flatmap
c, d, e = ('bla', (23, 24), 'yadda')

# BUILDING DICTIONARIES

#Constructor
dict1 = {'key1': 'value1'}
dict1['key2'] = 'value2'
dict1['key0'] = 'value0'
var = 'key2'
vtp = dict1[var] if var in dict1 else 'not present'
print(vtp)
print(dict1.keys())
# Get ordered keys a
ordered_keys = sorted(dict1.keys())
print(ordered_keys)
# Get values
dvalues = list(dict1.values())

# enumerate provides positional value
def build_dict(list_in):
    for counter, value in enumerate(list_in):
        yield(counter, value)

d9 = dict(build_dict(['aa', 'bb', 'cc']))
print(d9)

# Count frequencies and print max frequency
l1 = [1, 2, 3, 3, 2, 2, 2]
d1 = {}
max_count = 0
for i in l1:
    d1[i] = 1 if i not in d1 else d1[i] + 1
    if d1[i] > max_count:
        max_count = d1[i]
        max_key = i
print(max_key, max_count)

# Sorted dictionary
dict11 = {'key21': 'value21', 'key11': 'value11', 'key31': 'value31', 'key41': 'value41', 'key00': 'value00'}
sorted_dict = dict((dkey, dict11[dkey]) for dkey in sorted(dict11.keys()))
print("sorted:")
print(sorted_dict)

# SETS
# Creation. Object, passed to set() must be iterable, so []
empty_set, set1 = set(), set([10])
# Looks like set is presumed if no dict structure (not for empty)
set2 = {11, 12, 15}
# Set operations
print(set1.union(set2))
print(set1.intersection(set2))
print(sorted(set2.difference(set1)))
# Subset ops
try:
    set2.remove('b')
except KeyError:
    print("Crap, no key")

if set2.issubset(set1):
    print("is subset")
else:
    print("is not")


# LIST COMPREHENSIONS
# list of tuples with all compbinations
burgers = ["beef", "chicken"]
toppings = ["cheese", "beans"]
meals = [(burger, topping) for burger in burgers for topping in toppings]
print(meals)

menu = [
    ["egg", "spam"],
    ["biscuit", "egg"]
]
no_spam_2 = [meal if "spam" not in meal else "skpipped" for meal in menu]
print(no_spam_2)

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
# Standalone lambda
flambda = lambda x: x*10
print(flambda(5))

# yield returns an iterator object, not a list
def my_range(upper: int):
    for i in range(upper):
        yield i     # returns value without resetting the local vars and continues

my_range_1 = my_range(5)
for i in my_range_1:
    print(i)


# Get all odd elements
def solution(input_par):
    print('144')
    yield input_par[1::2]


# res = set(solution([0, 1, 2, 3, 4, 5, 6, 7]))


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

def print_args(*args):
    for i in args:
        print(i)

print_args(['blah', 'yadda', '========='], ('one', 2), {'three':3})

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


def fYieldTest():
    for k in [2, 3, 4]:
        yield k ** 2

#def fYieldTest():
#    (yield k1 ** 2) for k1 in [2, 3, 4]

#  Who wore it better ???
print(map(lambda k: k ** 2, [2, 3, 4]))
print(k ** 2 for k in [2, 3, 4])
print(fYieldTest())

print([map(lambda k: k ** 2, [2, 3, 4])])
print([k ** 2 for k in [2, 3, 4]])
print({k**2 for k in [2, 3, 4]})
print([fYieldTest()])

print(list(map(lambda k: k ** 2, [2, 3, 4])))
print(list(k ** 2 for k in [2, 3, 4]))
print(list(fYieldTest()))

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

from collections import namedtuple

named_tuple = namedtuple("tuple_name", "attr1 attr2 attr3")

yadda = named_tuple("1", ['2', '3'], 5)
blah = named_tuple(4, 6, 5)

# when you print it, you get the class name "tuple_name"
print(yadda, yadda.attr2)
print(blah)

print(__name__)

def factorial(n):
    return (n*factorial(n-1) if n > 1 else 1)

print(factorial(9))




