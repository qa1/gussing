#this just a game
import random
print 'Well can you guess my number? It is between 1 and 20. Enter a number now!'
def game():
	compGuesses = random.randint(1,20)
	print "Guse a number"
	userGuesses =input()
	while userGuesses != compGuesses:
             print 'Nope! Try again!'
             if userGuesses > compGuesses:
                 print "your number is bigger than true."
             if userGuesses < compGuesses:
                 print "your number is smaller than true."
             userGuesses = input()
	if  userGuesses == compGuesses:
             print 'Yay you guest it correctly'
             print "Would you like to play again? Type 'yes' or 'no'"
             answer = raw_input()
             if answer == 'yes':
              game()
             elif answer == 'no':
              print 'Bye!'
             else:
              print "That is not 'yes' or 'no! Just forget it!'"
              game()
game()
