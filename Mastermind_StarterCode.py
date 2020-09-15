import pygame
import tkinter
import random

##----------------------------------------------------------------------------##

class MastermindGame:
    def __init__(self):
        self.code_length = 4
        self.possible_nums = 6
        self.code = (0,)
        self.code_digit_count = None
        self.previous_guesses = list()


    ## Generate a random code for self.code
    ## len(code) == "length"
    ## Should include numbers between 0 and "possibilities"
    ## Ex. If "possibilities" = 3 then the code only has the numbers (0, 1, 2)
    def generate_code(self):
        length = self.code_length
        possibilities = self.possible_nums

        ## TODO: Generate a random code
        ## HINT: https://www.w3schools.com/python/ref_random_randint.asp
        ## How should we save the code?

        self.code = (0,0,0,0)

##----------------------------------------------------------------------------##

    ## Count how many times a number appears in the code
    def count_digits(self, code):
        digit_count = None

        ## TODO: Counting can't be that hard!
        ## What data type should digit_count be?

        return digit_count

##----------------------------------------------------------------------------##
    
    ## Compare the guess to the code
    ## Return how many numbers are correct and how many numbers are in the correct position.
    ## Ex. code = 1324 and guess = 1111
    ## correct_nums      should = 1
    ## correct_positions should = 1
    def check_guess(self, guess):
        code = self.code
        
        correct_nums = 0
        correct_positions = 0

        ## TODO: We want to check how correct the guess is
        ## HINT: Why did we write count_digits()?

        return correct_nums, correct_positions

##----------------------------------------------------------------------------##

    ## Prints out the last 5 guesses and correctness values all pretty
    ## Ex.
    ##    Guess      Num  Pos
    ## [ 0 1 2 3 ] |  1    0
    ## [ 0 1 4 4 ] |  1    1
    ## [ 1 1 4 4 ] |  2    2
    ## [ 1 5 4 5 ] |  4    3
    ## [ 1 5 5 3 ] |  3    3
    ## 
    ## Enter your guess: 
    def pretty_print(self):
        ## OPTIONAL TODO: Can look however you want
        pass

##----------------------------------------------------------------------------##

    ## Check if the input guess is the correct length
    ## Check if the input guess is a number
    ## Check if the input guess only has possible value
    def is_valid_guess(self, string_guess):

        ## TODO: Check guess to make sure it doesn't break your program
        ## HINT: https://www.w3schools.com/python/python_ref_string.asp
        ## HINT: Guess is a string, how do we know it only has numbers?

        return False

##----------------------------------------------------------------------------##

    ## Ask the player for a guess and get the guess
    ## Check if the guess is valid and ask again if it is not.
    def get_guess(self):
        guess = (0,)

        ## TODO: Read input, check if valid, repeat  until valid.
        ## HINT: https://www.w3schools.com/python/ref_func_input.asp
        
        ## print('Enter your guess: ')
        ## print('Please enter a valid guess: Ex \'0123\'')

        return guess

##----------------------------------------------------------------------------##

    ## Starts the game
    ## code_length specifies how long the code is
    ## possible_nums specifies how many choices each digit has
    def start(self, code_length=4, possible_nums=6):
        self.code_length = code_length
        self.possible_nums = possible_nums

        ## Determines the number of guesses you get, you can change this to give
        ## yourself more or less guesses if you want.
        max_guesses = int(code_length * possible_nums // 1.6)

        print('The code is {0} digits from 0 - {1}. You have {2} guesses'.format(code_length, possible_nums - 1, max_guesses))
        
        ## TODO
        ## print('{0} has {1} correct numbers and {2} numbers in the correct position.'.format(guess, correct_nums, correct_positions)) 

        print('Darn, you ran out of guesses!')
        print('The code was {0}'.format(self.code))

##----------------------------------------------------------------------------##

## IGNORE THIS FUNCTION
## This function will test your code to make sure it is correct.
def test():
    game = MastermindGame()

    game.possible_nums = 6
    for i in range(1, 10):
        game.code_length = i
        for _ in range(0, 3):
            game.generate_code()
            if len(game.code) != i:
                print('generate_code() failed: expected length was {0} but got {1} with length {2}'.format(i, game.code, len(game.code)))

    for i in range(1, 11):
        game.possible_nums = i
        game.generate_code()
        for digit in game.code:
            if digit < 0 or digit >= i:
                print('generate_code() failed: allowed values were {0} but got code {1} with invalid digit {2}'.format(list(range(0, i)), game.code, digit))

    print('Done testing generate_code()')

    game.code_length = 4
    test_codes = [(0,0,0,0), (1,2,4,5), (9,3,6,5), (2,1,2,0), (4,5,5,4)]
    possible_nums = [3, 6, 10, 3, 6]
    answers = [[4,0,0], [0,1,1,0,1,1], [0,0,0,1,0,1,1,0,0,1], [1,1,2], [0,0,0,0,2,2]]

    for code, pos, ans in zip(test_codes, possible_nums, answers):
        game.possible_nums = pos
        counts = game.count_digits(code)

        if type(counts) == list or type(counts) == tuple:
            if len(counts) != len(ans):
                print('count_digits() failed: Expected {0} but received {1}'.format(ans, counts))
            else:
                for i, j in zip(counts, ans):
                    if i != j:
                        print('count_digits() failed: Expected {0} but received {1}'.format(ans, counts))

        elif type(counts) == dict:
            for i, count in enumerate(ans):
                if i in counts:
                    if counts[i] != count:
                        temp = dict()
                        for i, a in enumerate(ans):
                            temp[i] = a
                        print('count_digits() failed: Expected {0} but received {1}'.format(temp, counts))
                else:
                    temp = dict()
                    for i, a in enumerate(ans):
                        temp[i] = a
                    print('count_digits() failed: Expected {0} but received {1}'.format(temp, counts))
        else:
            print("count_digits(): unexpected type, cannot test")

    print('Done testing count_digits()')

    guess = (0,1,4,4)
    test_codes = [(0,0,0,0), (1,2,4,5), (9,3,6,5), (2,1,2,0), (4,5,5,4), (0,1,4,4)]
    possible_nums = [6, 6, 10, 6, 6, 6]
    answers = [(1,1), (2,1), (0,0), (2,1), (2,1), (4,4)]
    
    for code, pos, ans in zip(test_codes, possible_nums, answers):
        game.code = code
        game.possible_nums = pos
        game.code_digit_count = game.count_digits(code)

        if ans != game.check_guess(guess):
            print('check_guess() failed: Code {0} and Guess {1} should have returned {2}, not {3}'.format(code, guess, ans, game.check_guess(guess)))

    print('Done testing check_guess()')

##----------------------------------------------------------------------------##

if __name__ == "__main__":
##    test()
    game = MastermindGame()
    game.start()
