#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importing numpy
import numpy as np


# In[3]:


#creating an array from list
a = np.array([0,1,2,3])
print(a)


# In[4]:


#creating array of first 10 numbers
print(np.arange(10))


# In[5]:


#1-Dimensional array
a = np.array([0,1,2,3])
print(a)


# In[6]:


#printing dimensions of array
print(a.ndim)


# In[7]:


#printing shape of array
print(a.shape)


# In[8]:


#printing length of array
print(len(a))


# In[9]:


#2-Dimensional array
b = np.array([[0,1,2],[3,4,5]])
print(b)


# In[10]:


#printing dimensional of b
print(b.ndim)


# In[11]:


#printing shape of b
print(b.shape)


# In[12]:


#printing length of b
#returns the size of 1st dimensional 
print(len(b))


# In[13]:


#3-Dimensional array
c = np.array([[[0,1],[2,3]],[[4,5],[6,7]]])
print(c)


# In[14]:


#printing dimensional of c
print(c.ndim)


# In[15]:


#printing shape of c
print(c.shape)


# In[16]:


#printing length of c
print(len(c))


# In[17]:


#creating array with range
a = np.arange(1,10)
print(a)


# In[18]:


#creating array with range with stepsize
a = np.arange(1,10,2) #np.arange(starting_index,end_index,step_size)
print(a)


# In[19]:


#creating array with linspace
b = np.linspace(0,1,6) #np.linspace(starting_index,end_index,number_of_points)
print(b)


# In[22]:


#common Arrays
#Array of ones
a = np.ones((3,3))
print(a)


# In[25]:


#Arrays of zeros
a = np.zeros((3,3))
print(a)


# In[26]:


#Arrays of diagonal
a = np.diag([1,2,3,4])
print(a)


# In[27]:


#Create an array using random
a = np.random.rand(4)
print(a)


# In[28]:


#Returns array with standard normalisation
a = np.random.randn(4)
print(a)


# **The items of an array can be assigned and accessed as same way as other python sequences.**

# In[29]:


#printing 5th element of an array
a = np.arange(10)
print(a[5])


# In[30]:


a = np.diag([1,2,3])
print(a[2,2])


# In[31]:


#assigning value to index
a = np.arange(10)
a[3] = 5
print(a)


# In[36]:


#Slicing
a = np.arange(15)
print(a[1:8:2])  #print(array_name(starting_index:end_index:step_size))


# In[39]:


#we can also combine assignment and slicing operation
a = np.arange(10)
print(a)
a[3:8] = 5
print(a)


# In[43]:


#Element wise operation
#Basic operation 
#Addition
a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a)
print(a+1)

#Subtraction
print(a-1)

#Multiplication
print(a*2)

#Division
print(a/2)


# In[52]:


a = np.array([1,2,3,4,5,6,7,8,9,10])
b = np.array([11,12,13,14,15,16,17,18,19,20])
print("Subtraction of two arrays is :",a-b)
print("Addition of two arrays is :",a+b)
print("Multiplication of two array elementwise :",a*b)
print("Multiplication of two array is:",a.dot(b))
print("Division of two array is :",a/b)
print("power of 2 to the every array element",a**2)


# In[56]:


#Element wise commparison
a = np.array([1,2,3,4,6])
b = np.array([3,4,3,4,5])
print(a==b)
print(a>b)
print(a<b)


# In[58]:


#Array wise comparision
a = np.array([1,2,3,4,5])
b = np.array([3,4,5,6,7])
c = np.array([1,2,3,4,5])
print(np.array_equal(a,b))
print(np.array_equal(a,c))


# In[67]:


#Logical operations
a = np.array([1,1,0,0])
b = np.array([1,0,1,0])
print(np.logical_or(a,b))
print(np.logical_and(a,b))
print(np.logical_xor(a,b))
print(np.logical_not(a))


# In[74]:


#Mathematical Functions
a = np.arange(10)
print("sin value of each element in array:",np.sin(a))
print("cos value of each element in array",np.cos(a))
print("tan value of each element in array",np.tan(a))
print("logarithmic value of each element in array",np.log(a))
print("exponential value of each element in array",np.exp(a))


# In[76]:


#basic reduction
a = np.array([1,2,3,4])
print(a)
print(np.sum(a))


# In[78]:


#sum by rows and by columns
a = np.array([[1,1],[2,2]])
print(a.sum(axis=0))
print(a.sum(axis=1))


# In[80]:


#minimum and maximum
a = np.array([1,2,3])
print(a.min())
print(a.max())
print(a.argmin()) #returns index of minimum element
print(a.argmax()) #returns index of maximum element


# In[81]:


#all and any
print(np.all([True,False,True]))   #returns True if every element is True else returns False
print(np.all([True,True,True]))    #returns True if every element is True else returns False
print(np.any([False,False,False])) #returns True if any of element is True else returns False
print(np.any([True,False,True]))   #returns True if any of element is True else returns False


# In[94]:


#statistics 
a = np.array([1,2,3,4,3,2,4,5,4,3,4,4,4,7])
b = np.array([[1,2,3,4,3,2,1,2,3],[1,2,3,3,4,45,5,6,6]])
print(np.mean(a))
print(np.median(a))
print(np.median(b,axis=1))
print(np.std(a)) 
print(a.std()) #same as np.std(a)


# In[104]:


#broadcasting
a = np.tile(np.arange(0,40,10),(3,1)) #np.tile(np.arange(starting_index,end_index,step_size),(number_of_rows,number_of repetations))
print(a)

