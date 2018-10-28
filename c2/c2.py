#!/usr/bin/env python
# coding: utf-8

# ### Default argument value is evaluated only once in function defination
# ### This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.

# In[2]:


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
print(f)


# In[10]:


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

L = []
print(f(1))
print(f(2))
print(f(3))
print(f)


# **Reference**  
# [4.7.1. Default Argument Values¶](https://docs.python.org/3/tutorial/controlflow.html?highlight=scope)  
# 
# The default values are evaluated at the point of function definition in the defining scope, so that
# ```python
# i = 5
# 
# def f(arg=i):
#     print(arg)
# 
# i = 6
# f()
# # will print 5.
# ```
# 
# Important warning: The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls:
# ```python
# def f(a, L=[]):
#     L.append(a)
#     return L
# 
# print(f(1))
# print(f(2))
# print(f(3))
# # [1]
# # [1, 2]
# # [1, 2, 3]
# ```
# If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
# ```python
# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L
# ```

# In[ ]:




