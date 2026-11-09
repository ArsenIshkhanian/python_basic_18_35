# a = 1
# b = 100
# steps = 0
# while a < b:
#     comp_number = (a + b) // 2
#     user_number = input(f'Qo tivy {comp_number}-is metsa, poqr te havasar ?(m/p/h): ')
#     steps += 1
#     if user_number == 'h':
#         print(f'Qo tivy exela {comp_number}, es gtel em {steps} qaylov')
#     elif user_number == 'm':
#         a = comp_number + 1
#     else:
#         b = comp_number - 1

#     print('Inch vor ban')



# for i in range(1, 11):
#     if i == 5:
#         continue
#         print('Chi tpelu meka')
#     print(i)



# for i in range(2): # 0, 1
#     for j in 'ab': # b
#         print(i, j, end=' | ')
#     print()

# print('prtsa es')


# for i in range(1, 6):
#     for j in range(1, 4):
#         print('*', end=' ')
#     print()


# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print('*', end=' ')
#     print()


# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i * j:<4}', end=' ')
#     print()



# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()


# n = int(input("N: "))

# for i in range(1, n + 1):
#     for j in range(1, n + 2 - i):
#         print(j, end=' ')
#     print()   

# for i in range(n + 1, 1, -1):
#     for j in range(1, i):
#         print(j, end=' ')
#     print()


# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if (i + j) % 2 == 0:
#             print('#', end=' ')
#         else:
#             print('.', end=' ')
#     print() 



# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j > n + 1 - i:
#             print('.', end=' ')
#         else:
#             print("#", end=' ')
#     print()


# n = int(input('n:'))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j or i == 1 or i == n or j == 1 or j == n:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')  
#     print()