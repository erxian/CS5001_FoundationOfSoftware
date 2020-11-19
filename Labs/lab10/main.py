'''
Zengping Xu
CS 5001 Fall 2020

This program will enable a user to search their TV channels
for shows based on criteria of their choosing e.g. shows
starring a particular actor.
'''
from actor import Actor
from show import Show
from channel import Channel


def shows_starring(actor, channel):
    '''
    Function -- shows_starring:
        searching for shows starring a particular ​Actor​
        in all available channels
    Parameters:
        actor -- an Actor Object
        channel -- a list of Channel Object
    Returns:
        a shows list
    '''
    lst = []
    for chal in channel:
        lst += chal.get_shows_by_actor(actor)
    return lst


def get_channel_by_show(show, channel):
    '''
    Function -- get_channel_by_show
        Get channel information for a particular show
    Parameters:
        show -- a Show Object
        channel -- a list of Channel Object
    Returns:
        print all channel's information
    '''
    msg = ""
    for chal in channel:
        if show in chal.shows:
            msg += f"channel name: {chal.name}\n channel number: {chal.number}"
    print(f"The channel information of {show.title} is:\n", msg)


def get_shows_by_day(day, channel):
    '''
    Function -- get_shows_by_day
        Get all shows playing on a particular day across all channels.
    Parameters:
        day -- a string
        channel -- a list of Channel Object
    Returns:
        print all shows title
    '''
    msg = ""
    for chal in channel:
        if day in chal.days:
            show = chal.days.get(day)
            msg += f"{show.title}\n"
    print("All available shows in", day, "are:\n", msg)


def main():
    actor1 = Actor("Actor", "1")
    actor2 = Actor("Actor", "2")
    actor3 = Actor("Actor", "3")
    show1 = Show("Monday Show", [actor1, actor2])
    show2 = Show("Tuesday Show", [actor1, actor2, actor3])
    show3 = Show("Friday Show", [actor2, actor3])
    show4 = Show("Jimmy Show", [actor1, actor3])
    channel11 = Channel("DEF", 42, [show1], {"Monday": show1})
    channel12 = Channel("XYZ", 31, [show2, show3], {"Tuesday": show2, "Friday": show3})
    channel13 = Channel("ABC", 53, [show4], {"Friday": show4})

    channel = [channel11, channel12, channel13]

    # searching for shows starring a particular ​Actor​
    # in all available channels
    total_shows = shows_starring(actor1, channel)
    print("The total shows of", actor1.first_name + actor1.last_name, "is:")
    for show in total_shows:
        print(show.title)
    print("\n")

    # Get channel information for a particular show
    get_channel_by_show(show2, channel)
    print("\n")

    # Get all shows playing on a particular day across all channels.
    get_shows_by_day("Friday", channel)


if __name__ == "__main__":
    main()
