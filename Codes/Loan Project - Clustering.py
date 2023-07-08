#!/usr/bin/env python
# coding: utf-8

# # Loan Project - Clustering
# ***

# **Importing the required libraries & packages**

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pyodbc
import os
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
import pickle
import warnings
warnings.filterwarnings('ignore')


# **Changing The Default Working Directory Path**

# In[2]:


os.chdir('C:\\Users\\Shridhar\\Desktop\\Loan Project - Clustering')


# ## Data Reading:

# **Processed the input data using Structured Query Language _(SQL)_ and done some cleaning, with the help of <span style = 'color : red'> pyodbc </span> package connecting Jupyter Notebook with SQL Server in the following 3 cells.**

# In[3]:


server = 'SHRIDHAR\SQLEXPRESS'
db = 'LoanProject'


# In[4]:


conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+db+';UID=Shri; PWD=12345678;Trusted connection=YES')


# In[5]:


sql = 'select * from acc_ord_card_disp_client_dist aocdcd join loan_trans lt on lt.account_id= aocdcd.disposition_account_id'


# **Reading the SQL File using Pandas Command**

# In[6]:


df = pd.read_sql(sql,conn)


# **Exporting the Data after processing in SQL, the final data is converted to Comma Seperated Values _(CSV)_ File**

# In[7]:


df.to_csv('Loan Final Data.csv',index = False)


# ## Exploratory Data Analysis:

# **Checking the Null values of all the columns in the dataset.**

# In[8]:


df.isna().sum()


# **Getting to describe the numerical columns of the dataset**

# In[9]:


df.describe()


# **Getting the information such as counts, datatypes of all the columns in the dataset**

# In[10]:


df.info()


# **Finding the shape of the dataset**

# In[11]:


df.shape


# **Since it has many columns, to extract the columns we need getting all the column names. So, that we can identify the necessary column**

# In[12]:


df.columns


# **Assigning the independent variable with only two columns i.e., `loan_amount`, `balance` since it is Clustering Model there's no dependent variable.**

# In[13]:


x = df[['loan_amount','balance']]


# ## Data Preprocessing:

# **Standardizing the independent variable of the dataset**

# In[14]:


sc = StandardScaler()
sc_x = sc.fit_transform(x)


# **Finding the WCSS (Within Cluster Sum of Square) values using KMeans Clustering Model**

# In[15]:


wcss = []
for i in range(2,15):
    kmeans = KMeans(n_clusters = i, init = 'k-means++')
    kmeans.fit(sc_x)
    wcss.append(kmeans.inertia_)
display(wcss)


# **Plotting the Line Graph with WCSS Values to get the exact ideal number of clusters to be created using KMeans Clustering Algorithm and saving the PNG file of the graph.**

# In[16]:


plt.rcParams['figure.figsize'] = 20,15
plt.plot(range(2,15),wcss)
plt.xlabel('No. of Clusters')
plt.ylabel('WCSS')
plt.title('Elbow Chart')
plt.savefig('Elbow Chart.png')
plt.show()


# **Fitting the KMeans Clustering model with ideal number of clusters found from Elbow Method Graph and getting the dataset belonging to the Cluster.**

# In[17]:


kmeans = KMeans(n_clusters = 6, init = 'k-means++')
kmeans = kmeans.fit(sc_x)
y_kmeans = kmeans.labels_


# **Plotting the Scatter Plot Graph with the independent variable and the Cluster which it belongs and saving the PNG file.**

# In[18]:


plt.scatter(sc_x[y_kmeans==0,0],sc_x[y_kmeans==0,1],s=100,c='r',label='Cluster 1')
plt.scatter(sc_x[y_kmeans==1,0],sc_x[y_kmeans==1,1],s=100,c='b',label='Cluster 2')
plt.scatter(sc_x[y_kmeans==2,0],sc_x[y_kmeans==2,1],s=100,c='g',label='Cluster 3')
plt.scatter(sc_x[y_kmeans==3,0],sc_x[y_kmeans==3,1],s=100,c='c',label='Cluster 4')
plt.scatter(sc_x[y_kmeans==4,0],sc_x[y_kmeans==4,1],s=100,c='m',label='Cluster 5')
plt.scatter(sc_x[y_kmeans==5,0],sc_x[y_kmeans==5,1],s=100,c='k',label='Cluster 6')
plt.title('KMeans Clustering Spread')
plt.savefig('KMeans Clustering Spread.png')
plt.legend()
plt.show()


# **Merging the Cluster Number, adding the sepearte column for it, also getting the `account_id` column from the dataset with assigned independent variable and Adding new column names for the existing columns of the resultant dataset  such as `Account ID`, `Loan Amount`, `Balance`, `Cluster Number` . Displaying the resulting dataset**

# In[19]:


result = pd.concat([df.iloc[:,4], pd.DataFrame(x),pd.DataFrame(y_kmeans)],axis = 1)
result.columns = ['Account ID', 'Loan Amount', 'Balance', 'Cluster Number']
display(result)


# **From the resulting dataset , found that the `Balance` column is Currency value but the readability is much worse since it has many figures after the decimal point. So, rounding off the `Balance` column and updating the rounded value to the `Balance` column in the independent variable and displaying the independent variable after updating.** 

# In[20]:


rounded_balance = round(x['balance'],2)
x.update({'balance': rounded_balance})
display(x)


# **Now again merging the columns just as like before, with updated column names as `Account ID`, `Loan Amount ($)`, `Balance ($)`, `Cluster Number` since we updated the independent variable the readability of all the columns is pretty good**

# In[21]:


result = pd.concat([df.iloc[:,4], pd.DataFrame(x),pd.DataFrame(y_kmeans)],axis = 1)
result.columns = ['Account ID', 'Loan Amount ($)', 'Balance ($)', 'Cluster Number']
display(result)


# **Grouping by the Cluster Number with respect to `Loan Amount ($)` and `Balance ($)` to get the Minimum, Maximum values of Loan Amount, Balance and the number of values in each Clusters.**

# In[22]:


result.groupby('Cluster Number').agg({'Loan Amount ($)':[np.min,np.max],'Balance ($)':[np.min,np.max,np.size]})


# **Loading the pickle file with K-Means Clustering model**

# In[23]:


pickle.dump(kmeans,open('KMeans.pkl','wb'))

