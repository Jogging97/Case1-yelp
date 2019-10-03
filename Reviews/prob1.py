import pandas as pd

bus= pd.read_csv("Yelp Data Files/CSV Files/business.csv")

#bus.shape
f = bus[['categories']]

f = f[pd.notnull(f['categories'])]
f.isnull().sum()
l = f['categories'].apply(lambda x: x.split(","))

import numpy as np
l = pd.DataFrame(l)
a = pd.Series([item for sublist in l.categories for item in sublist])
df = a.groupby(a).size().rename_axis('category').reset_index(name='count')
s = df.sort_values('count',ascending=False)
s = pd.DataFrame(s)
s['category'] = s['category'].astype(str)
s['category'] = s['category'].apply(lambda x: x.strip())
aggregation_functions = {'category': 'first','count': 'sum'}
d = s.groupby(s['category']).aggregate(aggregation_functions)
d = d.sort_values('count',ascending=False)
q = d.iloc[:10]
print (q.to_string(index=False))