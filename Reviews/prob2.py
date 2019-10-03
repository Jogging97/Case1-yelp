
import pandas as pd


bus= pd.read_csv("venv/business.csv")
ckin = pd.read_csv("venv/checkin.csv")

#ckin.shape
#ckin.head()
#d1 = ckin.duplicated(subset="business_id")
#ckin.groupby('business_id').count()

#ckin.isnull().values.any()
#ckin.isnull().sum().sum()

ckin['dl'] = ckin['date'].apply(lambda x: x.split(","))
ckin['count'] = ckin['date'].str.len()
ckin1 = ckin.sort_values('count',ascending=False)
f = ckin1[['business_id', 'count']]
r = pd.merge(f, bus, on='business_id')
a = r.iloc[:10]
print a.to_string(index=False)
