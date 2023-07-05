# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv('newcancer_Data.csv', index_col ='id')
  

  
# retrieving rows by loc method 
rows = df.loc[842302] 
  
# checking data type of rows 
print(type(rows)) 
  
# display 
radius=rows.radius_worst
