# x = ('Arsen', '+', 19, 0.9)
# x = 7, 8, 0
# print(type(x))
# for i in range(len(x)):
#     print(i)


# x = [1, 2, 3, 4, 'Arsen']
# print(x)
# print(type(x))


# x = [5, 4, 6, 3, 1, 2]
# x.sort(reverse=True)
# print(x)

# x = ['g', 'c', 'a', 'v', 'b']
# x.sort()
# print(x)

# x = ['Arsen', 'is', 'Vardan', 'Erik']
# x.sort(key=len)
# print(x[-1])


# x = [6, 5, 4, 3, 1, 2]
# # for i in range(len(x)):
# #     print(f'{i} -> {x[i]}')

# for i in range(6):
#     print(i)
# print('-'*50)
# for i in x:
#     print(i)


# x = [6, 5, 3, 1, 2]
# x.append(7)
# x.insert(2, 8)
# x = x + 7
# print(x)


# a = [1, 2, 3]
# b = [4, 5, 6]
# a.append(b)
# a = a + b
# a.extend(b)
# print(a)


# x = [1 ,2 ,3 ,4 , 5]
# x[2] = 8
# print(x)

# x = [1, 2, 3, 4, 5, 6]
# x.remove(3)
# deleted_element = x.pop()
# print(deleted_element)
# x.pop(2)
# print(x)
# del x[1:]
# print(x)


# x = [1, 2, 3, 4, 5, 6]
# print(x.index(6))
# print(sum(x))
# print(max(x))
# print(min(x))

# x = ['Arsen', 'Is', 'wefqwdq']
# print(max(x, key=len))


# x = [1, 2, 3]
# y = x
# x.append(4)
# print(y)


# from copy import deepcopy
# x = [1, 2, 3, 4 ,5, 6, ['a', ['b', 'c']]]
# y = deepcopy(x)
# y = x.copy()
# y = x[::]
# y = x[:]
# y = list(x)
# x[6][1][1] = 168
# print(y)
# print(x)

# x = [1, 2, 3, 2, 3, 5, 5, 4, 3, 1, 2, 3, 4]
# x.clear()
# x = []
# print(x.count(9))

# x = [-9, 0, 1, 2, -1, -65, -4, -3, 12, 4]
# y = [element for element in x if element > 0]
# y = ['bacasakan' if element < 0 else 'drakan' for element in x]
# for element in x:
#     if element > 0:
#         y.append(element)

# print(y)


# x = [[1, 2, 3], [4, [5, 6]], [7, 8, 9]]
# print([i for element in x for i in element])




# x = [1, 2, 3]

# for i in range(len(x)):
#     print(i, x[i])

# #----------------------------

# for index, value in enumerate(x):
#     print(index, value)




# x = [1, 2, 3]
# y = ['a', 'b', 'c']
# [(1, 'a'), (2, 'b')]

# for i, j in zip(x, y):
#     print(i ,j)



# x = [1, 2, 3]
# y = ['a', 'b', 'c']

# for i in range(3):
#     print(x[i], y[i])



# list_ = [1, 2, 3, 4, 5, 6, 7]
# print(sum([i for i in list_ if i % 2 == 0]))


# list_ = [0, 1, 2 ,5 , 8, 9, 4]
# summ = 0
# for i in list_:
#     print(i)


# list_ = [int(input(f'number[{i + 1}]: ')) for i in range(int(input("Range: ")))]
# print(list_)