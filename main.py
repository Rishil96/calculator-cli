# Calculator App
from art import logo


# Add function
def add(n1, n2):
    return n1 + n2


# Subtract function
def subtract(n1, n2):
    return n1 - n2


# Multiply function
def multiply(n1, n2):
    return n1 * n2


# Divide function
def divide(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError
    return n1 / n2


# Get operation
def get_operation():
    ip = input("Choose one of the below operators:"
               "\nAdd: +"
               "\nSubtract: -"
               "\nMultiply: *"
               "\nDivide: /\n")

    if ip not in operation.keys():
        print("Invalid Operator. Choose again.")
        return get_operation()

    return operation[ip]


# Get valid number from the user
def get_num(num_order: str):
    num = input(f"Enter {num_order} number: ")

    try:
        num = float(num)
    except TypeError:
        return 0
    return num


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)
is_on = True
continue_same = False
answer = 0

while is_on:
    # Get First number
    num1 = answer if continue_same else get_num("first")
    # Get operator
    operate = get_operation()
    # Get Second number
    num2 = get_num("second")

    # Operate answer
    answer = operate(num1, num2)
    # print answer
    print("Your answer is: ", answer)

    # Ask if continue with same answer or start fresh
    user_choice = input("\nChoose *Y* to continue with current answer"
                        "\n       *N* to start fresh with new values"
                        "\n       *E* to exit the calculator.").lower()

    if user_choice == "y":
        continue_same = True
    elif user_choice == "n":
        continue_same = False
    else:
        print("\nThanks for using the PyCalculator App!.")
        is_on = False
