# Take a list, say for example this one:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list
# that are less than 5.
#
# Extras:
#
# 1. Instead of printing the elements one by one, make a new
# list that has all the elements less than 5 from this list
# in it and print out this new list.
# 2. Write this in one line of Python.
# 3. Ask the user for a number and return a list that contains
# only elements from the original list a that are smaller than
# that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for value in a:
    if value <= 5:
        print(value)

b = []
for value in a:
    if value <= 5:
        b.append(value)

print("New list:")
print(b)

c = []

while True:
    try:
        evaluateElement = int(input("Enter a number"))
        for value in a:
            if value <= evaluateElement:
                c.append(value)
        print(c)
        break
    except ValueError:
        print("Error! Element is not a number")

print("One line solution")
print([new_list_element for new_list_element in a if new_list_element < 5])

