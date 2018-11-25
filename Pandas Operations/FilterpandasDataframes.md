
# Filter pandas Dataframes

## Import modules
```
import pandas as pd
```

### Create Dataframe
```
data = {'name': ['Rishi', 'Ajit', 'Amit', 'Arpit', 'Amy'], 
        'year': [2013, 2014, 2013, 2014, 2014], 
        'cgpa': [4.1, 4.3, 3.1, 2.9, 3.5],
        'coverage': [25, 94, 57, 62, 70]}
df = pd.DataFrame(data, index = ['apple', 'banana', 'orange', 'pineapple', 'plum'])
df
```
### View Column
```
df['name']
```

### View Two Column

```
df[['name', 'cgpa']]
```

### View First Two Rows
```
df[:2]
```
### View Rows Where Coverage Is Greater Than 50
```
df[df['coverage'] > 50]

```
## Filter based on multiple conditions
### View Rows Where Coverage Is Greater Than 50 And cgpa Less Than 3.5

```
df[(df['coverage']  > 50) & (df['cgpa'] < 4)]
```


