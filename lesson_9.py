# n = int(input("N: "))

# for i in range(n):
#     number = int(input("Number: ")) # 6
#     count = 0
#     for divisor in range(1, number + 1):
#         if number % divisor == 0:
#             count += 1
#     print(f'{number} -> {count} divisors')




# n = int(input("N: "))
# for number in range(2, n + 1): # 6
#     summ = 0 # 1 + 2 + 3
#     for divisor in range(1, number): # 1, 2, 3
#         if number % divisor == 0:
#             summ += divisor
#     if summ == number:
#         print(number)



# a = int(input("a: ")) # 12
# b = int(input("b: ")) # 18

# if a > b:
#     minimum = b
# else:
#     minimum = a

# #minimum = 12

# for divisor in range(1, minimum):
#     if a % divisor == 0 and b % divisor == 0:
#         print(divisor, end=' ')



# n = int(input("N: ")) # 5
# for number_1 in range(1, n): 
#     for number_2 in range(1, n): 
#         if number_1 + number_2 == n:
#             print(f'{number_1} + {number_2} = {n}')
#             break


# n = int(input("N: ")) # 5
# for i in range(1, n + 1):
#     for j in range(1, n + 2 - i):
#         print(n + 2 - j - i, end=' ')
#     print()
    


# n = int(input("N: "))
# for i in range(n):
#     for j in range(n):
#         print(i + 2 * j, end='\t')
#     print()




# n = int(input("N: "))

# for i in range(1, n + 1): # 1
#     for j in range(1, n + 1): # 1
#         if j == 1 or j == n:
#             print('|', end=' ')
#         elif i == 1 or i == n:
#             print('-', end=' ')
#         else:
#             print(' ', end=' ')
#     print()



# n = int(input("N: "))
# for i in range(1, n + 1): # 1
#     for j in range(1, n + 1): # 1
#         if i == j or j == n + 1 - i:
#             print('^', end=' ')
#         else:
#             print(' ', end=' ')
#     print()


# n = int(input("N: ")) # 4
# for i in range(1, n + 1): # 2
#     for j in range(1, n + i): # 3
#         if j > n - i:
#             print('#', end=' ')
#         else:
#             print(' ', end=' ')
#     print()




# n = int(input("N: ")) # 3

# for i in range(1, n + 1):
#     for j in range(1, n + 1 + i):
#         if j > n - i:
#             print('$', end=' ')
#         else:
#             print(' ', end=' ')
#     print()



# n = int(input("N: ")) # 4
# for i in range(1, n + 1): # 1
#     summ = 0 # 0
#     for j in range(1, n + i): # 1
#         if j > n - i:
#             if j <= n:
#                 summ += 1
#             else:
#                 summ -= 1
#             print(summ, end=' ')
#         else:
#             print(' ', end=' ')
#     print()

