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


# OBJ 3:
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


# OBJ 4:
# Define add_player() function.
def add_user():
    # Prompt user to enter a jersey number
    print("Enter a new player's jersey number:")
    jersey_num = int(input())

    # Check if jersey number is between 0 - 99.
    # If not, ask user to enter a jersey number again.
    while ((jersey_num < 0) or (jersey_num > 99)):
        print("Invalid Jersey Number! Please enter again!")
        print("Enter a new player's jersey number:")
        jersey_num = int(input())

    # Prompt user to enter player's rating.
    print("Enter the player's rating:")
    player_rating = int(input())

    # Check if player_rating is between 1 - 9
    # If not, ask user to enter player_rating again.
    while ((player_rating < 1) or (player_rating > 9)):
        print("Invalid Rating! Please enter again!")
        print("Enter the player's rating:")
        player_rating = int(input())

    # Update the player dictionary (player_dict) with
    # the new entry.
    player_dict.update({jersey_num : player_rating})


# OBJ 5:
# Define delete_player() function
def delete_player():

    # Prompt user for a player's jersey number.
    print("Enter a jersey number:")
    jersey_number = int(input())

    # Remove that player from the roster (delete jersey number and rating)
    if jersey_number in player_dict:
        del player_dict[jersey_number]



