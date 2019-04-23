"""
Rock Paper Scissors Game

Learning Goal:
    * Thinking through control flow logic - if/elif/else, while

Practiced Concepts:
    * Software design + iterative dev
    * Variables (strings, ints, lists)
    * Libraries
"""

##### Start with brainstorm of RPS game elements
# Computer play
# Human play + who won
# Complexity of game options from text through hand recognition, etc.


###### Print out a string representing the computer's play - vars, type

play = 'rock'
print play


###### We have three plays to choose from - lists, indexing

# Create a list of our play choices
plays = ['rock', 'paper', 'scissors']

# Review: How do we access the choices?
print plays[0]


###### Start with basic strat, choose random play - libraries

import random

plays = ['rock', 'paper', 'scissors']

# Use randint rather than choice to practice index concept
play = random.choice(plays)
print play


###### Let the human play and report who wins - if/elif/else, while

import random

plays = ['rock', 'paper', 'scissors']

playing = True
while playing: # Add after single run test
    # Get plays
    computer_play = random.choice(plays)
    human_play = raw_input('Enter rock, paper, scissors, or quit: ')

    print 'Computer played ' + computer_play

    # Few total options, so go long route as nested if logic practice
    # Tie
    if human_play == computer_play:
        print 'You Tied!'
    # Win or lose
    elif human_play == 'rock':
        if computer_play == 'paper':
            print 'Computer won!'
        else:
            print 'You won!'
    elif human_play == 'paper':
        if computer_play == 'scissors':
            print 'Computer won!'
        else:
            print 'You won!'
    elif human_play == 'scissors':
        if computer_play == 'rock':
            print 'Computer won!'
        else:
            print 'You won!'
    # Quit the game
    elif human_play == 'quit':
        playing = False
    # Human entered something we can't play with
    else: # Add after showing the error case of bad input
        print 'Uh oh. You need to enter rock, paper, or scissors.  Try again!'