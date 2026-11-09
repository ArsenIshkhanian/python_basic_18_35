# tsrar = 12
# namak = int(input("Namak: ")) # 64
# count = 0
# for i in range(100):
#     if namak > tsrar:
#         namak /= 2
#         count += 2
#     else:
#         break

# print(count)

#-----------------------------------------------------

# toshak = int(input('mutqagreq toshaki chapy: ')) # 5000
# caxser = int(input('mutqagreq amsakan caxsacy: ')) # 6000
# total = 0 # 1000 + 1180 + 1365 + 1556 + ....
# p = 0.03
# for amis in range(10): # 9 angam khashvenq qani vor arajin amisy inflyacya chilnum 
#     total += caxser - toshak
#     print(f'Tsaxs-{caxser}')
#     caxser *= 1.03

# print(total)

#-----------------------------------------------------

# n = int(input("Steps: "))
# S = 0

# for i in range(n):
#     S += (-1)**i * (1 / 2 ** i)

# print(S)


#-----------------------------------------------------

# x = int(input("X: "))
# hamarich = 1
# haytarar = 1
# for i in range(1, 7):
#     hamarich *= (x - ((2 ** i) - 1))
#     haytarar *= (x - 2 ** i)


# if haytarar != 0:
#     print(hamarich / haytarar)
# else:
#     print('Error')

#-----------------------------------------------------

# G = int(input("Girls: "))
# B = int(input("Boys: "))

# if B > 2 * G or G > 2 * B:
#     print("Dzev chka")
# elif B == G:
#     print("BG" * G)
# elif B > G:
#     skizb = (B - G) * "BGB"
#     voti_vra = G - skizb.count('G')
#     verj = voti_vra * "BG"
#     print(skizb + verj)
# else:
#     skizb = (G - B) * "GBG"
#     voti_vra = B - skizb.count('B')
#     verj = voti_vra * "GB"
#     print(skizb + verj)


#-----------------------------------------------------
# i = 0
# while i < 5:
#     print(i)
#     i += 1


# while True:
#     print(5)
#     break


# age = int(input("Enter your age: "))
# while age <= 0:
#     print('Invalid value: ')
#     age = int(input("Enter your age: "))
    



# while True:
#     age = int(input("Age: "))
#     if age > 0:
#         break


# summ = 0
# while True:
#     number = int(input("Number: "))
#     if number == 0:
#         break
#     summ += number

# print(summ)


# number = int(input("Number: ")) # 4124314 -> 7: 19 
# summ = 0
# count = 0



# while number > 0:
#     summ += number % 10
#     number //= 10
#     count += 1
# print(f"{count}: {summ}")

#-----------------------------------------------------


# age = int(input("enter your age:"))
# summ = 0
# while age > 0 :
#     if age < 6 :
#         summ += 700
#     elif age < 18 :
#         summ += 1000
#     elif age < 63:
#         summ += 1500
#     else:
#         summ += 700

#     age = int(input("enter your age:"))


# print(summ)

#-----------------------------------------------------

# import random
# count_o = 0
# count_p = 0
# sequence = ''

# while count_o != 3 and count_p != 3:
#     kopek = random.choice("OP")
#     sequence += kopek
#     if kopek == 'O':
#         count_o += 1
#         count_p = 0
#     else:
#         count_p += 1
#         count_o = 0

# print(sequence)
