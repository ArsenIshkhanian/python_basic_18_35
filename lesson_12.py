# nums = []
# while True:
#     number = int(input("Num: "))
#     if number == 0:
#         break
#     nums.append(number)
# mult = 1
# for i in nums:
#     mult *= i
# print(mult)




# words = []

# while True:
#     word = input("Word: ")
#     if word == '':
#         break
#     words.append(word)

# amenaerkar = 0
# amenaerkar_bar = ''
# for word in words:
#     if len(word) > amenaerkar:
#         amenaerkar = len(word)
#         amenaerkar_bar = word

# print(amenaerkar, amenaerkar_bar)



# list1 = [1, 2, 3, 4]
# list2 = [7, 8, 3, 10]

# for i in list1:
#     for j in list2:
#         if i == j:
#             print(j)


# list1 = [int(input(f"Number[{i + 1}]: ")) for i in range(int(input('How many element do you want for list 1? ')))]
# print('-'*50)
# list2 = [int(input(f"Number[{i + 1}]: ")) for i in range(int(input('How many element do you want for list 2? ')))]
# print(list1)
# print('-'*50)
# print(list2)


# link = 'https://www.youtube.com/watch?v=RRW2aUSw5vU'
# elements = link.split('=')
# print(elements[1])


# numbers = [1, 9, 3, 7, 2, 5]
# for number in numbers[::-1]:
#     if number % 2 == 1:
#         numbers.remove(number)
# print(numbers)





# import random
# qashoxner = ['Arsen', 'Lusy', 'Vardan', 'Nikan', 'Erik']
# qashvoxner = ['Arsen', 'Lusy', 'Vardan', 'Nikan', 'Erik']
# again = False
# while qashoxner != []:
#     qashox = random.choice(qashoxner)
#     qashvox = random.choice(qashvoxner)
#     while qashox == qashvox:
#         if len(qashvoxner) == 1:
#             again = True
#             break
#         qashvox = random.choice(qashvoxner)
#     if again:
#         qashoxner = ['Arsen', 'Lusy', 'Vardan', 'Nikan', 'Erik']
#         qashvoxner = ['Arsen', 'Lusy', 'Vardan', 'Nikan', 'Erik']
#         print('-----Noric sksenq-----')
#         again = False
#     else:
#         print(f'{qashox} -> {qashvox}')
#         qashoxner.remove(qashox)
#         qashvoxner.remove(qashvox)
    



# list_ = [6, 1, 3, 4, 2, 6, 7, 8, 9, 10]
# list_.sort() # O(nlogn)
# print(list_)
# list_.append(5)
# list_.insert(len(list_)//2, 5)


# nums = [4, 2, 7, 3, 2]
# for num in nums: #O(n)
#     if nums.count(num) > 1:#O(n)
#         print(num)
#         break



# nums.sort() #O(nlogn) #[2, 2, 3, 4, 7]

# for i in range(len(nums) - 1): #O(n)
#     if nums[i] == nums[i + 1]:
#         print(nums[i])

