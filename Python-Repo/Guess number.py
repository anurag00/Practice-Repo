#Guess the number game
import random

print('Hello, what is your name?')
name = input()
print('Well.. '+name+', I am thinking of a number between 1 and 20')
secNo = random.randint(1,20)

for guessNo in range(1,7):
    print('Take a guess (' + str( 7 - guessNo ) + ' guesse(s) left)')
    guess = int(input())

    if guess < secNo:
        print('Too low... ')
    elif guess > secNo:
        print('Too high... ')
    else:
        break

if guess == secNo:
    print('You took '+ str(guessNo) + ' guesses to get the answer.\nGood Job')
else:
    print('Aww... you coudnt guess the number ' + str(secNo) + ' before finishing you lives ' + name + '.\nBetter luck next time :)')

#end
