# -*- coding: utf-8 -*
'''
Zengping Xu
CS 5001 Fall 2020

This program implements a version of the game ​Hangman​,
the players attempts to guess a secret word one letter at a time,
and play three rounds against the computer
'''


SECRETE_WORDS = ("APPLE", "OBVIOUS", "XYLOPHONE")


def letter_in_word(letter, secret_word):
    '''
    Function -- letter_in _word
        check if the letter is in secret_word
    Parameters:
        letter -- the input lettr from user
        secret_word -- the secret word waits to guess
    Returns:
        a boolean, True means letter in secret_word,
        False means letter not in secret_word
    '''
    if letter in secret_word:
        return True
    else:
        return False


def compare_word(word, secret_word):
    '''
    Function -- compare_word
        check if the word is secret_word, yes return True,
        no return False
    Parameters:
        word --  the input word from user
        secret_word -- the secret word waits to guess
    Returns:
        a boolean, True means word is secret_word, False
        means it's not
    '''
    if word == secret_word:
        return True
    else:
        return False


def already_guessed(letter, guessed):
    '''
    Function -- already_guessed
        check if the letter has already been guessed
    Parameters:
        letter -- the input lettr from user
        guessed -- the already guessed letters
    Returns:
        a boolean, True means letter has been guessed before,
        False means letter has not been guessed yet
    '''
    if letter in guessed:
        return True
    else:
        return False


def main():
    win_time = 0
    for secret_word in SECRETE_WORDS:
        guessed = ""
        all_pos = []
        win = False
        max_turn = 6
        turn = 1
        while turn <= max_turn:
            msg = input("Enter a letter or word: ").upper()
            letter_length = 1
            # if msg is a word, compare it with secret_word
            if len(msg) > letter_length:
                is_word = compare_word(msg, secret_word)
                if is_word:
                    win = True
                    break
            # if msg is a letter, check if it is in secret_word
            if len(msg) == letter_length:
                # make sure if the letter has already been guessed
                is_guessed = already_guessed(msg, guessed)
                if is_guessed:
                    print("You've already guessed that letter!")
                else:
                    guessed += msg
                    is_letter = letter_in_word(msg, secret_word)
                    if is_letter:
                        # if letter in secret_word, find all the
                        # positions where the letter locates
                        for i, item in enumerate(secret_word):
                            if msg == item:
                                all_pos.append(i)
                    turn += 1

            output = []
            # the output will display all correctly guessed letters
            # and hide all non-guessed letters with "_"
            for i in range(len(secret_word)):
                if i in all_pos:
                    output.append(secret_word[i])
                else:
                    output.append("_")    
            print("".join(output))   
            print("Your guesses so far:", guessed)

        if win:
            print("You win!")
            win_time += 1
        else:
            print("You lose! The word was", secret_word)

    print("You won %d out of 3" % win_time)


if __name__ == "__main__":
    main()
