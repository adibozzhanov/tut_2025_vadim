"""
You and your friend are in a jail and you need to break out.
The warden will let you free if you solve his puzzle.

Consider having a chessboard with a coin on every square.
Each coin is either heads or tails.
Under one of the squares there is a key hidden.

These are the rules of the puzzle:

- You will enter the room with a chessboard.
  * coins will be arranged in a random configuration
  * You can see where the key is hidden
  * You have to flip ONE COIN

You then leave the room and your friend enters
  * He will have to guess where the key is first try

Come up with a strategy that guarantees success. (complete the functions below)

All functions must be pure without any shared state
"""

def initial_chessboard_and_key():
    # generate the initial chessboard configuration 
    chessboard = [1,1,1,1] # CHANGE
    key = 3 # CHANGE
    return chessboard, key

def person_1(chessboard_config, key):
    # take in a chessboard (up to you how to represent it)
    # and a key position (also up to you how to represent it)
    # spit out the updated chessboard after a flip
    return chessboard_config

def person_2(chessboard_config):
    # take in a chessboard and guess where the key is
    key = 3
    return key



chessboard, key = initial_chessboard_and_key() # this should do it randomly

after_flip = person_1(chessboard, key)

guess = person_2(after_flip)

assert guess == key






