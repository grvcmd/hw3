# Lab 11.27
"""This program will store roster and rating information for a soccer team.
    Coaches rate players during tryouts to ensure a balanced team."""

# jersey number: key
# player rating: value
player_dict = {}
sorted_list_keys = [] # sorted list to store the jersey numbers

# function to sort dictionary keys
def sortDictKeys():
    # sort the dictionary keys and then store them into
    # a list, then return that list
    sorted_list_keys = sorted(player_dict.keys())
    return sorted_list_keys