import math_pi

while True:
    try:
        x = int(input('Please enter a number to search for in Pi(23072008 for 23-july-2008): '))
        break
    except ValueError:
        print('Oops! That\'s not a valid number! Try again!')

print('The first occurance of that number is in the', end=" ")
print('\033[1m', end=" ")
print(str(str(math_pi.pi(b = 1000000)).find(str(x))).replace('-1', 'iCouldntFindIt'), end=" ")
print('\033[0m', end=" ")
print('digit of Pi.')