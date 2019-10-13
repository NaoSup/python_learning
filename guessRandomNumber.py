import random


def checkIfIntegerInRange(number, min, max):
    if min <= number <= max:
        return True
    return False


def convertStringToInteger(userInput):
    try:
        return int(userInput)
    except ValueError:
        return False


def getCorrectInteger(userInput):
    userNumber = convertStringToInteger(userInput)
    while not userNumber:
        userInput = input("Please enter a correct integer: \n")
        userNumber = convertStringToInteger(userInput)
    return userNumber


def getUserNumber(userInput, limitRandom):
    # get user number
    userNumber = getCorrectInteger(userInput)

    # check if user number in range
    while not checkIfIntegerInRange(userNumber, 1, limitRandom):
        userInput = input(
            "Please choose a number between 1 and " + str(limitRandom) + ": \n")
        userNumber = getCorrectInteger(userInput)
    return userNumber


def checkIfGameOver(maxAttempts, numberAttempts, randomNumber, userNumber):
    remainingAttempts = maxAttempts - numberAttempts

    # The user found the random number
    if userNumber == randomNumber:
        guessWord = "guess" if numberAttempts == 1 else "guesses"
        print("Congratulations !! You won with " +
              str(numberAttempts) + " " + guessWord + ".")
        return True

    # The random number is lower than the user number
    elif userNumber > randomNumber:
        print("Lower...")

    # The random number is higher than the user number
    else:
        print("Higher...")

    # Only display number of attempts left if not last attempt
    if numberAttempts < maxAttempts:
        attemptWord = "attempt" if remainingAttempts == 1 else "attempts"
        print(str(remainingAttempts) + " " + attemptWord + " left. Try again:")
    return False


def main():
    # Init variables
    isGameOver = False
    limitRandom = 100
    maxAttempts = 10
    numberAttempts = 0

    # Get random number
    randomNumber = random.randint(1, limitRandom)

    # Get user number
    userInput = input("Choose a number between 1 and " +
                      str(limitRandom) + ": \n")

    # Check if user input is an integer
    userNumber = getCorrectInteger(userInput)

    # Check if the number is in the range
    while not checkIfIntegerInRange(userNumber, 1, limitRandom):
        userInput = input(
            "Please choose a number between 1 and " + str(limitRandom) + ": \n")
        userNumber = getCorrectInteger(userInput)

    # Start comparing userNumber to randomNumber
    while not isGameOver:
        # If no attempts left, exit the game
        if numberAttempts == maxAttempts:
            print("You don't have any attempt left...")
            print("The number to found was " +
                  str(randomNumber) + ". Better luck next time !")
            break

        # ask new user input if not the first attempt
        if numberAttempts > 0:
            userInput = input()
            userNumber = getUserNumber(userInput, limitRandom)

        # Check if user found random number
        numberAttempts += 1
        isGameOver = checkIfGameOver(
            maxAttempts, numberAttempts, randomNumber, userNumber)


# Start the program
if __name__ == "__main__":
    main()
