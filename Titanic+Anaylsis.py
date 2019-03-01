
# coding: utf-8

# In[1]:


get_ipython().magic('matplotlib inline')

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import unicodecsv


# In[2]:


#makes list of a dictionaries with columns names as keys
#and rows as lists within data in a python setting
#only for practice will use Pandas Dataframe as main source of analysis

def make_list_dict_from_file(file):
    
    list_dict=[]
    
    with open(file,'rb') as f:
        reader=unicodecsv.DictReader(f)
        list_dict=list(reader)
    return list_dict

#makes a 1 dimenisoanl array from a list of dictionaries
#can make 2dimensinal just need to change code to take in arguements of field 
#qty and than loop around same s for interval and make a list and append it to the 
#numpy array
def make_1d_array(storage,fieldname='PassengerId'):
    
    d_list=[]
    for s in storage:
        d_list.append(s[fieldname])
    return np.array(d_list)


def standardize_values(df):
    
    mean=df.mean()
    std=df.std(ddof=1)
    
    return (df-mean)/std


# In[3]:


#how to open csv file for 3 types of data structures
# 1 normal data storage in default python(uses function from above)
# 2 using Numpy as 2d arrays(don't do because numpy arrays require same datatype)
# 3 using Pandas DataFrame

titanic_csv=r'C:\Users\karapet\Desktop\Python Code\Intro_to_Data_Anaylst\Project\titanic_data.csv'

#1
# python_storage= make_list_dict_from_file(titanic_csv)

#2
# tita_array=make_1d_array(python_storage)

#3
tita_df=pd.read_csv(titanic_csv)



tita_std_age=standardize_values(tita_df['Age'])

tita_df.corr(method='pearson',min_periods=1)



# As you can see in the Correlation Table Above no attribute is apperantly correleated  with Survival.
# 
# This should not be mistaken for any of the variables not causing survival, as some were dummy variables and are not shown in the table above.
# 
# But, this does showcase the possibility of none of the following variables having any effect on survival.

# # Survival  Through Age
# 
# We will examine if Age of a passenger caused any benefits for survival on board the Titanic.
# 
# Looking at the count of Survival V. Non-Survival. The amount of deaths was larger in our sample pool than survivors.
# 
# Examining the histogram below, reveals that most passengers were young with a mean age of 30.You may also, see the pattern that all passengers of age 0-10 survived. 
# 
# There is no indication  of age changing the survival rate, as the graphs showcases that there were more deaths in all age groups than survivors.
# 

# In[4]:


#Categorize data for surviving and non_surviving

grouped_survival=tita_df.groupby('Survived')
grouped_survival['Age'].describe()





# In[5]:


ax=grouped_survival['Age'].plot(kind='hist',bins=100,title="Survival Vs Age",legend=True)


# In[6]:


grouped_survival['SibSp'].describe()


# In[7]:


grouped_survival['SibSp'].plot(kind='hist',title='Class Struct V Survival',legend=True)


# In[8]:


grouped_survival['Fare'].describe()


# # Survival with Fare
# 
# Looking at the histogram, the higher fare passengers all seemed to survive. Indicating that paying a premium price, might help you survive upon a disaster.

# In[9]:


grouped_survival['Fare'].plot(kind='hist',bins=100,title='Class Struct V Survival',legend=True)


# # Gender Changes Everything
# 
# The ratio of Survival Changes as you become Female. This is clearly the case as there were less female passengers, but more of them survived than males.
# 
# Also, Female passengers had less deaths than survivors in the overall population of female passengers.
# 
# Males on the other hand, were more likely to die. Being more of the population and having less survivors than the female group.
# 
# This was probably the case, as rules required females to evacuate first than males.

# In[10]:


grouped_survival['Sex'].value_counts().plot(kind='bar')


# In[11]:


grouped_survival.head()
grouped_survival.get_group(0)


# # Fare doesn't matter
# 
# It looks like there was an equal trend of survival, regardless of fare on the lower prices 0-200. But once you reached over 200, there was a 100% survival rate, indicating there was a selection of saving higher paying passengers. 
# 
# 

# In[12]:


import math
def round_up(x):
    return int(math.ceil(x / 100.0)) * 100

def roundup_v2(x):
    return x.round(-2)


tita_df['Fare'].apply(round_up).value_counts().plot(kind='bar')



#grouped_survival['Fare'].apply(roundup_v2).value_counts().plot(kind='bar')

grouped_survival.get_group(1)['Fare'].round(-2).value_counts().plot(kind='bar',title="Survived Group Class Fare Counts")



# In[13]:


grouped_survival.get_group(0)['Fare'].round(-2).value_counts().plot(kind='bar',title="NON-Survived Group Class Fare Counts")

