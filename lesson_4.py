# import datetime

# now = datetime.datetime.now()
# print(now.hour > 9 and now.hour < 18)


# import random
# dice = random.randint(1, 6)
# print(f"Qo zary = {dice},aysinqn kstanas -> {dice == 1 or dice == 6}")


# import random
# import time
# sec=random.randint(1, 11)
# print(sec)
# time.sleep(sec)
# print(sec<=5)


# x = 5
# y = 4
# print(x > y)


# name = 'Arsen'
# print(name * 2)
# print(f'{name=}')
# print(name.center(20, '$'))

# x = int(input("X: "))
# y = int(input("Y: "))
# if x > y:
#     print('x is max')
# elif x == y:
#     print('x == y')
# else:
#     print('y is max')


# x = int(input("X: "))
# y = int(input("Y: "))
# if x > y:
#     print('x is max')
#     if x < 11:
#         print('y is less than 11')
#     else:
#         print('de uremn chgitem')
# elif x < y:
#     if y < 11:
#         print('x is less than 11')
#     elif y < 110:
#         print('x is less than 110')
#     else:
#         print('De chgitem')
#     print('y is max')
# else:
#     print('x == y')


# if 'o' in 'python' and len('python') < 11:
#     print('o tar ka python bari mej, u python bary karch bara')


# name = input('Enter your name: ').capitalize()
# exanak = input(f'Inch exanak e dursy {name} jan ?(arev/qami/andzrev) ').lower()
# if exanak == 'andzrev':
#     print('Mna tany python ara')
# elif exanak == 'arev':
#     bassein = input('Karoxa basein gnas ?(yes/no)').lower()
#     if bassein == 'yes':
#         tex = input('Vor baseinn es uzum gnas? ').lower()
#         if tex == 'harevani tun':
#             print("De du gna")
#         elif tex == 'dvin':
#             print('Ari im hetevic')
#         else:
#             print('De qez lav or')
#     else:
#         avto_status = input('Karoxa avton lvanas?(yes/no) ').lower()
#         if avto_status == 'yes':
#             print('Tuyn')
#         else:
#             print('Esinch anhaves lakot durs ekar!')
# else:
#     print('Taq hagnvi nor durs ari!!')


# import random
# import time
# name = input('Enter your name: ').capitalize()
# status = input(f"{name} jan are you ready(yes/no)? ").lower()
# if status == 'yes':
#     user_score = 0
#     comp_score = 0
#     print(3)
#     time.sleep(0.7)
#     print(2)
#     time.sleep(0.7)
#     print(1)
#     time.sleep(0.7)
#     print("Let's Go")
#     comp_number = random.randint(1, 5)
#     user_number = int(input('Guess the number between 1-5: '))
#     if user_number == comp_number: # es 1 comp 0
#         user_score += 1
#         print(f"{name} Win this round!!")
#         print(f"Comp = {comp_number} User = {user_number} | User_S = {user_score} Comp_S = {comp_score}")
#         comp_number = random.randint(1, 5)
#         user_number = int(input('Guess the number between 1-5: '))
#         if user_number == comp_number: # es 2 comp 0
#             user_score += 1
#             print('----End Game----')
#             print(f"{name} Win this Game!!")
#             print(f"Comp = {comp_number} User = {user_number} | User_S = {user_score} Comp_S = {comp_score}")
#         else:#es 1 comp 1
#             comp_score += 1
#             print(f"Comp Win this round!!")
#             print(f"Comp = {comp_number} User = {user_number} | User_S = {user_score} Comp_S = {comp_score}")
#             comp_number = random.randint(1, 5)
#             user_number = int(input('Guess the number between 1-5: '))
#             if user_number == comp_number: #Es 2 comp 1
#                 user_score += 1
#                 print('----End Game----')
#                 print(f"{name} Win this Game!!")
#                 print(f"Comp = {comp_number} User = {user_number} | User_S = {user_score} Comp_S = {comp_score}")
#             else: #es 1 comp 2
#                 comp_score += 1
#                 print('----End Game----')
#                 print(f"Comp Win this Game!!")
#                 print(f"Comp = {comp_number} User = {user_number} | User_S = {user_score} Comp_S = {comp_score}")
#     else: # es 0 comp 1
#         comp_score += 1
#         print(f"Comp Win this round!!")
#         print(f"Comp = {comp_number} User = {user_number} | User_S = {user_score} Comp_S = {comp_score}")
#         comp_number = random.randint(1, 5)
#         user_number = int(input('Guess the number between 1-5: '))
#         if user_number == comp_number: # es 1 comp 1
#             user_score += 1
#             print(f"{name} Win this round!!")
#             print(f"Comp = {comp_number} User = {user_number} | User_S = {user_score} Comp_S = {comp_score}")
#             comp_number = random.randint(1, 5)
#             user_number = int(input('Guess the number between 1-5: '))
#             if user_number == comp_number: # es 2 comp 1
#                 user_score += 1
#                 print('----End Game----')
#                 print(f"{name} Win this Game!!")
#                 print(f"Comp = {comp_number} User = {user_number} | User_S = {user_score} Comp_S = {comp_score}")
#             else: # es 1 comp 2
#                 comp_score += 1
#                 print('----End Game----')
#                 print(f"Comp Win this Game!!")
#                 print(f"Comp = {comp_number} User = {user_number} | User_S = {user_score} Comp_S = {comp_score}")
#         else: # es 0 comp 2
#             comp_score += 1
#             print('----End Game----')
#             print(f"Comp Win this Game!!")
#             print(f"Comp = {comp_number} User = {user_number} | User_S = {user_score} Comp_S = {comp_score}")
# else:
#     print('Du gites!')


# age = int(input("Age: "))
# if age <= 0:
#     print('Sxal tariq')
# elif age <= 2:
#     print('Noratsin')
# elif age <= 16:
#     pass
# elif age <= 18:
#     pass
# elif age <= 27:
#     pass
# elif age <= 63:
#     pass
# else:
#     pass


# amount = int(input('Qanak: '))

# if amount <= 1100:
#     money = amount * 25
# elif amount <= 2000:
#     money = 1100 * 25 + (amount - 1100) * 20
# elif amount < 5000:
#     money = 2000 * 20 + (amount - 2000) * 18
# else:
#     money = amount * 15

# print(f'${money}')