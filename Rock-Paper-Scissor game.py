import random

print("    WELCOME TO ROCK PAPER SCISSORS GAME     ")
print("\n")

value = {1: "Rock", 2: "Paper", 3: "Scissors"}

while True:
    print("\n")
    user_input = input("Choose one:\n1. Rock 2. Paper 3. Scissors 0. Exit\n")
    
    if user_input.isdigit():
        user = int(user_input)
        if user == 0:
            print("Thanks for Playing..")
            break
        elif user not in value:
            print("Invalid choice. Please enter a number between 0 and 3.")
            continue
    else:
        print("Invalid input. Please enter a number.")
        continue
    
    print("\n")
    print("You chose:", value[user])
    
    computer = random.choice(list(value.values()))
    print("Computer chose:", computer)
    
    if user == 1 and computer == "Scissors":
        print("Congratulations! You won!")
    elif user == 2 and computer == "Rock":
        print("Congratulations! You won!")
    elif user == 3 and computer == "Paper":
        print("Congratulations! You won!")
    elif user == list(value.keys())[list(value.values()).index(computer)]:
        print("It's a draw!")
    else:
        print("Sorry, you lost.")
