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
