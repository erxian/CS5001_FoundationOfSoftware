class Show:
    '''
    Class -- Show
        represent an TV show
    Attributes:
        title -- a string, the name of the show
        cast_mem -- a list, the cast members in the show
    Methods:
        cast_contains -- takes an ​Actor​ object as a parameter
        and returns ​True​ if that ​Actor​ is in the ​Show​’s cast
        list and ​False otherwise
    '''
    def __init__(self, title, cast_mem):
        self.title = title
        self.actors = cast_mem
    
    def cast_contains(self, actor):
        '''
        Function -- cast_contains:
            cast_contains -- takes an ​Actor​ object as a parameter
            and returns ​True​ if that ​Actor​ is in the ​Show​’s cast
            list and ​False otherwise
        Parameters:
            actor -- an Actor Object
        Retruns:
            True​ if that ​Actor​ is in the ​Show​’s cast
            list and ​False otherwise
        '''
        if actor in self.actors:
            return True
        else:
            return False

