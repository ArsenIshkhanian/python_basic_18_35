# n = int(input("N: "))
# count = 0
# for i in range(1, n + 1):
#     number = int(input("Number: "))
#     status = True
#     for divisor in range(2, int(number**0.5) + 1):
#         if number % divisor == 0:
#             status = False
#             break

#     if status == True:
#         count += 1

# print(count)



# n = int(input("N: ")) # 6
# summ = 0 #.+ 1 + 2 + 6 + 24 + 120 + 720

# for i in range(1, n + 1): # 2
#     factorial = 1 # 2
#     for j in range(1, i + 1): # 1
#         factorial *= j
#     summ += factorial

# print(summ)




# maximum_summ = 0
# maximum_number = 0 
# while True:
#     number = int(input("Number: "))
#     if number == 0:
#         break

#     number_copy = number
#     summ = 0 
#     while number > 0:
#         summ += number % 10
#         number //= 10

#     if summ > maximum_summ:
#         maximum_summ = summ
#         maximum_number = number_copy

# print(maximum_summ, maximum_number)


# n = int(input("N: ")) # 5
# k = 1
# for i in range(1, n + 1):
#     for j in range(1, n + i):
#         if j > n - i:
#             if (i + j) % 2 == 1: 
#                 print(' ', end='\t')
#             else:
#                 print(k, end='\t')
#                 k += 2
#         else:
#             print(' ', end='\t')
#     print()



# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(1, 2 * n + 1):
#         if j > i and j < 2 * n + 1 - i:
#             print('.', end=' ')
#         else:
#             if j < n + 1:
#                 print(n + 1 - j, end=' ')
#             else:
#                 print(j - n, end=' ')
#     print()



# n = int(input("N: "))
# for i in range(1, n + 1): # 4
#     for j in range(i): # 0, 1, 2, 3
#         print(n - j, end=' ')
#     for k in range(2 * (n - i)): # 0, 1
#         print('.', end=' ')
#     for t in range(i): # 0, 1, 2, 3
#         print(n - j + t, end=' ')
#     print()




    