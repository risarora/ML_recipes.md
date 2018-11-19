import importlib # Fore reloading the library
#importlib.reload(preProcess)

import re
import numpy as np

def add_datepart(df, fldname, drop=True, time=False):
    fld = df[fldname]
    if not np.issubdtype(fld.dtype, np.datetime64):
        df[fldname] = fld = pd.to_datetime(fld, infer_datetime_format=True)
        targ_pre = re.sub('[Dd]ate$', '', fldname)
        attr = ['Year', 'Month', 'Week', 'Day', 'Dayofweek', 'Dayofyear','Is_month_end', 'Is_month_start', 'Is_quarter_end', 'Is_quarter_start', 'Is_year_end', 'Is_year_start']
        if time: attr = attr + ['Hour', 'Minute', 'Second']
        for n in attr: df[targ_pre + n] = getattr(fld.dt, n.lower())
        df[targ_pre + 'Elapsed'] = fld.astype(np.int64) // 10 ** 9
        if drop: df.drop(fldname, axis=1, inplace=True)



def print_NullPercent(data_raw):
    NullCols = data_raw.isnull().sum()!=0
    NullColsNames=data_raw.columns[NullCols]
    #data_raw[data_NullCols].head()

    # TODO FOR LOOP
    for zzx in NullColsNames:
        print(zzx,data_raw[zzx].isnull().sum()/len(data_raw)*100)

        #print("",data_NullCols[0],data_raw[data_NullCols[0]].isnull().sum()/len(data_raw)*100)


def showDataTypes(dataFrame):
    for cols in dataFrame.columns:
        print(cols,dataFrame[cols].dtypes)

#    data_raw.info()


def printColumnCategories(dataFrame):
    for a in dataFrame.columns:
        var = dataFrame[a].dtypes.name
        print(var,a)
        if (var == 'category'):
            print(a, dict( enumerate(dataFrame[a].cat.categories)))
#          print(a, dataFrame[a].cat.categories)


from sklearn import preprocessing
def convert(data):
    number = preprocessing.LabelEncoder()
    data['Employer_Name'] = number.fit_transform(data.Employer_Name)
    data['Source'] = number.fit_transform(data.Source)
    data=data.fillna(-999)
    return data


from sklearn import preprocessing
```
```
def labelFit(dataFrame):
    number = preprocessing.LabelEncoder()
    for azzx in dataFrame.columns:
        dataFrame[azzx] = number.fit_transform(dataFrame[azzx])

#importlib.reload(preProcess)
