#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[2]:


import numpy as np
array1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array1.reshape(2,5) # convert a 1D into 2D array


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[3]:


a1 = np.arange(0,10).reshape(2,5)
b1 = np.ones((2,5),dtype=int).reshape(2,5)
np.vstack((a1,b1))


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[5]:


a1 = np.arange(0,10).reshape(2,5)
b2 = np.ones((2,5),dtype=int).reshape(2,5)
np.hstack((a1,b1)) # stack two arrays horizontally


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[6]:


a = np.array([0,1,2,3,4,5,6,7,8,9,]).reshape(5,2)
np.ravel(a) # convert an arrays into a flat 1d array


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[18]:


a1 = np.arange(0,15).reshape(5,3)
a1 = np.arange(0,15).reshape(1,15) #convert higher dimention into one dimension
a1


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[20]:


a1 = np.arange(0,15)
a1.ravel() # conversion of one dimension to higher dimension


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[31]:


a1 = np.arange(4,29).reshape(5,5)
a1
np.square(a1) #cal the square of an array


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[37]:


a1 = np.arange(4,34).reshape(5,6)
a1.mean() # cal the mean of array 


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[38]:


a1.std() # cal the standard deviation of the previous array in Q8


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[39]:


np.median(a1) # cal the median of the previous array in Q8


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[40]:


a1.transpose() # transpose of the previous array in Q8


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[41]:


a2 = np.random.randn(4,4) # created 4X4 array
a2.diagonal() # this statement cal the diagonal elements of array


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[42]:


np.linalg.det(a2) # find the determinant of the a2 variable


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[53]:


a3 = np.arange(100).reshape(25,4)
a3
np.percentile (a3, 5, axis=None, out=None) # find the 5th percentile of an array


# In[52]:


a3 = np.arange(100).reshape(25,4)
a3
np.percentile (a3, 95, axis=None, out=None) # find the 95th percentile of an array


# ## Question:15

# ### How to find if a given array has any null values?

# In[61]:


a4 = np.array([50,np.NaN,80,45,85,np.NaN,97,23,0,12])
a4
np.isnan(a4) # find the null values s boolean True


# In[63]:


a4


# In[ ]:




