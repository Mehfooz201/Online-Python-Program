#!/usr/bin/env python
# coding: utf-8

# # Assignment#1

# # Question # 1

# In[8]:


print("Twinkle, twinkle, little star,")
print("      How I wonder what you are!")
print("           Up above the world so high,")
print("           Like a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("      How I wonder what you are!")


# # Question # 2
# Write a Python program to get the Python version you are using.

# In[2]:


import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# # Question#3
# Write a Python program to display the current date and time
# 

# In[9]:


import datetime
x = datetime.datetime.now()
print(x)


# # Question#4
# Write a Python program which accepts the radius of a circle from the user and compute the area.

# In[10]:


from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# # Question#5
# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

# In[11]:


fname = input("Input your First Name: ")
lname = input("Input your Last Name :")
fullName = fname+lname
fullName[::-1]


# In[ ]:




