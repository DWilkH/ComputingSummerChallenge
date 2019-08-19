
def userInput():
    return int(input("Please enter an integer between 1 and 99,999 \
inclusive to be converted into Linear B:...."))

denary = userInput()

def convert(num):
    number10000 = ""
    number1000 = ""
    number100 = ""
    number10 = ""
    number1 = ""
    ceiling = ""
    floor = ""
    
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
        while num >= 10:
            num = num - 10
            number10 = number10 + "-"
        while num >= 1:
            num = num - 1
            number1 = number1 + "|"

            
    while len(number10000) >= 2:
        number10000 = number10000[0:-2]
        ceiling = ceiling + "@"
        floor = floor + "@"
    if len(number10000) == 1:
        ceiling = ceiling + "@"
    if len(floor) < len(ceiling):
        floor = floor + " "
    while len(number1000) >= 2:
        number1000 = number1000[0:-2]
        ceiling = ceiling + "O"
        floor = floor + "O"
    if len(number1000) == 1:
        ceiling = ceiling + "O"
    if len(floor) < len(ceiling):
        floor = floor + " "
    while len(number100) >= 2:
        number100 = number100[0:-2]
        ceiling = ceiling + "o"
        floor = floor + "o"
    if len(number100) == 1:
        ceiling = ceiling + "o"
    if len(floor) < len(ceiling):
        floor = floor + " "
    while len(number10) >= 2:
        number10 = number10[0:-2]
        if len(ceiling) > len(floor):
            floor = floor + "="
        else:
            ceiling = ceiling + "="
    if len(number10) == 1:
        if len(ceiling) > len(floor):
            floor = floor + "-"
        else:
            ceiling = ceiling + "-"
    if len(floor) < len(ceiling):
        floor = floor + " "
    if len(number1) >= 5:
        number1 = number1[0:-5]
        ceiling = ceiling + "|||||"
        floor = floor + number1
    else:
        ceiling = ceiling + number1

    print(ceiling + "\n" + floor)


while denary > 99999 or denary == 0:
    print("Invalid input, please try again.")
    denary = userInput()

print(convert(denary))
