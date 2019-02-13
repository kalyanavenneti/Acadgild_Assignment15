
# coding: utf-8

# In[4]:


# Question 1: You survey households in your area to find the average rent they are paying. 
# Find the standard deviation from the following data:  1550, 1700,  900, 850,  1000, 950.

import statistics
Rent_list = [1550,1700,900,850,1000,950]

q= statistics.stdev(Rent_list)

print('The standard deviation of the surveyed households is:\n',q)


# In[5]:


# Question 2:  Find the variance for the following set of data representing trees in California 
# (heights in feet): 3, 21, 98, 203, 17, 9

Theight_list =[3,21,98,203,17,9]
a= statistics.variance(Theight_list)
print('The variance for the above set is as below:\n',a)


# In[9]:


# Question 3: In a class on 100 students, 80 students passed in all subjects, 10 failed in one subject, 7 failed in two subjects 
# and 3 failed in three subjects. Find the probability distribution of the variable for number of subjects a student from 
# the given class has failed in.

import numpy as np
import pandas as pd
import scipy.stats as stats

# probability of students passed in all, failed in 1, 2, 3 subjects is presented in the list
list=[0.1,0.03,0.07,0.8] 
df = pd.DataFrame(list)
display(df.describe())


# In[10]:


# for accurate values of mean and Standard deviation multiply by 100

mean = 25.00
std = 36.77

# probability distribution function is calculated as

stats.norm(25.00,36.7786).pdf(80)

