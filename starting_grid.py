"""
This function will be used to determine the order of the starting grid.  There
will be the option to use multiple methods including but not limited to: random,
single pole lap, and multiple pole lap.
"""
from random import randint

def random_rank(racer_names):
"""
    :racer_names: a list of strings
    :start_order: a dict with start order as keys
"""

# create a choice list
choice_list = [value for value in range(1,len(racer_names)+1)]
