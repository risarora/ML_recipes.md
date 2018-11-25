



batchelors=data['marital-status'].str.startswith('Married')


data[batchelors]['salary'].value_counts()

data[~ batchelors]['salary'].value_counts()

