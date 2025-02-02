import random
def game():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    x = random.randint(1, 20)
    k = 0
    while(True):
        print("Take a guess.")
        a = int(input())
        k += 1
        if(a < x):
            print("Your guess is too low.")
        elif(a > x):
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {k} guesses!")
            return
game()