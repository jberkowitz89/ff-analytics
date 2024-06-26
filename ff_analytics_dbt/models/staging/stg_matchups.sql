with source as (

    select * from {{ source('ff_analytics', 'matchups') }}

),

renamed as (

    select
        {{ dbt_utils.generate_surrogate_key(['home_team_id', 'away_team_id', 'week', 'year']) }} as matchup_id,
        home_team_id,
        away_team_id,
        home_team_name,
        away_team_name,
        lower(matchup_type) as matchup_type,
        home_score,
        away_score,
        is_playoff,
        week,
        year,
        case
            when home_score > away_score then home_team_id
            else away_team_id
        end as winning_team_id,
        case
            when home_score > away_score then away_team_id
            else home_team_id
        end as losing_team_id

    from
        source

)

select * from renamed