{{
  config(
    materialized = 'table',
    )
}}

with matchups_enhanced as (

    select 
        *
    from 
        {{ ref('fct_matchups_enhanced') }} 
    where
        matchup_type not in ('losers_consolation_ladder', 'winners_consolation_ladder')

),

wins_by_year as (

    select
        winning_team_owner as owner,
        year,
        count(*) as wins
    from
        matchups_enhanced
    group by 1,2
)

select
    owner,
    year,
    wins,
    sum(wins) over (partition by owner order by year) as rolling_wins
from
    wins_by_year
