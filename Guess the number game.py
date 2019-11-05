import random
print("--Guess the number--")
difficulty = int(input('What should be the difficulty level? :\n1) Easy \n2) Medium \n3) Hard\n'))
Diff_add = 35
if difficulty == 1:
    Diff_add = 5
elif difficulty == 2:
    Diff_add = 15
elif difficulty == 3:
    Diff_add = 25
lucky_num = random.randint(1, 5 + Diff_add)
for a in range(1, 6):
    print('Enter your guess from 1 to', 5 + Diff_add, '. You currently have', 6 - a, 'tries:')
    guess = int(input())
    if guess == lucky_num:
        print('You win!^_^')
        break
    elif guess < lucky_num:
        print('You are too low')
    elif guess > lucky_num:
        print('You are too high')
else:
    print("You lose!*x*")
