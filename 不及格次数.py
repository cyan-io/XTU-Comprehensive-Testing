import pandas as pd

df1: pd.DataFrame = pd.read_excel('./排名表/湘潭大学班级成绩排名表 .xls', skiprows=2, index_col=0, usecols=[0, 1, 9])
df2: pd.DataFrame = pd.read_excel('./排名表/湘潭大学班级成绩排名表  (1).xls', skiprows=2, index_col=0, usecols=[0, 1, 9])
df3: pd.DataFrame = pd.read_excel('./排名表/湘潭大学班级成绩排名表  (2).xls', skiprows=2, index_col=0, usecols=[0, 1, 9])
df4: pd.DataFrame = pd.read_excel('./排名表/湘潭大学班级成绩排名表  (3).xls', skiprows=2, index_col=0, usecols=[0, 1, 9])

df1 = df1.sort_index()
df2 = df2.sort_index()
df3 = df3.sort_index()
df4 = df4.sort_index()

assert df1.index.equals(df2.index) and df2.index.equals(df3.index) and df3.index.equals(df4.index)

print(df1.sample())
print(df2.sample())
print(df3.sample())
print(df4.sample())

res = pd.DataFrame(0, index=df1.index, columns=df1.columns)
COL = '不及格次数'
res[COL] = df1[COL] + df2[COL] + df3[COL] + df4[COL]
res['姓名'] = df1['姓名']
print(res)
res.to_csv('不及格次数.csv', encoding='GBK')
