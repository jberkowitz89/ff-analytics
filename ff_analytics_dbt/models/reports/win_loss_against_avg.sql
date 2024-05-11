with matchups_enhanced as (

    select 
        *
    from 
        {{ ref('fct_matchups_enhanced') }} 
    where
        matchup_type not in ('losers_consolation_ladder', 'winners_consolation_ladder')


),

wins as (

    select
        winning_team_owner as owner,
        losing_team_owner as opponent,
        year,
        week,
        case 
        	when home_team_id = winning_team_id then home_score
        	when away_team_id = winning_team_id then away_score
        	else 0
        end as team_score,
        case when home_team_id = losing_team_id then home_score
        	when away_team_id = losing_team_id then away_score
        	else 0 
        end as opponent_score,
        'win' as result, 
        round(avg_pts_per_team::numeric, 2) as weekly_avg_pts
    from matchups_enhanced

),

losers as (

    select
        losing_team_owner as owner,
        winning_team_owner as opponent,
        year,
        week,
        case
        	when home_team_id = losing_team_id then home_score
        	when away_team_id = losing_team_id then away_score
        	else 0
        end as team_score,
        case
        	when home_team_id = winning_team_id then home_score
        	when away_team_id = winning_team_id then away_score
        	else 0
        end as opponent_score,
        'loss' as result,
        round(avg_pts_per_team::numeric, 2) as weekly_avg_pts
    from matchups_enhanced
    
),

unioned as (
	select * from wins
	union all
	select * from losers

),

final as (

    select
        *,
        team_score - weekly_avg_pts as delta_from_avg,
        opponent_score - weekly_avg_pts as opponent_delta_from_avg
    from
        unioned

)

select * from final