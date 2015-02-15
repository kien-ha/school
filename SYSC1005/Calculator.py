# Calculator Program

def add (x, y):
    """Returns the sum of the variables, x & y"""
    return x + y

def subtract (x, y):
    """ Returns the difference of the variables, x & y """
    return x - y

def multiply (x, y):
    """ Returns the product of the variables, x & y """
    return x * y

def divide (x, y):
    """ Returns the quotient of the variables, x & y """
    return x / y


def print_menu():
    """Print's the menu

    Prints 5 options:
    - add
    - subtract
    - multiply
    - divide
    - exponents
    """
    print("Select operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponents")

#The Calculator
n = "yes"
while True:
    if n == "no":
        break

    print_menu()

    choice = input ("Enter choice (1 / 2 / 3 / 4 / 5): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":  # Add
        """ Returns the sum of the two variables """
        c = num1 + num2
        print (c)

    elif choice == "2":  # Subtract
        """ Returns the difference between two variables """
        c = num1 - num2
        print (c)

    elif choice == "3": # Multiply
        """ Returns the product of the two variables """
        c = num1 * num2
        print (c)

    elif choice == "4": # Divide
        """ Returns the quotient of the two variables """
        c = num1 / num2
        print(c)

    elif choice == "5": # Exponents
        """ Exponent function where  num1 is the base and num2 raises it to some power """
        c = num1 ** num2
        print (c)

    n = input("Want another math calculation (yes/no)?: ")
