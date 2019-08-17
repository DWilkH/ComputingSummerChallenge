
def userInput():
    return int(input("Please enter an integer between 1 and 99,999 \
inclusive to be converted into Linear B:...."))

denary = userInput()

def convert(num):
    number10000 = ""
    number1000 = ""
    number100 = ""
    number20 = ""
    number10 = ""
    number1 = ""
    while num > 0:
        while num >= 10000:
            num = num - 10000
            number10000 = number10000 + "@"
        while num >= 1000:
            num = num - 1000
            number1000 = number1000 + "O"
        while num >= 100:
            num = num - 100
            number100 = number100 + "o"
        while num >= 20:
            num = num - 20
            number20 = number20 + "="
        while num >= 10:
            num = num - 10
            number10 = number10 + "-"
        while num >= 1:
            num = num - 1
            number1 = number1 + "|"
    return(number10000 + number1000 + number100 + number20 + \
           number10 + number1)

while denary > 99999 or denary == 0:
    print("Invalid input, please try again.")
    denary = userInput()

print(convert(denary))
