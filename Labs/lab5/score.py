'''
Zengping Xu
CS 5001 Fall 2020

This program will calculate the average, median, lowest
and highest score of a class.
'''


def is_empty(all_scores):
    '''
    Function -- is_empty
        Checks if a list is empty.
    Parameter:
        lst -- A list.
    Returns:
        True if the list contains 0 items, False otherwise.
    '''
    return len(all_scores) == 0


def get_max(all_scores):
    '''
    Function -- get_max
        get the maxmum score of all scores
    Parameters:
        all_scores --  the list of scores
    Return a float, which is the maxmum score
    '''
    if is_empty(all_scores):
        return 0

    all_scores.sort()
    max_score = all_scores[-1]
    return max_score


def get_min(all_scores):
    '''
    Function -- get_min
        get the minimum score of all scores
    Parameters:
        all_scores --  the list of scores
    Return a float, which is the minimum score
    '''
    if is_empty(all_scores):
        return 0
        
    all_scores.sort()
    min_score = all_scores[0]
    return min_score


def get_median(all_scores):
    '''
    Function -- get_median
        get the median score of all scores
    Parameters:
        all_scores --  the list of scores
    Return a float, which is the median score
    '''
    if is_empty(all_scores):
        return 0
    
    all_scores.sort()
    if len(all_scores) % 2 == 1:
        i = int(len(all_scores) / 2)
        median_score = all_scores[i]
    else:
        i = int((len(all_scores) - 1) / 2)
        median_score = (all_scores[i] + all_scores[i+1]) / 2
    return median_score
    

def get_average(all_scores):
    '''
    Function -- get_average
        get the average score of all scores
    Parameters:
        all_scores --  the list of scores
    Return a float, which is the average score
    '''
    if is_empty(all_scores):
        return 0
    
    sum = 0
    for score in all_scores:
        sum = sum + score

    average_score = sum / len(all_scores)
    return average_score


def main():
    all_scores = []
    stop_sign = "q"
    user_input = input("Enter a score or 'q' to quit: ")
    while user_input != stop_sign:
        score = float(user_input)
        all_scores.append(score)
        user_input = input("Enter a score or 'q' to quit: ")
    
    get_min(all_scores)
    get_max(all_scores)
    get_median(all_scores)
    get_average(all_scores)


if __name__ == "__main__":
    main()
