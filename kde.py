# -*- coding: utf-8 -*-
import numpy as np

def univar_continue_KL_divergence(p, q):
    # p is target distribution
    return np.log(q[1] / p[1]) + (p[1] ** 2 + (p[0] - q[0]) ** 2) / (2 * q[1] ** 2) - 0.5

p = (mu1, sigma1) = 0.2, 0.1
q = (mu2, sigma2) = 3, 0.5
print(univar_continue_KL_divergence(p, q))  # 16.8094379124341
print(univar_continue_KL_divergence(q, p))  # 402.3905620875658
print(univar_continue_KL_divergence(p, p))  # 0.0


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