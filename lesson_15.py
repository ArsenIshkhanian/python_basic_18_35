# data = {
#     'b': 8,
#     'a': 7
# }
# print(data)

# data = {7}
# data = set()
# print(type(data))


# data = {1, 1, 1, 2, 2, 2, 3, 4, 3, 2, 2, 1, 5, 65, 6, 5, 4}
# mylist = [1, 2, 3, 3, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 7, 5, 4, 3]
# data = set(mylist)
# print(data)


# data = {1, 2, 3, 4, 5}
# data.add(6)
# data.add(6)
# print(data)
# data.discard(67)
# data.remove(4)
# print(data)

# x = {1, 2, 3, 4, 5, 6}
# y = { 7, 8, 9}
# print(x.issuperset(y))
# print(y.issubset(x))
# print(x.intersection(y))
# print(x.difference(y))
# print(y.difference(x))
# print(x.isdisjoint(y))
# x.update(y)
# y.update(x)
# print(x)
# print(y)


# def test_func():
#     # print(10)
#     return 10


# x = test_func()
# print(x + 5)


# def func():
#     print(5)
# func()


# def func():
#     return 5
# print(func())


# def func():
#     return 15
#     print(14)
# print(func())


# def qarakusi(digit):
#     return digit ** 2

# x = 5
# y = qarakusi(x)
# print(y)


# def add(a, b):
#     return a + b
# a = int(input('X: '))
# b = int(input('Y: '))
# print(add(a, b))


# def add(a, b, c, d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
# x = 5
# y = 8
# z = 13
# f = 5
# add(x, y, d=z, c=f)


# def func(*args):
#     for value in args:
#         print(value)
# func(1, 2, 3, 4, 5, 5, 5, 4, 3, 3, 3, 3, 2, 1)


# def func(**kwargs):
#     print(kwargs)

# func(a=6, b=7, c=8)


# def func(*args, **kwargs):
#     print(args)
#     print('-'*50)
#     print(kwargs)
# func(1, 4, 3, 2, 1, 3, 4, 5, c=7, b=9, d=0, a=1)


# from matem import astichan
# # print(astichan(5, 2))
# print(astichan(6, 3))


# x = 5
# def func():
#     global x
#     x += 2
#     print(x)
# func()


# def f1(a):
#     a += 2
#     def f2(b, c):
#         return b + c
#     return f2(a, a * 2)
# print(f1(2))



# def is_prime(digit):
#     for divisor in range(2, digit):
#         if digit % divisor == 0:
#             return False
#     return True
    
# def filter_prime(elements):
#     primes = []
#     for element in elements:
#         if is_prime(element):
#             primes.append(element)
#     return primes

# elements = [i for i in range(2, 101)] #-> [2, 3, 4, ..., 99, 100]
# prime_elements = filter_prime(elements)
# print(prime_elements)


# x = lambda a, b: a == 3 and b == 4
# print(x(3, 4))


# def median(a, b, c):
#     return (a + b + c) - max(a, b, c) - min(a, b, c)

# a = int(input('A: '))
# b = int(input('B: '))
# c = int(input('C: '))
# print(median(a, b, c))


# def summ(a, b):
#     return a + b
# a = int(input('a: '))
# b = int(input('b: '))
# print(summ(a, b))