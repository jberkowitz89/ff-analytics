---
title: DHSAlumni Analytics
---

```sql unique_owners
select 
    owner
from ff_analytics.rolling_wins_by_year
group by 1
```

```sql years
select
  year
from ff_analytics.rolling_wins_by_year
group by 1
```

<Dropdown 
  data={unique_owners} 
  name=owner 
  value=owner
  multiple=true
  defaultValue={['berkowitz', 'klein', 'stein', 'katz', 'kogan', 'stein_kamoo', 'treshansky', 'rosenberg', 'lirtzman', 'zwick']}
  title="Select Owner(s)"
  >
</Dropdown>


<Dropdown 
  data={years} 
  name=years 
  value=year 
  multiple=true
  defaultValue={[2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]}
  >
</Dropdown>

```sql win_loss_by_owner
  select
    owner,
    sum(wins) as wins,
    sum(losses) as losses
  from
    ff_analytics.win_loss_by_owner
  where owner in ${inputs.owner.value}
  and year in ${inputs.years.value}
  group by 1
  order by 2 desc
```

<DataTable 
  data={win_loss_by_owner}
  title="Total Wins and Losses by Owner"> 
</DataTable>

```sql win_loss_by_opponent
  select
    owner,
    opponent,
    sum(wins) as wins,
    sum(losses) as losses
  from
    ff_analytics.win_loss_by_opponent
  where
    owner in ${inputs.owner.value}
  group by 1, 2
```

<DataTable 
  data={win_loss_by_opponent}
  title="Total Wins and Losses by Owner by Opponent"> 
</DataTable>


```sql rolling_wins_by_year
  select
    owner,
    year,
    wins,
    rolling_wins
  from ff_analytics.rolling_wins_by_year
  where owner in ${inputs.owner.value}
  and year in ${inputs.years.value}
```

<LineChart 
    data={rolling_wins_by_year} 
    x=year 
    y=rolling_wins
    series=owner
    title="Year over Year Wins by Owner" 
    yAxisTitle="cumulative wins" 
    xAxisTitle="year"
    chartAreaHeight=400
    xMin=2009
    xMax=2024
/>
