# Lab 11.27
"""This program will store roster and rating information for a soccer team.
    Coaches rate players during tryouts to ensure a balanced team."""

# key: jersey number (0 - 99)
# value: player rating (1 - 9)
player_dict = {}
sorted_list_keys = []  # sorted list to store the jersey numbers


# function to sort dictionary keys
def sort_dict_keys():
    # sort the dictionary keys and then store them into
    # a list, then return that list
    sorted_list_keys = sorted(player_dict.keys())
    return sorted_list_keys


# Define the function output_roster().
def output_roster():

    # Call the sort_dict_keys() function to get
    # sorted list of dictionary keys.
    sorted_list_keys = sort_dict_keys()
    print('ROSTER')

    # For loop to run through the list of keys
    for i in sorted_list_keys:

        # Display jersey number and player's rating
        # sorted by jersey number.
        print("Jersey number: {}, Rating: {}".format(i, player_dict[i]))


