# Create a program that asks the user for a number and
# then prints out a list of all the divisors of that number.
# (If you don't know what a divisor is, it is a number that divides
# evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

def calculateDivisors(number):
    divisors = []
    possible_divisor = number
    while possible_divisor > 0:
        if(number % possible_divisor == 0):
            divisors.append(possible_divisor)
        possible_divisor = possible_divisor - 1
    if(possible_divisor is None):
        print(str(number) + " doesn't have any divisor")
    else:
        print("Divisors of " + str(number))
        print(divisors)


while True:
    try:
        evaluateElement = int(input("Enter a number"))
        calculateDivisors(evaluateElement)
        break
    except ValueError:
        print("Error! Element is not a number")