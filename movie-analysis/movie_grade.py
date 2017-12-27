#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Cousera课程《用Python玩转数据 Data Processing Using Python》第4.2章编程作业《男女电影评分差异分析编程》
#
#分析数据集，找出男性女性用户评分的标准差，并输出两位小数部分
#提示：先分别计算每个人电影评分的平均分，再按性别求标准差

#使用方法：
# python movie_grade.py > result.txt

import pandas

#读取评分数据
#  格式user id | item id | rating | timestamp
data_df = pandas.read_table("./data/u.data", names=('userid', 'rating'), usecols=[0,2])

#读取用户数据
#  格式user id | age | gender | occupation | zip code
user_df = pandas.read_table("./data/u.user", sep='|', names=['userid','gender'], usecols=[0,2])

#组合数据
df = pandas.merge(data_df, user_df)

#分别计算男女用户的方差
std_male=df[df.gender=='M'].groupby('userid').rating.mean().std()
std_female=df[df.gender=='F'].groupby('userid').rating.mean().std()

#输出结果
print('{:.0f}{:.0f}'.format(std_male*100,std_female*100))