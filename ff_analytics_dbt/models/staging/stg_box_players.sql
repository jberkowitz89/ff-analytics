with source as (

    select * from {{ source('ff_analytics', 'box_players') }}

),

renamed as (

    select 
        *
    from
        source

)

select * from renamed