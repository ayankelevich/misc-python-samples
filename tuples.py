# While a Tuple is immutable, you can create a new object and assign the pointer to it
t1 = ('a','b', 'c')
t1 = (t1[0], 'd', t1[2])

#Unpacking the tuple will NOT flatmap
c, d, e = ('bla', (23, 24), 'yadda')

from collections import namedtuple

named_tuple = namedtuple("tuple_name", "attr1 attr2 attr3")

yadda = named_tuple("1", ['2', '3'], 5)
blah = named_tuple(4, 6, 5)

# when you print it, you get the class name "tuple_name"
print(named_tuple)
print(yadda, yadda.attr2)
print(blah)