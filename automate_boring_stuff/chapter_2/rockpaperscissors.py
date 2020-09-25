# Write your code here :-)
import random, sys

def main():
    wins = 0
    losses = 0
    ties = 0
    answer = ''
    print("ROCK, PAPER, SCISSORS")
    while True:
        print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
        print ("Enter your move: (r)ock (p)aper (s)cissors of (q)uit")
        choice = input().lower()
        if choice == 'q':
            break
        computerChoice = random.choice('rps')
        print('%s versus...' % (letterValue(choice).upper()))
        print(letterValue(computerChoice))
        if (choice == computerChoice):
            ties+=1
            print("It is a tie!")
        if (choice == 'p'):
            if (computerChoice == 's'):
                print("You lose!")
                losses += 1
            elif (computerChoice == 'r'):
                print("You win!")
                wins += 1
        if (choice == 'r'):
            if (computerChoice == 'p'):
                print("You lose!")
                losses += 1
            elif (computerChoice == 's'):
                print("You win!")
                wins += 1
        if (choice == 's'):
            if (computerChoice == 'r'):
                print("You lose!")
                losses += 1
            elif (computerChoice == 'p'):
                print("You win!")
                wins += 1
    print("Finished")

def letterValue(ans):
    choices = {
        'p' : 'PAPER',
        'r' : 'ROCK',
        's' : 'SCISSORS'
    }
    return choices[ans]

if __name__ == '__main__':
    main()