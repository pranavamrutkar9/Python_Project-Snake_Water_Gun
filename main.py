import random

# Mapping choices
youDict = {"s": 1, "w": -1, "g": 0}
mainDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Taking user input
yourChoice = input("Enter your choice (s for Snake / w for Water / g for Gun): ").lower()

if yourChoice not in youDict:
    print("Invalid input! Please choose s, w, or g.")
else:
    you = youDict[yourChoice]
    computer = random.choice([-1, 0, 1])
    
    print(f"\nYou chose {mainDict[you]}")
    print(f"Computer chose {mainDict[computer]}")

    # Result logic
    if computer == you:
        print("It's a draw!")
    elif (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
        print("Oh!! You Lose! :(")
    else:
        print("Hurray!! You Win! :)")
