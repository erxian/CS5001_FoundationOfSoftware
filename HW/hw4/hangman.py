# -*- coding: utf-8 -*
'''
Zengping Xu
CS 5001 Fall 2020

This program implements a version of the game ​Hangman​,
the players attempts to guess a secret word one letter at a time,
and play three rounds against the computer
'''


all_secret_word = ["APPLE", "OBVIOUS", "XYLOPHONE"]


def compare_letter(letter, secret_word):
    '''
    Function -- compare_letter
        check the input letter with secret_word, if the letter in
        secret_word, remain the letter, if not, fill with "_". For
        example, letter = "A", secret_word = ['A', 'P', 'P', 'L', 'E']
        then the result should be ['A', '_', '_', '_', '_']
    Parameters:
        letter --  the input letter from player
        secret_word -- the secret word waits to guess
    Returns:
        a list, represent the compare result.
    '''
    result = []
    secret_word = list(secret_word)
    for each_letter in secret_word:
        if each_letter == letter:
            result.append(each_letter)
        else:
            result.append("_")
    return result


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


def combine(result, total_result):
    '''
    Function -- combine
        combine exists answer with new input answer. For example,
        exists answer is ['A', '_', '_', '_', '_'], and the new
        input answer is ['_', 'P', 'P', '_', '_'], then the
        combination of them is ['A', 'P', 'P', '_', '_']
    Parameters:
        result -- the new input answer
        total_result -- the exist answer
    Returns:
        a list, represents the lastest answer
    '''
    i = 0
    length = len(result)
    combine_result = []
    while i < length:
        if result[i].isalpha() is False and \
                total_result[i].isalpha() is False:
            combine_result.append('_')
        elif result[i].isalpha() is True:
            combine_result.append(result[i])
        elif total_result[i].isalpha() is True:
            combine_result.append(total_result[i])
        i += 1

    return combine_result


def initial(secret_word):
    '''
    Function -- initial
        initialize the answer's default value, for example,
        if the secret_word is "APPLE", the answer's default
        value should be "_____" with 5 "_"
    Parameters:
        secret_word -- the the secret word waits to guess
    Returns:
        a list, all element is "_"
    '''
    total_result = []
    length = len(secret_word)
    i = 0
    while i < length:
        i += 1
        total_result.append("_")
    return total_result


def main():
    max_turn = 6
    win_time = 0
    for secret_word in all_secret_word:
        total_result = initial(secret_word)
        print("".join(total_result))
        total_answer = ""
        turn = 1
        letter_length = 1
        win = False
        while turn <= max_turn:
            answer = input("Enter a letter or word: ")
            answer = answer.upper()
            length = len(answer)
            if length > letter_length:
                result = compare_word(answer, secret_word)
                if result:
                    win = True
                    break
            if length == letter_length:
                if answer in total_answer:
                    print("You've already guessed that letter!")
                else:
                    if turn == max_turn:
                        break
                    result = compare_letter(answer, secret_word)
                    total_result = combine(result, total_result)
                    total_answer = total_answer + answer
                    turn += 1
            print("".join(total_result))
            print("Your guesses so far:", total_answer)

        if win:
            print("You win!")
            win_time += 1
        else:
            print("You lose! The word was", secret_word)

    print("You won %d out of 3" % win_time)


if __name__ == "__main__":
    main()
