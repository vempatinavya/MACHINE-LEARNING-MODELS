
import pandas as pd
data=pd.read_csv('https://github.com/cs109/2014_data/blob/master/countries.csv',sep = "\t")


a=[1,2,3,4]
d=pd.Series(a)
print(d)

b=[[2,3,4],[7,8,9]]
#e=pd.DataFrame(b)
e=pd.DataFrame(b,columns=['c','java','python'])
#print(e['java'])
e.size
e.shape


data=pd.read_csv(r'C:\Users\Navya\Downloads\IMDB-Movie-Data.csv')
#print(data.columns)
#unique elements
print(data['Year'].unique())

#unique count
a=list(data['Year'].unique())
print(len(a))

#all count
print(data['Year'].value_counts())

#data[data['Rating']>6.0]

data[(data['Rating']>6.0) &
     (data['Revenue (Millions)']>100.0)]

#to know empty values
data.isnull()
data['Revenue (Millions)'].isnull().value_counts()
data.isnull().sum()
#to drop empty rows
z=data.dropna()


#to replace empty values
y=data.fillna(0)
y['Revenue (Millions)'].isnull().value_counts()
#to fill with average of perticular row
y['Revenue (Millions)'].fillna(
    y['Revenue (Millions)'].mean())
#to delete empty rows
x=data.dropna()
x['Revenue (Millions)'].isnull().value_counts()

#to create duplicate rows
data=data.append(data)
data.shape

#delete duplicates
data=data.drop_duplicates()
d[(d['Director']=='Ridley Scott') & (d['Year']==2012)].count()

d[(d['Year']==2012) & (d['Revenue(Millions)']>100.0)]
