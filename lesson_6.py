# a = int(input('a: '))
# b = int(input('b: '))

# if a > b:
#     maximum = a
# else:
#     maximum = b

# for i in range(maximum, a * b + 1, maximum):
#     if i % a == 0 and i % b == 0:
#         print(i)
#         break



# n = int(input("N: "))
# a = 0
# b = 1
# # c = a + b
# for i in range(n):
#     # a = b
#     # b = c
#     # c = a + b
#     # a, b = b, a + b
# print(a)

# c = a + b # 9
# a = c - a # 4
# b = c - a # 5
# print(a, b)



# n = int(input("N: "))
# summ = 1
# for i in range(1, n + 1):
#     summ *= i
# print(summ)


# digit = int(input("N: "))
# summ = 0
# for i in range(len(str(digit))):
#     summ += digit % 10
#     digit //= 10
# print(summ)




# months = int(input("Months: "))
# summ = 0
# for month in range(months):
#     salary = int(input("Salary: "))
#     summ += salary

# print(summ / months)



# a = int(input("a: ")) # 10
# b = int(input("b: ")) # 20

# summ = 0
# count = 0

# for digit in range(a, b + 1):
#     if digit % 3 == 0:
#         summ += digit
#         count += 1

# print(summ / count)



# for i in range(10, 100):
    #version 1
    # first = str(i)[0]
    # second = str(i)[1]
    # mult = int(first) * int(second)
    # if mult == i / 3:
    #     print(i)

    #version 2
    # first = i // 10
    # second = i % 10
    # if first * second == i / 3:
    #     print(i)



# n = int(input("N: ")) # 5
# summ = n * (n + 1) / 2 # 15 - 5 - 4 - 1 - 2 = 3

# for i in range(n - 1): # 0,1,2,3
#     remain_card = int(input("Card: "))
#     summ -= remain_card

# print(int(summ))