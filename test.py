# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv('newcancer_Data.csv')
a=84230555
for value_i in df.id:
    if (value_i==a):
             print("okkk")