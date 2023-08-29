class League:
    def __init__(self, team, season):
        self.team = team
        self.season = season

    def info(self):
        print(f"IPL Season {self.season} is won by {self.team}")


class Season(League):

    def player(self, player):
        print(f'Player of the season won by {player}')


if __name__ == '__main__':
    team_list = ['RR', 'CSK', 'DC', 'MI', 'KXIP', 'SRH', 'RCB', 'GT', 'LSG']
    season_list = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
    player_list = ['Sehwag', 'Sachin', 'Kaif', 'Gambhir', 'Kohli', 'Ganguly', 'Dravid', 'Laxman', 'Kumble']
    for i in range(0, 9):
        b = Season(team_list[i], season_list[i])
        b.info()
        b.player(player_list[i])
        print('-' * 50)
