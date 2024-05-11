---
title: "Weekly Performance Against Average"
---

```sql unique_owners
select 
    owner
from ff_analytics.win_loss_against_avg
group by 1
```

```sql years
select
  year
from ff_analytics.win_loss_against_avg
group by 1
```

<Dropdown 
  data={unique_owners} 
  name=owner 
  value=owner
  multiple=true
  defaultValue={['berkowitz']}
  title="Select Owner(s)"
  >
</Dropdown>


<Dropdown 
  data={years} 
  name=years 
  value=year 
  multiple=true
  defaultValue={[2023]}
  >
</Dropdown>

```sql win_loss_against_avg
  select
    owner,
    opponent,
    team_score,
    opponent_score,
    result,
    pts_above_or_below_avg,
    opponent_pts_above_or_below_avg
  from
    ff_analytics.win_loss_against_avg
  where
    owner in ${inputs.owner.value}
    and year in ${inputs.years.value}
```

<ScatterPlot 
    data={win_loss_against_avg} 
    x=pts_above_or_below_avg
    y=opponent_pts_above_or_below_avg
    series=result 
    title="Wins and Losses Against Weekly Average"
    xAxisTitle="Points Scored v. Weekly Avg" 
    yAxisTitle="Points Against v. Weekly Avg" 
    chartAreaHeight=500
    seriesColors={{'win': 'green', 'loss': 'red'}}
    >
    <ReferenceLine x=0 color=black hideValue=true lineType=solid lineWidth=1/>
    <ReferenceArea xMin=0 xMax=100 yMin=0 color=green label="good performance"/>
    <ReferenceArea xMin=-100 xMax=0 yMin=-100 yMax=0 color=red label="bad performance"/>
</ScatterPlot>