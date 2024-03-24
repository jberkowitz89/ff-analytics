with source as (

    select * from {{ source('ff_analytics', 'draft') }}

),

renamed as (

    select
        {{ dbt_utils.generate_surrogate_key(['"playerId"', 'team_id', 'round_num', 'round_pick']) }} as draft_pick_id,
        team_id,
        "playerId" as player_id,
        team_name,
        "playerName" as player_name,
        "nominatingTeam" as nominating_team,
        round_num,
        round_pick,
        bid_amount,
        keeper_status,
        year
    from
        source

)

select * from renamed