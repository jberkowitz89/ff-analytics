with source as (

    select * from {{ source('ff_analytics', 'players') }}

),

renamed as (

    select
        name,
        "playerId" as player_id,
        "posRank" as pos_rank,
        "eligibleSlots" as eligible_slots,
        "acquisitionType" as acquisition_type,
        "proTeam" as pro_team,
        "injuryStatus" injury_status,
        "onTeamId" as on_team_id,
        stats,
        position,
        injured,
        percent_owned,
        percent_started,
        active_status,
        total_points,
        projected_total_points,
        avg_points,
        projected_avg_points,
        year,
        team_id,
        team_name

    from source

)

select * from renamed