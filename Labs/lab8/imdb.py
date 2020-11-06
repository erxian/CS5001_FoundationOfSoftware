'''
xxx xxx xxx 
CS 5001 Fall 2020

This program get inputs from user about a imdb labelled file,
and find the negative review and positive review according to
its lable, then write them to new separated txt file, finally
display the selected reviews on the basis of user inputs.
'''


PATH = "imdb_labelled.txt"
NEGATIVE_PATH = "negative.txt"
NEGATIVE_LABLE = "0"
POSITIVE_PATH = "positive.txt"
POSITIVE_LABLE = "1"
MIN = 1
MAX = 500


def file_validator(user_in):
    '''
    '''
    parts = user_in.split(".")
    head = parts[0].split("_")
    if len(parts) != 2 or parts[1] != "txt" or len(head) != 2:
        raise FileNotFoundError
    if user_in != PATH:
        raise ValueError


def write_file(file_path):
    '''
    '''
    with open(file_path, "r") as imdb:
        lines = imdb.readlines()

    with open(POSITIVE_PATH, "w") as positive:
        for line in lines:
            if "\n" in line:
                line = line.strip()
            if line[-1] == POSITIVE_LABLE:
                line = line[:-4] + "\n"
                positive.write(line)

    with open(NEGATIVE_PATH, "w") as negative:
        for line in lines:
            if "\n" in line:
                line = line.strip()
            if line[-1] == NEGATIVE_LABLE:
                line = line[:-4] + "\n"
                negative.write(line)


def find_lines(index):
    '''
    '''
    try:
        parts = index.split(" ")
        char = parts[0]
        num = int(parts[1])
        if num < MIN or num > MAX:
            raise Exception
    except ValueError:
        return "review index must be an integer"
    except:
        return "review index out of range(1-500)"

    if char == "n":
        with open("negative.txt", "r") as negative:
            lines = negative.readlines()    
    if char == "p":
        with open("positive.txt", "r") as positive:
            lines = positive.readlines()
    return (lines[num -1])


def main():
    # PROMPT = "Enter the path to the IMDB dataset:\n"
    msg = "Enter a 'n' or 'p' and its index(or 'q' to quit): "
    QUIT = "q"
    # user_in = input(PROMPT)
    # while user_in != PATH:
    #     try:
    #         file_validator(user_in)   
    #     except FileNotFoundError:
    #         print("File not found")
    #     except:
    #         print("Error processing the file.")
    #     user_in = input(PROMPT)
    # write_file(user_in)

    index = input(msg)
    while index != QUIT:
        print(find_lines(index))
        index = input(msg)


if __name__ == "__main__":
    main()
