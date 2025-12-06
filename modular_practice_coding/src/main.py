from .subtract import minus_two_number
from .op_divide import divide
from .op_multiply import multiply
from .add import add_two_number


def calculator(x=input("Enter the operation: ")):
    
    a,b = int(input("Enter the value: ")),int(input("Enter the value: "))
    
    if x=="add":
        print(add_two_number(a,b))

    elif x=='minus':
        print(minus_two_number(a,b))

    elif x=="multiply":
        print(multiply(a,b))

    elif x=="divide":
        print(divide(a,b))
    
    else:
        print("you have given wrong value")

if __name__ == "__main__":
    calculator()