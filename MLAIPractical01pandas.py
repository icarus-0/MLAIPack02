import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


s = pd.Series([1,3,4,15,7,8])
print(s)
dates = pd.date_range('20180101',periods=6,freq='D')
print(dates)

#print(np.random.rand(6,4))


df = pd.DataFrame(np.random.rand(6,4),index=dates,columns=['A','B','C','D'])

print(df)
print()
print(df.columns)
print()
print(df.values)
print()
print(df.index)



df2 = pd.DataFrame({'A' : 1.0,
                    'B' : pd.Timestamp("20190102"),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float64'),
                    'D' : pd.array([3]*4,dtype = 'int64'),
                    'E' : pd.Categorical(["test","train","train","test"],categories=["test","train"]),
                    'F' : 'foo'

                      })

#print(df2)

print(df2.dtypes)

print(df.head())

print(df.tail(3))

print(df.sample(3))

print(df.index)

print(df.values)

print(df.columns)

print(df.describe())

print(df.describe(include="all"))

#print(df.T)
#print("\n\n original avalue = \n",df)
#print("sorted value:\n",df.sort_values(by='B',ascending=True))

##############################################################################################333

print(df.A)
print()
print(df['A'])
print("\n\n\n")

print(df['2018-01-01':'2018-01-03'])

print(df[:3])

print(df['20180102':'20180104'])
print("\n\n\n")
print(df.loc[dates[0]])

print("\n\n\n")

print(df.loc[:,['A','B']])

print("\n\n\n")

print(df.loc['20180102':'20180104',['A','B']])


print("\n\n\n")

print(df.loc['20180102',['A','B']])

print("\n\n\n")

print(df.loc[dates[0],'A'])

print("\n\n\n")

print(df.at[dates[0],'A'])

print("\n\n\n")

print(df.iloc[3])

print("\n\n\n")

print(df.iloc[3:5,0:2])

print("\n\n\n")

print(df.iloc[[1,2,4],[0,2]])

print("\n\n\n")


print(df.iloc[1:3,:])

print("\n\n\n")

print(df.iloc[:,1:3])

print("\n\n\n")

print(df.iloc[1,1])

print("\n\n\n")

print(df.iat[1,1])

print("\n\n\n")

print(df.A)

print("\n\n\n")

#print(df.A>0 and df.c>0)
print("\n\n\n")
print(df[df.A>0])
print("\n\n\n")
print(df["B"][df.A>0])


print("\n\n\n")

print(df>0)

print("\n\n\n")

print(df[df>0])

print("\n\n\n")

df2 =df.copy()

df2['E'] = ['one','one','two','three','four','three']

print(df2)

print(df[df2['E'].isin(['two','four'])])

print("\n\n\n")

print(df.mean())

print("\n\n\n")

print(df.B.mean())
print(df['B'].mean())
print("\n\n\n")


print(df[df.B>df.B.mean()])
print("\n\n\n")

print(df.mean(axis=1))
print(df2.drop(df2.index[2:4],axis=0))
print("\n\n\n")

# is invalid expression
# print(df2.drop(df2.columns[1:3],axis=1))


#df.to_excel('output.xls',sheet_name='sheet1')






