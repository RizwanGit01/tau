on = True


def add():
    a = float(input("Enter a number. "))
    b = float(input("Enter another umber. "))
    print(a + b)

def subtraction():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a -b)

def multiply():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a * b)

def divide():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print(a / b)

while on:
    operations = input("Please type +, -, *, or /, or q()quit: ")
    if operations == '+':
        add()
    elif operations == '-':
        subtraction()
    elif operations == '*':
        multiply()
    elif operations == '.':
        divide()
    elif operations == 'q':
        on = False
    else:
        print("That operation does not exist. ")