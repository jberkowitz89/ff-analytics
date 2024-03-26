with source as (

    select * from {{ source('ff_analytics', 'box_players') }}

),

renamed as (

    select 
        *,
        to_json(stats) as stats_dict
    from
        source

)

select * from renamed