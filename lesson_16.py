#Ex. 15
# def compress(text):
#     sequence = '' # + 'a' + '2' + 'b' + '1' + 'c' + '2' + 'a' + '1'
#     count = 1 
#     for i in range(len(text) - 1): # 0, 1, 2, 3, 4
#         if text[i] == text[i + 1]:
#             count += 1
#         else:
#             sequence += text[i] + str(count)
#             count = 1

#     sequence += text[-1] + str(count)

#     return sequence
# print(compress("aabcc"))



#Ex. 16
# def is_prime(number):
#     for divisor in range(2, int(number**0.5) + 1):
#         if number % divisor == 0:
#             return False
#     return True

# def count_prime(numbers):
#     count = 0 # + 1
#     for number in numbers:
#         if is_prime(number):
#             count += 1

#     return count
# mylist = [i for i in range(2, 101)] #[2, 3, 4, 5 ...., 99, 100]
# print(count_prime(mylist))


# def f1(a):
#     a += 2
#     def f2(b, c):
#         return b + c
#     return f2(a, a * 2)
# print(f1(2))

# x = 5
# def func(a):
#     global x
#     x += a
#     print(x)
# func(6)

# def func():
#     x = 5
#     y = 5
#     b = 2
#     name = 'Arsen'
#     print(locals())
# func()


# text = 'madam'
# print(text == text[::-1])
# def palindrome(text):
#     left = 0 # 1 2
#     right = len(text) - 1 # 4 3 2
#     while left < right:
#         if text[left] != text[right]:
#             return False
#         left += 1
#         right -= 1

#     return True
# print(palindrome(text))


