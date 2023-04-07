# In[27]:


pip install pandas


# In[28]:


import pandas as pd


# In[32]:


Titanic = pd.read_csv('C:\Titanic.csv')


# In[44]:


Titanic.Name.count()


# In[48]:


Titanic.Age.sum()


# In[49]:


Titanic.Age.count()


# In[53]:


Titanic.Age.sum()/Titanic.Age.count()


# In[54]:


Titanic.Ticket.count()


# In[55]:


Titanic.head()


# In[58]:


Titanic.Fare.sum()


# In[61]:


Titanic.Fare.sum()/Titanic.Ticket.count()


# In[66]:


Titanic.Fare.max()


# In[67]:


Titanic.Fare.min()


# In[88]:


Titanic[Titanic.Fare==Titanic.Fare.max()]


# In[93]:


Titanic[Titanic.Sex=='male'].count()


# In[94]:


Titanic[Titanic.Sex=='female'].count()


# In[95]:


Titanic[Titanic.Sex=='male'].Age.sum()


# In[96]:


Titanic[Titanic.Sex=='female'].Age.sum()


# In[98]:


Titanic[Titanic.Sex=='male'].Age.sum()/Titanic[Titanic.Sex=='male'].Sex.count()


# In[99]:


Titanic[Titanic.Sex=='female'].Age.sum()/Titanic[Titanic.Sex=='female'].Sex.count()


# In[102]:


Titanic[Titanic.Survived == 1].count()


# In[104]:


Titanic.Survived.count()/Titanic[Titanic.Survived == 1].count()


# In[105]:


Titanic[Titanic.Survived == 1].count()/Titanic.Survived.count()


# In[106]:


Titanic[Titanic.Survived == 1].Survived.count()/Titanic.Survived.count()


# In[113]:


Titanic.groupby(['Pclass']).mean()


# In[115]:


Titanic.groupby(['Pclass']).Ticket.count()


# In[116]:


Titanic[Titanic.Survived == 1].Survived.count()