import random

choices = ["Rock", "Paper", "Scissors"]

def getUserChoice():
    userInput = input("Choose Rock, Paper, or Scissors: ")
    return(userInput)

def getComputerChoice():
    computerInput = random.choice(choices)
    return(computerInput)

userChoice = getUserChoice()
computerChoice = getComputerChoice()

print("\n")
print("You chose " + userChoice)
print("The Computer Chose " + computerChoice + "\n")

def determineWinner(userChoice, computerChoice):
    if(userChoice == "Rock"):
        if(computerChoice == "Rock"):
            return("It's a tie")
        elif(computerChoice == "Paper"):
            return("You lost")
        elif(computerChoice == "Scissors"):
            return("You won")

    elif(userChoice == "Paper"):
        if(computerChoice == "Rock"):
            return("You Won")
        elif(computerChoice == "Paper"):
            return("It's a tie")
        elif(computerChoice == "Scissors"):
            return("You lost")

    elif(userChoice == "Scissors"):
        if(computerChoice == "Rock"):
            return("You lost")
        elif(computerChoice == "Paper"):
            return("You won")
        elif(computerChoice == "Scissors"):
            return("It's a tie")

winner = determineWinner(userChoice, computerChoice)
print(winner)