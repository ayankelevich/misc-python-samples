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


res = list(solution([0, 1, 2, 3, 4, 5, 6, 7]))
for el in res:
    print(el)

def print_args(*args):
    for i in args:
        print(i)

def fYieldTest():
    for k in [2, 3, 4]:
        yield k ** 2

print(list(fYieldTest()))

def factorial(n):
    return (n*factorial(n-1) if n > 1 else 1)

print(factorial(9))

print_args(['blah', 'yadda', '========='], ('one', 2), {'three':3})

print(fYieldTest())
print([fYieldTest()])
print(list(fYieldTest()))