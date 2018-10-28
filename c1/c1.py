#!/usr/bin/env python
# coding: utf-8

# ### 函数内部引用外部list/dict/set变量可不用`global`关键字声明(要小心)
# ### 函数内部引用外部int/str变量必须用global关键字声明

# In[1]:


a = [0]

def f():
    a.append(1)
    print("in f, a =", a)
    print("in f, id(a) =", id(a))

f()
print("out f, a =", a)
print("out f, id(a) =", id(a))


# In[2]:


a = {}

def f():
    a[0] = 0
    print("in f, a =", a)
    print("in f, id(a) =", id(a))

f()
print("out f, a =", a)
print("out f, id(a) =", id(a))


# In[3]:


a = set()

def f():
    a.add(0)
    print("in f, a =", a)
    print("in f, id(a) =", id(a))

f()
print("out f, a =", a)
print("out f, id(a) =", id(a))


# **Reference**  
# [实例讲解Python中global语句下全局变量的值的修改](https://www.jb51.net/article/86765.htm)

# In[ ]:




