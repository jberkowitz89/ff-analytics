---
title: DHSAlumni Analytics
---

```sql categories
  select
      category
  from needful_things.orders
  group by category
```

<Dropdown data={categories} name=category value=category>
    <DropdownOption value="%" valueLabel="All Categories"/>
</Dropdown>

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

<LineChart 
    data={rolling_wins_by_year} 
    x=year 
    y=rolling_wins
    series=owner 
    yAxisTitle="cumulative wins" 
    xAxisTitle="year"
    chartAreaHeight=400
    xMin=2009
    xMax=2024
/>


<Dropdown name=year>
    <DropdownOption value=% valueLabel="All Years"/>
    <DropdownOption value=2019/>
    <DropdownOption value=2020/>
    <DropdownOption value=2021/>
</Dropdown>

