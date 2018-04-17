
# coding: utf-8

# In[26]:


#To get the male female propotion
import pandas as pd
import matplotlib.pyplot as plt
url='https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
titanic = pd.read_csv(url)
titanic.head()
y=titanic['sex'].value_counts()
Sex= 'Male','Female','Sex'
y.plot(kind='pie',labels=Sex,subplots=True,figsize=(7,7),autopct='%1.1f%%')
plt.title('Male Female Propotion')
plt.legend(title="Sex")
plt.show()


# In[207]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
url='https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
titanic = pd.read_csv(url)
titanic['sex']=titanic['sex'].astype('category')
labels=['Male','Female']
col_map=['Blues','Oranges']
for i in range(2):    
    plt.scatter(titanic['fare'].values,titanic['age'].values,c=titanic['sex'].cat.codes.values,cmap=col_map[i],label=labels[i])
plt.legend()
ax = plt.gca()
legend = ax.get_legend()
legend.legendHandles[0].set_color(plt.cm.Blues(.8))
legend.legendHandles[1].set_color(plt.cm.Oranges(.8))
plt.xlabel("Fare Paid")
plt.ylabel("Age")
plt.title("Fare paid vs Age based on Gender")
plt.show()

