with source as (

    select * from {{ source('ff_analytics', 'settings') }}

),

renamed as (

    select
        {{ dbt_utils.generate_surrogate_key(['name']) }} as league_id,
        name as league_name,
        scoring_type,
        faab as is_faab,
        reg_season_count as n_weeks_reg_season,
        array_length(matchup_periods::text[], 1) as n_weeks_total,
        array_length(matchup_periods::text[], 1) - reg_season_count as n_weeks_playoffs,
        veto_votes_required,
        team_count as n_teams,
        playoff_team_count as n_playoff_teams,
        keeper_count,
        to_timestamp(trade_deadline/1000) as trade_deadline
    from
        source

)

select * from renamed