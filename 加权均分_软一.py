#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd

NOT_CHOOSE = -2

df1: pd.DataFrame = pd.read_excel('./class_1/成绩表/湘潭大学班级成绩表  (1).xls', skiprows=3, index_col=0)
df1 = df1.replace('不及格', 50).replace('及格', 60).replace('中', 70).replace('良', 80).replace('优', 90)
df1 = df1.fillna(NOT_CHOOSE)
df1 = df1.sort_index()
cred1 = [4, 2, 2, 1, 3.5, 1, 4, 1]

df2: pd.DataFrame = pd.read_excel('./class_1/成绩表/湘潭大学班级成绩表  (2).xls', skiprows=3, index_col=0)
df2 = df2.replace('不及格', 50).replace('及格', 60).replace('中', 70).replace('良', 80).replace('优', 90)
df2 = df2.fillna(NOT_CHOOSE)
df2 = df2.sort_index()
cred2 = [3, 2, 2, 4, 3.5, 4, 2, 1, 4.5, 1]

assert df1.index.equals(df2.index)

print(df1.sample())
print(df2.sample())

res = pd.DataFrame(None, index=df1.index, columns=['姓名', '学科数', '加权总分', '总学分', '加权均分'])
res['姓名'] = df1['姓名']

for i, _ in df1.iterrows():
    if i == 201905556838:
        continue

    xk, zf, xf, jf = 0., 0., 0., 0.
    row1 = [j for j in df1.loc[i]]
    row2 = [j for j in df2.loc[i]]
    assert (row1[0] == row2[0] and type(row1[0]) is str)
    assert (len(row1) - 1 == len(cred1) and len(row2) - 1 == len(cred2))

    for idx, score in enumerate(row1):
        if idx == 0 or score == NOT_CHOOSE:
            continue
        xk += 1
        zf += cred1[idx - 1] * float(score)
        xf += cred1[idx - 1]
    for idx, score in enumerate(row2):
        if idx == 0 or score == NOT_CHOOSE:
            continue
        xk += 1
        zf += cred2[idx - 1] * float(score)
        xf += cred2[idx - 1]
    jf = zf / xf
    res.loc[i]['学科数'] = xk
    res.loc[i]['加权总分'] = zf
    res.loc[i]['总学分'] = xf
    res.loc[i]['加权均分'] = jf

res.to_csv('加权均分_软1.csv', encoding='GBK')
