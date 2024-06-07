#Imports
from espn_api.football import League
from constants import LEAGUE_ID, ESPN_S2, SWID

#Constants

def get_league(league_id:int, year:int, espn_s2:str, swid:str) -> League:
    '''
    Function to return a League object from the espn_api football module.

    Args:
        league_id (int): ID of ESPN fantasy football league.
        year (int): Year of the league.
        espn_s2 (str): ESPN_S2 cookie.
        swid (str): SWID cookie.

    Returns:
        League: League object from espn_api.football module.
    '''
    
    league = League(LEAGUE_ID, year, ESPN_S2, SWID)
    return league

def get_settings(league) -> dict:
    '''
    Function to return dictionary of settings for a given league.

    Args:
        league (League): League object from espn_api.football module.
    
    Returns:
        settings_dict (dict): Dictionary of settings for the league.
    '''

    position_keys = ['QB', 'RB', 'WR', 'TE', 'D/ST', 'K', 'BE', 'RB/WR/TE', 'WR/TE']
    settings = league.settings
    settings_dict = vars(settings)
    settings_dict['year'] = league.year
    for position in position_keys:
        try:
            settings_dict[f'n_{position.lower()}'] = settings_dict['position_slot_counts'][position]
        except:
            settings_dict[f'n_{position.lower()}'] = 0
    return settings_dict

def get_draft(league: League) -> list:
    '''
    docstring placeholder
    '''
    draft_picks = list()
    draft = league.draft
    for pick in draft:
        pick_dict = vars(pick)
        pick_dict['team_id'] = pick.team.team_id
        pick_dict['team_name'] = pick.team.team_name
        pick_dict['year'] = league.year
        draft_picks.append(pick_dict)
    return draft_picks

def get_weekly_matchups(league: League) -> list:
    '''
    docstring placeholder
    '''
    all_weeks = list()
    for i in range(len(league.settings.matchup_periods)):
        i += 1
        matchups_lst = league.scoreboard(week=i)
        for matchup in matchups_lst:
            matchup_info = vars(matchup)
            matchup_info['year'] = league.year
            matchup_info['home_team_id'] = matchup_info['home_team'].team_id
            matchup_info['home_team_name'] = matchup_info['home_team'].team_name
            matchup_info['away_team_id'] = matchup_info['away_team'].team_id
            matchup_info['away_team_name'] = matchup_info['away_team'].team_name
            matchup_info['week'] = i
            all_weeks.append(matchup_info)
    return all_weeks

def get_teams(league: League) -> list:
    '''
    docstring placeholder
    '''
    all_teams = list()
    for team in league.teams:
        team_info = vars(team)
        team_info['year'] = league.year
        all_teams.append(team_info)
    return all_teams

def get_players(league: League) -> list:
    '''
    docstring placeholder
    '''
    all_players = list()
    for team in league.teams:
        for player in team.roster:
            player_info = vars(player)
            player_info['year'] = league.year
            player_info['team_id'] = team.team_id
            player_info['team_name'] = team.team_name
            all_players.append(player_info)
    return all_players

def get_box_scores(league: League) -> list:
    '''
    docstring placeholder
    '''
    all_box_scores = list()
    if league.year < 2019:
        print('Box scores not available for '+ str(league.year))
    else:
        for i in range(len(league.settings.matchup_periods)):
            i += 1
            box_scores_lst = league.box_scores(week=i)
            for box_score in box_scores_lst:
                box_score_info = vars(box_score)
                box_score_info['year'] = league.year
                box_score_info['home_team_id'] = box_score_info['home_team'].team_id
                box_score_info['home_team_name'] = box_score_info['home_team'].team_name
                box_score_info['away_team_id'] = box_score_info['away_team'].team_id
                box_score_info['away_team_name'] = box_score_info['away_team'].team_name
                box_score_info['week'] = i
                all_box_scores.append(box_score_info)
        return all_box_scores
    
def get_box_players(league: League) -> list:
    '''
    docstring placeholder
    '''
    all_box_players = list()
    player_info = dict()
    stats_keys = ['rushingAttempts', 'rushingYards', 'rushingTouchdowns', 'rushingYardsPerAttempt',
                  'receivingReceptions', 'receivingYards', 'receivingTargets', 'receivingYardsAfterCatch',
                  'receivingTouchdowns', 'receivingYardsPerReception', 'passingAttempts', 'passingCompletions',
                  'passingYards', 'passingTouchdowns', 'passingInterceptions', 'passingYardsPerAttempt',
                  'turnovers', 'fumblesLost']
    if league.year < 2019:
        print('Box players not available for '+ str(league.year))
    else:
        for i in range(len(league.settings.matchup_periods)):
            i += 1
            box_scores_lst = league.box_scores(week=i)
            for box_score in box_scores_lst:
                for player in box_score.home_lineup:
                    player_info = vars(player)
                    player_info['year'] = league.year
                    player_info['team_id'] = box_score.home_team.team_id
                    player_info['team_name'] = box_score.home_team.team_name
                    player_info['week'] = i
                    for field in stats_keys:
                        try:
                            player_info[field] = player_info['points_breakdown'][field]
                        except:
                            player_info[field] = 0
                    all_box_players.append(player_info)
                for player in box_score.away_lineup:
                    player_info = vars(player)
                    player_info['year'] = league.year
                    player_info['team_id'] = box_score.away_team.team_id
                    player_info['team_name'] = box_score.away_team.team_name
                    player_info['week'] = i
                    for field in stats_keys:
                        try:
                            player_info[field] = player_info['points_breakdown'][field]
                        except:
                            player_info[field] = 0
                    all_box_players.append(player_info)
        return all_box_players
            
if __name__ == '__main__':
    my_league = get_league(LEAGUE_ID, 2009, ESPN_S2, SWID)
    settings = get_settings(my_league)
    print(type(settings))
    print(settings)