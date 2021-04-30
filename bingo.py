import random

answer = random.randint(1, 100)
count = 0

while True:
    guess = int(input("Your guess? :"))
    count += 1
    
    if answer == guess:
        print("Bingo! It took %i guesses!" %count)
        break
    elif answer > guess:
        print("Bigger!")
    else:
        print("Smaller!")