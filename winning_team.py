class Team:
    def __init__(self):
        self.team_name = None
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        calculation = (self.team_wins / (self.team_wins + self.team_losses))
        return calculation


if __name__ == '__main__':

    user_input = Team()

    user_input.team_name = str(input())
    user_input.team_wins = int(input())
    user_input.team_losses = int(input())

    if (user_input.get_win_percentage() >= 0.50):
        print('Congratulations, Team {} has a winning average!'.format(user_input.team_name))
    else:
        print('Team {} has a losing average.'.format(user_input.team_name))

