import random

random_num = random.randint(1, 100)
count = 0
while True:
    guess = int(input("please enter a number between 1-100: "))
    count+=1
    if guess>random_num:
        print("you guessed is to large ! ")
    elif guess< random_num:
        print("you guessed is to small !")
    else:
        print("you guessed the right number! ")
        print("you're taken ",count," guesses total, dude.")
        break


