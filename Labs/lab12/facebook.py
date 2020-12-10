'''
Zengping Xu
CS 5002 Fall 2020

This program will ask the user which dwarf is logging in
(no password required), and then print a menu with options
prints friends, remove friends and add friends.
'''

valid_user = ["Happy", "Dopey", "Bashful", "Sneezy", "Sleepy", "Doc", "Grumpy"]
valid_choice = ["P", "U", "F"]
QUIT = "Q"
file_path = "dwarves.txt"

def read_file():
    '''
    Function -- read_file
        Reads a file one line at a time using "with". Store each
        line in a dictionary, first name is the key, other names
        are value. other names will be stored in a list
    Parameters: no parameters
    Returns:
        The contents of the file (a dictionary)
    '''
    network = {}
    # Opens the file and assigns it to the variable called file
    try:
        with open(file_path, "r") as file:
            # The following is the line by line option but the others work too
            for line in file:
                line_s = line.strip("\n").split(" ")
                network[line_s[0]] = line_s[1:]
    except FileNotFoundError:
        print("File not found")
    # The file is automatically closed when using "with"
    return network


def get_friend(user):
    '''
    Function -- get_friend
        get user's all friends
    Parameters:
        user -- login user
    Returns:
        a string, represent the friends
    '''
    network = read_file()
    friends = ", ".join(network.get(user))
    return friends


def write_file(network):
    '''
    Function -- write_file
        update content to file
    Parameters:
        network -- a dictionary, contains all dwarves
        name and its friends
    No Returns
    '''
    lines = []
    for user in valid_user:
        line = user + " " + " ".join(network.get(user))
        lines.append(line)
    # Opens the file and assigns it to the variable called file
    with open(file_path, "w") as file:
        # The following is the line by line option but the others work too
        for line in lines:
            file.write(line + "\n")
    # The file is automatically closed when using "with"


def unfriend(user, fname):
    '''
    Function -- unfriend
        remove a friend of dwarf
    Parameters:
        user -- the dwarf
        fname -- the friend of dwarf
    Returns:
        0 -- if the remove one if not dwarf's friend
        1 -- remove successfully
        2 -- if the dwarf has no friends
    '''
    network = read_file()
    friends = network.get(user)
    if len(friends) == 0:
        return 2
    if fname not in friends:
        return 0
    # do remove
    friends.remove(fname)
    network[user] = friends
    write_file(network)
    return 1


def add_friend(user, fname):
    '''
    Function -- add_friend
        add a friend to dwarf
    Parameters:
        user -- the dwarf
        fname -- the new friend of dwarf
    Returns:
        0 -- the new one is already dwarf's friend
        1 -- add successfully
    '''
    network = read_file()
    friends = network.get(user)
    if fname in friends:
        return 0
    friends.append(fname)
    network[user] = friends
    write_file(network)
    return 1


def main():
    user = input("Which of the 7 dwarves is logging in? ")
    while user not in valid_user:
        user = input("Which of the 7 dwarves is logging in? ")
    msg = "Choose from one of the options below:\n" + \
        "P: Print your friends list\n" + \
        "U <name>: Unfriend someone\n" + \
        "F <name>: Friend someone\n" + \
        "Q: Quit\n"
    user_in = input(msg)
    while user_in != QUIT:
        choice = user_in.split(" ")
        if choice[0] not in valid_choice:
            user_in = input(msg)
        else:
            if choice[0] == "P":
                # print users friends
                print("Your friends: ", get_friend(user))
            if choice[0] == "U":
                # unfriend someone
                if choice[1] not in valid_user:
                    print("Dwarf %s not existing" % choice[1])
                else:
                    result = unfriend(user, choice[1])
                    if result == 1:
                        print("%s has been unfriended." % choice[1])
                    if result == 0:
                        print("%s is not your friend." % choice[1])
                    if result == 2:
                        print("%s not having any friends." % user)
                
            if choice[0] == "F":
                if choice[1] not in valid_user:
                    print("Dwarf %s not existing" % choice[1])
                else:
                    # friend someone
                    result = add_friend(user, choice[1])
                    if result == 1:
                        print("%s is your friend now." % choice[1])
                    if result == 0:
                        print("%s has already been your friend." % choice[1])
            user_in = input(msg)


if __name__ == "__main__":
    main()
