with matchups as (

    select * from {{ ref('stg_matchups') }} where year <= 2018

),

box_scores as (

    select * from {{ ref('stg_box_scores') }}

),

team_owners as (

    select * from {{ ref('team_owners') }}

),

matchups_joined as (

    select
        --ids
        matchups.matchup_id,
        matchups.home_team_id,
        matchups.away_team_id,
        
        --descriptives
        home_team_owners.owner_name as home_team_owner,
        away_team_owners.owner_name as away_team_owner,
        matchups.home_team_name,
        matchups.away_team_name,
        matchups.winning_team_id,
        matchups.losing_team_id,
        winning_team_owners.owner_name as winning_team_owner,
        losing_team_owners.owner_name as losing_team_owner,
        matchups.matchup_type,

        --amounts
        matchups.home_score,
        matchups.away_score,
        --projections dont exist for matchup data
        null::float as home_projected_score,
        null::float as away_projected_score,
        null::float as home_projected_delta,
        null::float as away_projected_delta,

        --dates/times
        matchups.week,
        matchups.year
    from
        matchups
    left join team_owners as home_team_owners
        on matchups.home_team_id = home_team_owners.team_id
    left join team_owners as away_team_owners
        on matchups.away_team_id = away_team_owners.team_id
    left join team_owners as winning_team_owners
        on matchups.winning_team_id = winning_team_owners.team_id
    left join team_owners as losing_team_owners
        on matchups.losing_team_id = losing_team_owners.team_id

),

box_scores_joined as (

    select
        --ids
        box_scores.box_score_id,
        box_scores.home_team_id,
        box_scores.away_team_id,

        --descriptives
        home_team_owners.owner_name as home_team_owner,
        away_team_owners.owner_name as away_team_owner,
        box_scores.home_team_name,
        box_scores.away_team_name,
        box_scores.winning_team_id,
        box_scores.losing_team_id,
        winning_team_owners.owner_name as winning_team_owner,
        losing_team_owners.owner_name as losing_team_owner,
        box_scores.matchup_type,

        --amounts
        box_scores.home_score,
        box_scores.away_score,
        box_scores.home_projected_score,
        box_scores.away_projected_score,
        box_scores.home_projected_delta,
        box_scores.away_projected_delta,

        --times
        box_scores.week,
        box_scores.year
    from
        box_scores
    left join team_owners as home_team_owners
        on box_scores.home_team_id = home_team_owners.team_id
    left join team_owners as away_team_owners
        on box_scores.away_team_id = away_team_owners.team_id
    left join team_owners as winning_team_owners
        on box_scores.winning_team_id = winning_team_owners.team_id
    left join team_owners as losing_team_owners
        on box_scores.losing_team_id = losing_team_owners.team_id

),

unioned as (

    select * from matchups_joined
    union all
    select * from box_scores_joined

),

matchups_enhanced as (

    select
        *,
        case
            when home_team_id = winning_team_id then home_score - away_score
            else away_score - home_score
        end as margin_of_victory,
        home_score + away_score as total_matchup_points,
        sum(home_score + away_score) over (partition by week, year) as total_week_points,
        count(matchup_id) over (partition by week, year) as total_week_matchups,
        case
            when year < 2011 then (sum(home_score + away_score) over (partition by week, year)) / 12
            else (sum(home_score + away_score) over (partition by week, year)) / 10
        end as avg_pts_per_team
    from
        unioned

)


select 
    *,
    home_score - avg_pts_per_team as home_score_diff_from_avg,
    away_score - avg_pts_per_team as away_score_diff_from_avg
from 
    matchups_enhanced 
