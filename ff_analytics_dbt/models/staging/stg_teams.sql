with source as (

    select * from {{ source('ff_analytics', 'teams') }}

),

renamed as (

    select
        team_id,
        team_abbrev,
        team_name,
        division_id,
        division_name,
        wins,
        losses,
        ties,
        points_for,
        points_against,
        acquisitions,
        acquisition_budget_spent,
        drops,
        trades,
        playoff_pct,
        draft_projected_rank,
        streak_length,
        streak_type,
        standing,
        final_standing,
        logo_url,
        roster,
        schedule,
        scores,
        outcomes,
        mov,
        owners,
        year

    from source

)

select * from renamed