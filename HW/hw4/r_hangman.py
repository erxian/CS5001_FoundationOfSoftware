# -*- coding: utf-8 -*
'''
Zengping Xu
CS 5001 Fall 2020

This program implements a version of the game ​Hangman​,
the players attempts to guess a secret word one letter at a time,
and play three rounds against the computer
'''



def letter_in_word(letter, secret_word):
    '''
    '''
    if letter in secret_word:
        return True
    else:
        return False


def compare_word(answer, secret_word):
    '''
    Function -- compare_word
        check the answer with secret_word, if same return True,
        if not return False
    Parameters:
        answer --  the input answer from user
        secret_word -- the secret word waits to guess
    Returns:
        a boolean, reprent the compare result
    '''
    if answer == secret_word:
        return True
    else:
        return False

def main():
    # 3 rounds - each word has a secret word
    # FOR EACH ROUND:
    # print secret word woth each letter replaced with _
    # IF GUESSES REMAINING
        # prompt to enter letter or word
        # if a single letter
        # check if in secret word
        # if already guessed
        # print message

    # user enter something
    # check the enter is a letter or word
    # if it is a word
        # call compare_word
    # if it is a letter
        # call letter_in_word
        # if letter in word
            # return True
        # secret_word.index(letter)
        # print message
    
    # loop
    # user enter something
    # check the enter is a letter or word
    # if it is a word
        # call compare_word
    # if it is a letter
        # check if it guessed before
        # call letter_in_word
        # ...


if __name__ == "__main__":
    main()
