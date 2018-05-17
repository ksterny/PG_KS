import random

number = random.randint(0,3)

words = ["soccer", "lacrosse", "basketball", "football",]
hint1 = ["Played with you feet", "Played with a stick", "Played with your hands", "A lot of tackling"]
hint2 = ["Goal", "Bounce shot", "Basket", "Touchdown"]

secretword = words[number]
guess = ""
counter = 1

while True:
    print("Guess the word I am thinking of!")
    print("Type 'hint1', 'first letter', or 'give up' for answer.")
    guess = input()

    if guess == secretword:
        print("You win!")
        print("It took you " + str(counter) + " guesses.")
        break

    elif guess == "hint1":
        print(hint1[number])

    elif guess == "hint2":
        print(hint2[number])

    elif guess == "first letter":
        print(secretword[0])

    elif guess == "give up":
        print("Wow, you couldn't get it...")
        print("You failed " + str(counter) + " times.")
        break

    else:
        print("Guess again.")
        counter += 1
