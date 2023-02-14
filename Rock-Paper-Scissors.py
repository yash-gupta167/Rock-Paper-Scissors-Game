import random

def getchoice():
    choices = ['Rock', 'Paper', 'Scissors']
    choice = input("Enter your choice: 1. Rock 2. Paper 3. Scissors\n")
    while choice not in ['1', '2', '3']:
        print("Invalid choice")
        choice = input("Enter your choice: 1. Rock 2. Paper 3. Scissors\n")
    return choices[int(choice)-1]



def computerchoice():
    return random.choice(['Rock', 'Paper', 'Scissors'])


def winner(userchoice, compchoice):
    if userchoice==compchoice:
        return "Tie"
    elif userchoice=='Rock' and compchoice=='Scissors':
        return "You Won"
    elif userchoice=='Paper' and compchoice=='Rock':
        return "You Won"
    elif userchoice=='Scissors' and compchoice=='Paper':
        return "You Won"
    else:
        return "Computer wins"

userpoint= 0
computerpoint= 0
for i in range(5):
    print(f"Round {i+1}: ")
    userchoice= getchoice()
    compchoice= computerchoice()
    print("You chose", userchoice)
    print("Computer chose", compchoice)
    roundwinner= winner(userchoice, compchoice)
    print(roundwinner)
    if roundwinner== "You win":
        userpoint = userpoint + 1
    elif roundwinner == "Computer wins":
        computerpoint = computerpoint + 1

print("Final scores:")
print("You:", userpoint)
print("Computer:", computerpoint)

if userpoint > computerpoint:
    print("You have won the game")
elif computerpoint > userpoint:
    print("Computer won")
else:
    print("It's a tie")
