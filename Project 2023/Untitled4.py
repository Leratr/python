#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[2]:


import pandas as pd


# In[9]:


mall = pd.read_csv("C:\\Users\\user\\Desktop\\Python(Бабчёнок О.Ю)\\PythonTasks\\Datasets\\Mall_Customers.csv")

# In[18]:


mall.head()


# In[19]:


mall.tail()


# In[20]:


mall['Genre']


# In[21]:


mall.count()


# In[22]:


mall.Genre.max()


# In[23]:


mall.Genre.min()



# In[25]:


mall.Genre.mean


# In[26]:


mall.groupby('Age').mean()


# In[27]:


import seaborn as sns
import pandas as pd


# In[28]:


mall = pd.read_csv("C:\\Users\\user\\Desktop\\Python(Бабчёнок О.Ю)\\PythonTasks\\Datasets\\Mall_Customers.csv")


# In[29]:


sns.scatterplot(data=Mall_Customers, x = "Genre", y = "Age")


# In[36]:


sns.lineplot(data = Mall_Customers, x = "Annual Income (k$)", y = "Age")


# In[38]:


sns.barplot(data = Mall_Customers, x = "Genre", y = "Annual Income (k$)")


# In[41]:


sns.histplot(x = 'Age', data = Mall_Customers)


# In[46]:


sns.histplot(x ='CustomerID', data = Mall_Customers)


# In[47]:


sns.histplot(x = 'Genre', data = Mall_Customers)


# In[48]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[49]:


data = [80, 20]
labels = ['Female', 'Male']


# In[50]:


colors = sns.color_palette('bright')[ 0:5 ]


# In[51]:


plt.pie(data, labels = labels, colors = colors, autopct = '%.0f%%')
plt.show()

# In[55]:


sns.barplot(data = Mall_Customers, x = 'Genre', y = 'Annual Income (k$)')


# In[57]:


sns.lineplot(data = Mall_Customers, x = 'Age', y = 'Genre')


# In[61]:


sns.lineplot(data = Mall_Customers, y = "Annual Income (k$)", x = "CustomerID")


# In[ ]:




