class Channel:
    '''
    Class -- Channel
        represent the TV Channel
    Attributes:
        name -- a string, the name of the channel
        number -- an integer, the number of the channel
        shows -- a list, contains Show Object
        days -- a dict, represent the shows are playing
        on a particular day
    Methods:
        get_shows_by_actor -- iterates through each ​Show​
        object in the ​Channel​’s show list. If the ​Show​’s cast
        list contains the Actor​, the ​Show​ is added to the list
        to be returned.
    '''
    def __init__(self, name, number, shows, days):
        self.name = name
        self.number = number
        self.shows = shows
        self.days = days

    def get_shows_by_actor(self, actor):
        '''
        Function -- get_shows_by_actor
            iterates through each ​Show​
            object in the ​Channel​’s show list. If the ​Show​’s cast
            list contains the Actor​, the ​Show​ is added to the list
            to be returned.
        Parameters:
            actor -- an Actor Object
        Returns:
            a list, contains the shows list has the Actor
        '''
        self.show_lst = []
        for show in self.shows:
            if show.cast_contains(actor):
                self.show_lst.append(show)
        return self.show_lst


