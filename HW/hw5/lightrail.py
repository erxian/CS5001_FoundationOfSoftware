'''
Zengping Xu
CS 5001 Fall 2020

This program contains the link stations form north (University of
Washington) to south (Angle Lake), and provides the ways to validate
stations, determine direction or get station numbers.
'''


LINK_STATIONS = ("University of Washington", "Capitol Hill", "Westlake",
                 "University Street", "Pioneer Square",
                 "International District/Chinatown", "Stadium", "SODO",
                 "Beacon Hill", "Mount Baker", "Columbia City", "Othello",
                 "Rainier Beach", "Tukwila International Boulevard",
                 "SeaTac/Airport", "Angle Lake")


def is_valid_station(station):
    '''
    Function -- is_valid_station
        Checks if a given string is a valid Seattle light rail station.
        Provided station must match a station name exactly. For example, "mount
        baker" would not be valid because the case doesn't match.
    Parameter:
        station -- The string to check
    Returns:
        True if a given string is a valid Seattle light rail station
        name, False otherwise.
    '''
    if station in LINK_STATIONS:
        return True
    else:
        return False


def get_station_index(start, end):
    '''
    Funtion -- get_station_index
        get station's index in LINK_STATIONS, for example the index of
        station "Capitol Hill" is 1. If either station is invalid or
        both station are same, the station index is 0.
    Parameters:
        start - The starting station name
        end - The ending station name.
    Returns:
        start_index, means start station's index
        end_index, means end station's index
    '''
    if start not in LINK_STATIONS or end not in LINK_STATIONS \
            or start == end:
        start_index = 0
        end_index = 0
        return start_index, end_index

    for pos, station in enumerate(LINK_STATIONS):
        if station == start:
            start_index = pos
        if station == end:
            end_index = pos
    return start_index, end_index


def get_direction(start, end):
    '''
        Function -- get_direction
            Given start and end station names, determines if the direction is
            Northbound or Southbound.
        Parameters:
            start - The starting station name
            end - The ending station name.
        Returns:
            "Northbound" if the end station is north of the start station, or
            "Southbound" if the end station is south of the start station. If
            either station is invalid, or start and end stations are the same,
            return "No destination found".
    '''
    start_index, end_index = get_station_index(start, end)
    if start_index == end_index:
        direction = "No destination found"
    elif end_index > start_index:
        direction = "Southbound"
    else:
        direction = "Northbound"
    return direction


def get_num_stops(start, end):
    '''
        Function -- get_num_stops
            Calculates the number of stops from start to end.
        Parameters:
            start - The starting station name
            end - The ending station name.
        Returns:
            The number of stops from start to end. If either station is invalid
            or both stations are the same, return 0.
    '''
    start_index, end_index = get_station_index(start, end)
    if start_index == end_index:
        stops_num = 0
    elif start_index > end_index:
        stops_num = start_index - end_index
    else:
        stops_num = end_index - start_index
    return stops_num
