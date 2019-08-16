from pandas import Series, DataFrame
import pandas as pd
import numpy as np
# Introduction to pandas data structure
# Pandas Series
obj = Series([4, 7, -5, 3])

print(obj)

print(obj.values)

print(obj.index)

obj2 = Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])

print(obj2.values)

print(obj2)

# obj = obj2[obj2 > 2]

print(obj2.index)

print(obj2['c'])

obj2['d'] = 6

print(obj2)

# print(obj2 * 2)


print(np.exp(obj2))

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}

obj3 = Series(sdata)

print(obj3)

states = ['California', 'Ohio', 'Oregon', 'Texas']

obj4 = Series(sdata, index=states)

print(obj4)

# is null or notnull should be used to detect null values

pd.isnull(obj4)

pd.notnull(obj4)

obj3 + obj4

obj4.name = 'population'

obj4.index.name = 'state'

print(obj4)

# object index can be altered

obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']

print(obj)


# Pandas DataFrame

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = DataFrame(data)

print(frame)

frame = DataFrame(data, columns=['year', 'state', 'pop'])

print(frame)

frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])

print(frame2)

print(frame2.columns)

print(frame2['state'])

print(frame2.year)

print(frame2.ix['one'])
frame2['debt'] = 1.6
print(frame2)

frame2.debt = np.arange(5)

print(frame2)

val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])

frame2['debt'] = val

print(frame2)
frame2['eastern'] = frame2.state == 'Ohio'

print(frame2)

del frame2['eastern']

print(frame2.columns)

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame3 = DataFrame(pop)

print(frame3)

print(frame3.T)

print(DataFrame(pop, index=[2001, 2002, 2003]))

pdata = {'Ohio': frame3['Ohio'][:-1], 'Nevada': frame3['Nevada'][:2]}

DataFrame(pdata)

frame3.index.name = 'year'
frame3.columns.name = 'state'

print(frame3)


# Index Object

obj = pd.Series(range(3), index=['a', 'b', 'c'])

index = obj.index

print(index)

print(index[1:])

# index[1] = 'd' # TypeError : "TypeError: Index does not support mutable operations'

labels = pd.Index(np.arange(3))

print(labels)

obj2 = pd.Series([1.5, -2.5, 0], index=labels)

print(obj2)

print(obj2.index is labels)

print(frame3)

print(frame3.columns)

print('Ohio' in frame3.columns)

print(2003 in frame3.index)


dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])

print(dup_labels)


# Essential Functionality

# Reindexing
print(obj)

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])

print(obj)

obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])

print(obj2)

obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])

obj5 = obj3.reindex(range(6), method='ffill')


print(obj5)


# Reindex DataFrame

frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])

print(frame)

frame2 = frame.reindex(['a', 'b', 'c', 'd'])


print(frame2)

states = ['Texas', 'Utah', 'California']
frame.reindex(columns=states)

# Dropping Entries from an Axis

obj = pd.Series(np.arange(50)*2, index=np.arange(50), name='num_square')
obj.index.name = 'pop'
print(obj)

new_obj = obj.drop([x for x in range(5, 10)])
print(new_obj)

data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])

data_1 = data.drop(['Colorado', 'Ohio'])

print(data_1.head())

data_1 = data.drop('two', axis=1)
print(data_1.head())

# Indexing, Selection, and Filtering

obj = pd.Series(np.arange(4), index=['a', 'b', 'c', 'd'])

print(obj['b'])

print(obj[1])

print(obj[2:4])

print(obj[['b', 'a', 'd']])

print(obj[[1, 3]])

# d = obj[obj < 2]
# print(d)
print(obj['b':'d'])

tm = obj['b':'c'] = 5

print(tm)

# Indexing into a DataFrame is for retrieving one or more columns either with a single value or sequence:

data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])

print(data.head())

print(data[['two']])

print(data[['three', 'one']])

print(data[:2])
print(data[data['three'] > 5])

# print(data < 5)

# data[data < 5] = 0
# print(data)


# Selection with loc and iloc

print(data.loc[['Colorado', 'Utah'], ['two', 'three']])

print(data.iloc[[1, 2], [3, 0, 1]])

print(data.loc[:'Utah', :'two'])
print(data.iloc[:, :3][data.three > 5])

# Integer indexes

ser = pd.Series(np.arange(6))
print(ser)


# Arithmetic and Data Alignment

s1 = pd.Series([1.2, 3.4, 4.3, 2.1, 1.8], index=['a', 'b', 'c', 'd', 'e'])

s2 = pd.Series(np.arange(7), index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

print(s1 + s2)

df1 = pd.DataFrame(np.arange(9).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])

df2 = pd.DataFrame(np.arange(12).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(df1)

print(df2)

print(df1 + df2)

df1 = pd.DataFrame({'A': [1, 2]})

df2 = pd.DataFrame({'B': [3, 4]})

print(df1 - df2)

df1 = pd.DataFrame(np.arange(12).reshape((3, 4)), columns=list('abcd'))

df2 = pd.DataFrame(np.arange(20).reshape((4, 5)), columns=list('abcde'))

df2.loc[1, 'b'] = np.nan

print(df1)

print(df2)

print(df1 + df2)

print(df1.add(df2, fill_value=0))

print(1/df1)

print(df1.rdiv(1))

