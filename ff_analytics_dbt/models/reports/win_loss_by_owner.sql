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

winners as (

    select
        winning_team_owner as owner,
        year,
        count(*) as wins
    from matchups_enhanced
    group by 1, 2

),

losers as (

    select
        losing_team_owner as owner,
        year,
        count(*) as losses
    from matchups_enhanced
    group by 1, 2

),

totals as (

    select
        winners.owner,
        winners.year,
        coalesce(wins,0) as wins,
        coalesce(losses,0) as losses
    from winners
    left join losers
        on winners.owner = losers.owner
        and winners.year = losers.year
)

select * from totals