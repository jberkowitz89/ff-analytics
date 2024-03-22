with source as (

    select * from {{ source('ff_analytics', 'box_scores') }}

),

renamed as (

    select
        {{ dbt_utils.generate_surrogate_key(['home_team_id', 'away_team_id', 'home_score', 'away_score']) }} as box_score_id,
        home_team_id,
        away_team_id,
        lower(home_team) as home_team,
        lower(away_team) as away_team,
        lower(matchup_type) as matchup_type,
        home_score,
        away_score,
        home_projected,
        away_projected,
        home_score - home_projected as home_projected_delta,
        away_score - away_projected as away_projected_delta,
        week,
        year,
        home_team_name,
        away_team_name,
        home_lineup,
        away_lineup,
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