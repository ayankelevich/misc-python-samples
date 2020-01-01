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