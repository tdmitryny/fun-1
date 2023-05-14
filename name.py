def divide(n1,n2):
    return n1 / n2

def multiply(n1,n2):
    return n1 * n2

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What is first number? "))
num2 = int(input("What is second number? "))
for oper in operation:
    print(oper)



choose = input("What operation do you want to use above? ")


plus = operation[choose]
answer = plus(num1,num2)

print(f"{num1}{choose}{num2} = {answer}")

