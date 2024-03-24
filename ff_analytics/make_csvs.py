import csv
from get_data import get_league
from constants import LEAGUE_ID, ESPN_S2, SWID

def settings_csv(settings):
    '''
    docstring placeholder
    '''
    keys = settings[0].keys()
    with open('data/settings.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(settings)


def draft_csv(all_drafts):
    '''
    docstring placeholder
    '''
    keys = all_drafts[0][0].keys()
    with open('data/draft.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        for draft in all_drafts:
            for pick in draft:
                writer.writerow(pick)

def matchups_csv(all_matchups):
    '''
    docstring placeholder
    '''
    keys = all_matchups[0][0].keys()
    with open('data/matchups.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        for season in all_matchups:
            for matchup in season:
                writer.writerow(matchup)

def teams_csv(all_teams):
    '''
    docstring placeholder
    '''
    keys = all_teams[0][0].keys()
    with open('data/teams.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        for teams in all_teams:
            for team in teams:
                writer.writerow(team)

def players_csv(all_players):
    '''
    docstring placeholder
    '''
    keys = all_players[0][0].keys()
    with open('data/players.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        for players in all_players:
            for player in players:
                writer.writerow(player)

def box_scores_csv(all_box_scores):
    '''
    docstring placeholder
    '''
    keys = all_box_scores[0][0].keys()
    try:
        with open('data/box_scores.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            for box_scores in all_box_scores:
                for box_score in box_scores:
                    writer.writerow(box_score)
    except:
        pass

def box_players_csv(all_box_players):
    '''
    docstring placeholder
    '''
    keys = all_box_players[0][0].keys()
    try:
        with open('data/box_players.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            for box_players in all_box_players:
                for box_player in box_players:
                    writer.writerow(box_player)
    except:
        pass

if __name__ == '__main__':
    my_league = get_league(LEAGUE_ID, 2021, ESPN_S2, SWID)
    settings_csv(my_league)
    draft_csv(my_league)
    matchups_csv(my_league)
    teams_csv(my_league)
    players_csv(my_league)
    box_scores_csv(my_league)
    box_players_csv(my_league)
