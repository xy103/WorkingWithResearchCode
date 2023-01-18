# from https://realpython.com/python-refactoring/

# Compares x to y and prints relationship
x = 5
value = input("Enter a number: ")
y = int(value)
if x < y:
    print(f"{x} is less than {y}")
elif x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{x} is more than {y}")