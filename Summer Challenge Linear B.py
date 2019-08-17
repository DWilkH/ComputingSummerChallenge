
def userInput():
    return int(input("Please enter an integer between 1 and 99,999 \
inclusive to be converted into Linear B:...."))

denary = userInput()

while denary > 99999 or denary == 0:
    print("Invalid input, please try again.")
    denary = userInput()

    
