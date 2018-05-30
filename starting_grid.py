"""
This function will be used to determine the order of the starting grid.  There
will be the option to use multiple methods including but not limited to: random,
single lap shakdown, and multiple lap shakedown, and multiple session shakedown.
"""
import random as rnd

def random_rank(racer_names):
    """
    :racer_names: a list of strings
    :start_order: a dict with start order as keys
    """

    # create a list of possible start positions
    choice_list = [option for option in range(1, len(racer_names)+1)]

    # create start order dict with keys and default values
    start_order = {value: 0 for value in range(1,len(racer_names)+1)}

    # give each racer a starting position
    for name in racer_names:
        start = rnd.choice(choice_list)
        start_order[start] = name
        choice_list.drop(start)

    return start_order

def single_lap_shakedown(racer_names):
    pass

def multi_lap_shakedown(racer_names, lap_count):
    pass

def multi_session_shakedown(racer_names, session_count, lap_count):
    pass
