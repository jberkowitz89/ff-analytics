from get_data import get_league, get_settings, get_draft, get_weekly_matchups, get_teams, get_players, get_box_scores, get_box_players
from constants import LEAGUE_ID, ESPN_S2, SWID
from make_csvs import settings_csv, draft_csv, matchups_csv, teams_csv, players_csv, box_scores_csv, box_players_csv

if __name__ == '__main__':
    start_year = int(input('Enter the year you want to start collecting data from: '))
    end_year = int(input('Enter the year you want to end collecting data from: '))
    all_settings, all_drafts, all_matchups, all_teams, all_players, all_box_scores, all_box_players = ([] for i in range(7))
    for year in range(start_year, end_year + 1):
        my_league = get_league(LEAGUE_ID, year, ESPN_S2, SWID)
        settings = get_settings(my_league)
        drafts = get_draft(my_league)
        matchups = get_weekly_matchups(my_league)
        teams = get_teams(my_league)
        players = get_players(my_league)
        box_scores = get_box_scores(my_league)
        box_players = get_box_players(my_league)
        all_settings.append(settings)
        all_drafts.append(drafts)
        all_matchups.append(matchups)
        all_teams.append(teams)
        all_players.append(players)
        if box_scores != None:
            all_box_scores.append(box_scores)
        if box_players != None:
            all_box_players.append(box_players)
    settings_csv(all_settings)
    draft_csv(all_drafts)
    matchups_csv(all_matchups)
    teams_csv(all_teams)
    players_csv(all_players)
    box_scores_csv(all_box_scores)
    box_players_csv(all_box_players)