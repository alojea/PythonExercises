# Ask the user for a number.
# Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
#
# extras:
# 1. If the number is a multiple of 4, print out a different message.
# 2. Ask the user for two numbers: one number to check (call it num)
# and one number to divide by (check). If check divides evenly into num,
# tell that to the user. If not, print a different appropriate message.

def checkOddOrEven( numb ):
    """Function for calculate if the number are even or odd"""
    if numb % 4 == 0:
        print(str(numb) + " is divisible by 4")
    elif numb % 4 == 0:
        print(str(numb) + " is even")
    else:
        print(str(numb) + " is odd")

while True:
     try:
        num = int(input("Enter one number \n"))
        check = int(input("Enter second number \n"))
        break
     except ValueError:
        print("Error! Insert a numeric value")

print("Results:")
checkOddOrEven(num)

if num % check == 0:
    print(str(num) + " and " + str(check) + " are divisible")
else:
    print(str(num) + " and " + str(check) + " are not divisible")



