# import random
# # import msvcrt -> msvcrt.getwche()
# import readchar

# zombi_step = random.choice('awsd')

# score_emoji = '⭐'
# score = 0

# hp = 3
# hp_emoji = '❤️'
# n = int(input("N: ")) 

# bomb_emoji = '💣'
# bomb_row = random.randint(1, n) 
# bomb_column = random.randint(1, n) 

# monkey_emoji = '🐵'
# monkey_row = random.randint(1, n) 
# monkey_column = random.randint(1, n) 

# banana_emoji = '🍌'
# banana_row = random.randint(1, n) 
# banana_column = random.randint(1, n) 

# while True:
#     for i in range(1, n + 1): 
#         for j in range(1, n + 1): 
#             if i == monkey_row and j == monkey_column:
#                 print(monkey_emoji, end='\t')
#             elif i == banana_row and j == banana_column:
#                 print(banana_emoji, end='\t')
#             elif i == bomb_row and j == bomb_column and score >= 3:
#                 print(bomb_emoji, end='\t')
#             else:
#                 print('*', end='\t')
#         print()
#     print(hp * '❤️ ')
#     print(score * score_emoji)
#     print('\n')
#     print(f'{monkey_emoji} -> {monkey_row}|{monkey_column}')

#     print('Enter the step: q->quit: ')
#     monkey_step = readchar.readkey()
#     monkey_step = monkey_step.lower()
#     if monkey_step == 'q':
#         break
#     elif monkey_step == 'w':
#         if monkey_row == 1:
#             monkey_row = n
#         else:   
#             monkey_row -= 1

#     if monkey_row == banana_row and monkey_column == banana_column:
#         score += 1
#         banana_row = random.randint(1, n)
#         banana_column = random.randint(1, n)
#     elif monkey_row == bomb_row and monkey_column == bomb_column and score >= 3:
#         hp -= 1
#         bomb_row = random.randint(1, n)
#         bomb_column = random.randint(1, n)