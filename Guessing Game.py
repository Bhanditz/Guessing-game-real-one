import random
import sys

def main():

    print('Think of a number from 1-100.')
    computer = random.randint(0,101)
    new_list = [i for i in range(0,101)]
    validate = input("Is your number %d? (y/n)" % computer)
    computerTrys = 1
    
    while validate == 'n':
        computerTrys += 1
        high_low = input('Was the number high or low? ')
        if high_low == ('high'):
            guess_list = [i for i in range(computer,101)]
            for i in guess_list:
                if i in new_list:
                    new_list.remove(i)
            computer = random.choice(new_list)
            validate = input("Is your number %d? (y/n)" % computer)
        if high_low == ('low'):
            guess_list = [i for i in range(0,computer + 1)]
            for i in guess_list:
                if i in new_list:
                    new_list.remove(i)
            computer = random.choice(new_list)
            validate = input("Is your number %d? (y/n)" % computer)

    if validate == 'y':
        print('Ez Pz only took me',computerTrys,' times.')
                     
        
main()
