with source as (

    select * from {{ source('ff_analytics', 'box_players') }}

),

renamed as (

    select 
        -- ids
        "playerId" as player_id,
        team_id,
        "onTeamId" as on_team_id,

        --descriptives
        name as player_name,
        position,
        slot_position,
        "proTeam" as pro_team,
        pro_opponent,
        pro_pos_rank,
        "injuryStatus" as injury_status,
        active_status as active_status,
        team_name,


        --amounts
        points,
        projected_points,
        points - projected_points as projection_delta,
        "rushingAttempts" as rushing_attempts,
        "rushingYards" as rushing_yards,
        "rushingTouchdowns" as rushing_touchdowns,
        "rushingYardsPerAttempt" as rushing_yards_per_attempt,
        "receivingReceptions" as receiving_receptions,
        "receivingYards" as receiving_yards,
        "receivingTargets" as receiving_targets,
        "receivingTouchdowns" as receiving_touchdowns,
        "receivingYardsPerReception" as receiving_yards_per_reception,
        "passingAttempts" as passing_attempts,
        "passingCompletions" as passing_completions,
        "passingYards" as passing_yards,
        "passingTouchdowns" as passing_touchdowns,
        "passingInterceptions" as passing_interceptions,
        "passingYardsPerAttempt" as passing_yards_per_attempt,
        "fumblesLost" as fumbles_lost,
        turnovers,

        --booleans
        injured as is_injured,

        --dates/times
        game_date,
        year,
        week

    from
        source

)

select * from renamed