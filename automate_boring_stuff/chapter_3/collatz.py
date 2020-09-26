# Collatz program

def collatz(number):
    if number <= 0:
         return 0
    while (number > 1):
        if number % 2 == 0:
            number = int(number / 2)
        else:
            number = number * 3 + 1
        print(number)

print("Enter number:")
answer = input()
collatz(int(answer))