"""

Created on Dec,27,2020
@author: junyun,Pan
Aim：反向拟合物性参数。
"""

######################################################################
#input

import sys
import os
mupif_dir=os.path.abspath(os.path.join(os.getcwd(), "../"))
sys.path.append(mupif_dir)
import mupif
import numpy as np
from scipy import stats
from bayes_opt import BayesianOptimization
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

#get 尺寸分布 ->psd.csv
###################################################################### 
#Step 3: input 尺寸分布

df=pd.read_csv('psd.csv').values

#get 核密度估计
######################################################################
#Step 4: input 核密度估计(实验&&模拟)
def kde_error(label,yhat):
    yhat = np.array(yhat)
    label = np.array(label)
    error_sum = ((yhat - label)**2).sum()
    return kde_error_sum


c=[]
d=[]
for i in range(6):
    c.append(sns.distplot(df[1:,i]).get_lines()[i].get_data()[1])
    
for j in range(1,6): 
    d.append(kde_error(c[0],c[j]))
#get  KL(EXPMS||PRDMS)
######################################################################
#Step 5: input KL(EXPMS||PRDMS)

#GPR+Baysian
def black_box_function(x, y):
    """Function with unknown internals we wish to maximize.

    This is just serving as an example, for all intents and
    purposes think of the internals of this function, i.e.: the process
    which generates its output values, as unknown.
    """
    
    
    return -x ** 2 - (y - 1) ** 2 + 1


pbounds = {'x': (2, 4), 'y': (-3, 3)}

optimizer = BayesianOptimization(
    f=black_box_function,
    pbounds=pbounds,
    random_state=1,
)

optimizer.maximize(
    init_points=2,
    n_iter=3,
)
#get next interfacial energy
######################################################################
#Step 6: input interfacial energy

#Step 1--->Step 2--->Step 3--->Step 4--->Step 5  until KL<某个值
micressJobs = cConf.micressJobs
for i in range(micressJobs):
  
  # initialize working directory for MICRESS
  # i.e. make directory if necessary,
  #      copy input files 
  jobsWorkdir = cConf.localWorkdir + "/" + str(jobs)
  print ("Creating working directory ... (or reuse existing)")
  print (jobsWorkdir)
  if ( not os.path.exists(jobsWorkdir) ):
    #raw_input('Press <ENTER> to confirm. Break with <CTRL-C>.')
    os.mkdir(jobsWorkdir)
  for f in cConf.micressInputFiles:
    filename = cConf.micressPrefix + '/' + f            
    dest = jobsWorkdir + "/" + f
    try:
      copyfile(filename,dest)
    except:
      print ("Error: file copy failed")
      print (f + ' -> ' + dest )
      sys.exit()
  
  # get an MICRESS interface object    
  try:
    mic.append(micress.micress(workdir=jobsWorkdir, file='input.in'))
  except Exception as e:
    log.error('jobsWorkdir=%s' % (jobsWorkdir) )
    log.exception(e)
    ## set the properties for micro simulation
    mic[interface].setProperty(propLocation)
    mic[interface].setProperty(propT)
    mic[interface].setProperty(propzG) 

    ## make a MICRESS step
    mic[interface].solveStep(istep)
    
#get 
######################################################################
#Step 7: input



#get
######################################################################