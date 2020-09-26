# Collatz program

def collatz(number):
    try:
        number = int(number)
        if number <= 0:
            print(0)
        while (number > 1):
            if number % 2 == 0:
                number = int(number / 2)
            else:
                number = number * 3 + 1
            print(number)
        return True
    except ValueError:
        print("Invalid input")
        return False

finished = False
while (not finished):
    print("Enter number:")
    answer = input()
    finished = collatz(answer)