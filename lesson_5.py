# import random
# import time

# name = input("enter your  name: ").capitalize()
# status = input(f"are you ready {name} (yes or no)")
# #xaxy o shut darav kompy te mardy pti radom tvery mutq anes
# if status == 'yes':
#     user_score = 0
#     comp_score = 0
    
#     time.sleep(0.5)
#     print(3)
#     time.sleep(1)
#     print(2)
#     time.sleep(1)
#     print(1)
#     time.sleep
#     print("Let's Go")
#     comp_number = random.randint(1, 5)
#     user_number = int(input("Guess the number 1-5: "))
#     if user_number == comp_number:
#         user_score += 1
#         print(f"{name} you win this round: ")
#             # user-1 comp-0
#         print(f" comp score = {comp_score} | user score = {user_score} | comp number = {comp_number} user number  {user_number} ")
#         comp_number = random.randint(1, 5)
#         user_number = int(input("Guess the number 1-5: "))
#         if user_number == comp_number: #user 2 comp 0
#             print(f" comp score = {comp_score} | user score = {user_score} | comp number = {comp_number} user number  {user_number} ")  
#             print(f"{name} jan duq haxteciq: ")
#             print("----end game----")
#             print(f"{name} win this game ")
#             print(f" comp score = {comp_score} | user score = {user_score} | comp number = {comp_number} user number  {user_number} ")
#         else: # 1-1
#             comp_score += 1
#             print("comp win this round: ")
#             print(f" comp score = {comp_score} | user score = {user_score} | comp number = {comp_number} user number  {user_number} ")
#             comp_number = random.randint(1, 5)
#             user_number = int(input("Guess the number 1-5: "))
#             if user_number == comp_number: #es 2 komp  1
#                 user_score += 1
#                 print("----end game----")
#                 print(f"{name} win this game ")
#                 print(f" comp score = {comp_score} | user score = {user_score} | comp number = {comp_number} user number  {user_number} ")
#             else: #es 1 komp 2
#                 comp_score += 1
#                 print("----end game----")
#                 print(" win this game ")
#                 print(f" comp score = {comp_score} | user score = {user_score} | comp number = {comp_number} user number  {user_number} ")
                
#     else:
#         comp_score += 1   #com - 1 user - 0
#         print("comp win this round: ")
#         print(f" comp score = {comp_score} | user score = {user_score} | comp number = {comp_number} user number  {user_number} ")
#         user_number = int(input("guess the numb beetwen 1-5: "))
#         if user_number == comp_number:
#             user_score += 1 # 1 - 1
#             print(f"{name} you win this round: ")
#             print(f" comp score = {comp_score} | user score = {user_score} | comp number = {comp_number} user number  {user_number} ")
#             comp_number = random.randint(1, 5)
#             user_number = int(input("Guess the number 1-5: "))
#             if user_number == comp_number: #es 2 comp 1
#                 user_score += 1
#                 print(f"{name} jan duq haxteciq\n comp_score = {comp_score} user_score = {user_score} user number = {user_number} comp number = {comp_number}")
#                 print("----End game----")
#         else: #comp 2 es 0
#             comp_score +=1
#             print("comp win this round: ")
#             print(f" comp score = {comp_score} | user score = {user_score} | comp number = {comp_number} user number  {user_number} ")
#             print("----End Game----")
# else:        
#     print("chilni chilni: ")



# year = int(input('enter year: ')) #2024


# if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
#     print('leap year')
# else:
#     print('Is not leap year')


# human_age = int(input('enter age: ')
# if human_age <= 0:
#     print('invalid')
# elif human_age <= 2:
#     print(human_age * 10.5)
# else:
#     print(2 * 10.5 + (human_age - 2) * 4)


# text = 'python'

# for element in text:
#     print(element, end='')


# for i in range(10, 21, 2):
#     print(i)

# text = 'python'
# for index in range(len(text)):
#     print(f'{index} -> {text[index]}')

# for index in range(len(text) - 1): # 0, 1, 2, 3, 4
#     print(f'{text[index]} -> {text[index + 1]}')

# text = 'python'
# for i in range(1, len(text)):
#     print(text[i - 1], text[i])


# text = 'python'

# for index, value in enumerate(text):
#     print(index, value) 

# print('-'*50)

# for index in range(len(text)):
#     print(index, text[index])


# for i in range(30):
#     print(f'Barev {i + 1}')

# for i in range(103, 118):
#     if i % 17 == 0:
#         print(i)
#         break
# else:
#     print('Chka tenc tiv! ')
        

# for i in range(1, 20):
#     if i % 17 == 0:
#         continue
#     print(i)
# else:
#     print('Chka tenc tiv! ')


# for i in range(1, 20):
#     if i % 17 == 0:
#         pass
#     print(i)
# else:
#     print('Chka tenc tiv! ')


# summ = 0
# count = 0 
# for i in range(6):
#     summ += i
#     count += 1
# print(summ)
# print(count)



# # summ = 0
# count = 0
# a = int(input('a: '))
# b = int(input('b: '))
# for i in range(a, b+1):
#     # summ += i
#     if i % 3 == 0:
#         count += 1

# # print(summ)
# print(count)


# n = int(input("N: ")) # 9
# for i in range(2, int(n**0.5) + 1): #2, 3, 4, 5, 6
#     if n % i == 0:
#         print('Parz chi')
#         break
# else:
#     print('Parz')


# import random
# user_score = 0
# comp_score = 0
# rounds = int(input("How many round do you want to play? "))

# for raund in range(1, rounds + 1): # 1, 2, 3, 4, 5
#     title = f'Raund {raund}'
#     print(title.center(40, '-'))
#     comp_number = random.randint(1, 5)
#     user_number = int(input("Enter number: "))
#     if user_number == comp_number:
#         user_score += 1
#         print('User win')
#         print(f'Scores: {user_score}|{comp_score} >> U={user_number}/C={comp_number}')
#     else:
#         comp_score += 1
#         print('Comp win')
#         print(f'Scores: {user_score}|{comp_score} >> U={user_number}/C={comp_number}')


# print('End Game')
# if user_score > comp_score:
#     print('User Win')
# elif comp_score > user_score:
#     print('Comp Win')
# else:
#     print('Draw')
    


