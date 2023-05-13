



def number_check(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")


        



n = int(input("Check this number: "))
number_check(number=n)