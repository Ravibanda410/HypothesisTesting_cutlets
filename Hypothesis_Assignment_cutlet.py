# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:54:08 2020

@author: RAVI
"""


import pandas as pd
import scipy
from scipy import stats
import statsmodels.api as sm

############2 sample T Test(Cutlets) ##################

Cutlets=pd.read_excel("C:\RAVI\Data science\Assignments\Modue 5 Hypothesis\Cutlets.xlsx")
Cutlets

Cutlets.columns="UnitA","UnitB"
##########Normality Test ############
#Ho= Data is normally distributed (no action take)
#Ha=Data is not normally distributed (action take)



Cutlets=Cutlets.iloc[0:35,]

stats.shapiro(Cutlets.UnitA)
# p-value = 0.319 >0.05 so p high null fly => It follows normal distribution

print(stats.shapiro(Cutlets.UnitB))
# p-value = 0.522 >0.05 so p high null fly => It follows normal distribution 

#############Variance test###############
     
#Ho= Variance of diameters of Unit A is equal to the variance of diameters of Unit B
#Ha= Variance of diameters of Unit A is not equal to the variance of diameters of Unit B
scipy.stats.levene(Cutlets.UnitA,Cutlets.UnitB)
# p-value = 0.41 > 0.05 so p high null fly => Equal variances accept null hypothesis.


######## 2 Sample T test ################
#Ho= Averages of diameters of Unit A is equal to Averages of diameters of unit B
#Ha= Averages of diameters of Unit A is not equal to Averages of diameters of unit B

scipy.stats.ttest_ind(Cutlets.UnitA,Cutlets.UnitB)
# p-value = 0.472 > 0.05 p high null fly accept null Hypothesis

#Inference is that there is no significant difference in the diameters of Unit A and Unit B




















   