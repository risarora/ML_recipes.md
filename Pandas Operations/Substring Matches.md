
batchelors=data['marital-status'].str.startswith('Married')
batchelors=data['marital-status'].str.startswith('Married')
print(data[batchelors]['salary'].value_counts())
