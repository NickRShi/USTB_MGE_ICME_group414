"""

Created on Dec,27,2020
@author: junyun,Pan
Aim：反向拟合物性参数。
"""

######################################################################
#imput

import sys
import os
from mupif import * 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import logging
log = logging.getLogger()
#get 
######################################################################  
#Step 1: input 50组不同参数对应的输入文件   distributed compute

#run micress

#get 50张图片，不同的界面能对应的晶粒分布
###################################################################### 
#Step 2: input 50张图片

#imagepy

#get 尺寸分布
###################################################################### 
#Step 3: input 尺寸分布
df=pd.read_csv('../test.csv')
df1=df['Area']

df3=0

for i in range(len(df1)):
    df3  = df3 + df1[i]/len(df1)
df2=np.sort(np.array(df1)) / df3

plt.style.use('seaborn-white')

plt.hist(df2, bins=10, density=True, alpha=0.5, histtype='stepfilled',
         color='steelblue', edgecolor='none')#bins调节横坐标分区个数，alpha参数用来设置透明度
sns.set()
sns.kdeplot(df2)
#get 核密度估计
######################################################################
#Step 4: input 核密度估计(实验&&模拟)



#get  KL(EXPMS||PRDMS)
######################################################################
#Step 5: input KL(EXPMS||PRDMS)

#GPR+Baysian


#get next interfacial energy
######################################################################
#Step 6: input interfacial energy

#Step 1--->Step 2--->Step 3--->Step 4--->Step 5  until KL<某个值


#get 
######################################################################
#Step 7: input



#get
######################################################################