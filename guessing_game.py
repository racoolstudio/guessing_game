from os import name, system
from unittest import result


def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')

   # for mac and linux
   else:
     _ = system('clear')
GUESSED_NUMBER = 17

def level(level):
    if level == 'easy':
        return 10
    else:
        return 5    
    
def pick (number):
    endGame = False
    if number == GUESSED_NUMBER:
        endGame = True
        print('You are Smart! You got it')
    elif number > (GUESSED_NUMBER ) :
        print('Too high ! You are smarter than that lol 🤣')
    elif  number < GUESSED_NUMBER:
        print('Too Lowww!!!! Try again')
    return endGame    
def guessGame() :
    levels = input('Choose your level\n Enter "easy" for easy level or "hard" for Hard level \n : ').lower()
    attempts = level(levels)
    while attempts != 0 :
        number=int(input('Guess The number from 1-100\n : '))
        endGame = pick(number)
        attempts -=1
        if endGame:
            return
        if not endGame  :
            print(f'You have {attempts} attempt(s) left !!!')
        if attempts <0 :
            clear()
            print('Sorry you lose !!! Try again')
            main()
             
def main () :
    print('Welcome to Guessing Game !!!')        
    guessGame()
main()    
