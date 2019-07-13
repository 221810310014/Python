#!/usr/bin/env python
# coding: utf-8

# lst=[1,5,34,67,123]
# print(lst) # access the total list
# print(lst[0]) #access the first item list
# print(lst[-1]) #access the last item list
# print(lst[-2]) #last second
# print(lst[1:]) #access from one 
# print(lst[1:4]) #access from one to fourth
# 

# In[2]:


lst=[1,5,34,67,123]
print(lst) # access the total list
print(lst[0]) #access the first item list
print(lst[-1]) #access the last item list
print(lst[-2]) #last second
print(lst[1:]) #access from one 
print(lst[1:4]) #access from one to fourth


# In[4]:


# delete a specific item in the list
print(li)
del li[2]
print(li)


# In[5]:


# Basic list operations
lis = [1,5,9,45,85]
print(len(lis)) # length of the list
print(lis*2) # repetation
print(len(lis))
print(9 in lis)
print(15 in lis)
#access the list item using iteration
for x in range(len(lis)):
    print(lis[x],end=" ")


# In[6]:


# Function of the list
lst1=[1,9,6,18,2]
print(min(lst1)) #Min item of the list
print(max(lst1))# max item of the list
print(sum(lst1)) # sum of the all terms in the list
print(sum(lst1)//len(lst1))#Average of the list elements
print(sum(lst1[1::2])/len(lst1[1::2]))#average of all elements


# In[7]:


# Function
# Input :List
# Output : Formatted output
#Test case :
# [1,6,9,4,16,19,22] -- 1 9 19 22 
def linearsearch6(li):
    # Implement the logic
    for x in range(len(li)):
        if x ==0 or x == len(li) - 1:
            print(li[x],end=" ")
        elif li[x-1] % 2 == 0 and li[x+1] % 2 ==0:
            print(li[x],end=" ")
    return
li = [1,6,9,4,16,19,22]
linearsearch6(li) # 1 9 19 22


# In[8]:


#Function
# Input :List
# Output : Formatted output
# Test case :
# [1,2,3,4,5] -- [1,3,8,15,5]
# [6,5,2,8,2] -- [6,12,40,4,2]
def linearsearch5(li):
    for x in range(len(li)):
        if x==0 or x==len(li)-1:
            print(li[x],end=" ")
        else:
            print(li[x-1]*li[x+1],end=" ")
    return
li=[1,2,3,4,5]
linearsearch5(li)


# In[9]:


#Function
# Input :List
# Output : Formatted output
# Test case :
# [1,2,3,4,5] -- [1,3,8,15,5]
# [6,5,2,8,2] -- [6,12,40,4,2]
def linearsearch5(li):
    for x in range(len(li)):
        if x==0 or x==len(li)-1:
            print(li[x],end=" ")
        else:
            print(li[x-1]*li[x+1],end=" ")
    return
li=[1,2,3,4,5]
linearsearch5(li)


# In[10]:


# Function for conversion - 
# Input- number
# Output - list
# 14569 -- [1,4,5,6,9]
# 1990 -- [1,9,9,0]
def numberlistconversion(n):
    li=[]
    while n!=0:
        r=n%10
        li.append(r)
        n=n//10
    li.reverse()
    return li
numberlistconversion(14569)


# In[12]:


# Function to count the occurances of a character in a string
# "Python Programming" ->2
# "Python Programming" ->2
def countcharoccarances(s,c):
    cnt=0
    for ch in s:
        if ch==c:
            cnt +=1
    return cnt
countcharoccarances("Python Programming",'m')


# # contact algorithm
# - add contact
# - search the contact
# - list all contacts
#         - name1: phone1
#         - name2: phone2
# - modify the contact
# - remove the contact
# - import the contact
# 

# In[18]:


# Add contact
contacts = {} # Creating a dict object
def addcontact(name,phone):
    if name not in contacts:
        contacts[name] = phone
        print("contact details are added")
    else:
        print("contact details already exist")
    return
addcontact('eva elfie','5481032973')
addcontact('kimmy granger','5484532973')
addcontact('jasmine james','6969696969')


# In[19]:


# Search for contact details
def searchcontact(name):
    if name in contacts:
        print(name,":",contacts[name])
    else:
        print("%s does not exists"% name)
    return
searchcontact('nike')
searchcontact('harsha')


# In[20]:


# Import some contacts
# Merge contacts with existing contacts
def impcontacts(newcontacts):
    contacts.update(newcontacts)
    print(len(newcontacts.keys()),"Contacts added successfully")
    return
newcontacts={'dinesh':9987456445,'ajay':1475829635}
impcontacts(newcontacts)


# In[21]:


# Add contact
contacts= {}  # creating adict object
def addcontact(name,phone):
    if name not in contacts:
        contacts[name]=phone
        print("contact details are added")
    else:
        print("contact details already exists")
    return
addcontact('nike','9876541230')
addcontact('mahesh','0987654321')
addcontact('nike','9876541230')


# In[1]:


#function to create a file and write a file
def createfile(filename):
    f = open(filename,)


# # Regular expressions
# - pattern matching
# - patterns(re)package
# - [0-9]--> any digit matching
#     >two digit number (^[0-9]{2}$)

# In[1]:


# function to test two digit number match
import re
def twodigitmatch(n):
    pattern='^[0-9]{2}$'
    n=str(n)
    if re.match(pattern,n):
        return True
    return False
print(twodigitmatch(12))   #True
print(twodigitmatch(123))  #False


# # Regular expression for characters
# - [a-z]-->any word in lowercase charcters
# - [A-Z]-->any word in uppercase character
#  - ^[a-z]{5}$-->it accepts 5 lower case characters
#  
#  - ^[a-zA-Z]{8}$-->it accepts 8 chars can be lower and upper
# 
#  - ^[a-zA-Z0-9]{8}$-->accepts 8 chars can be lower ,upper and numbers
# 

# In[2]:


#Function to define to test username having characters
# Upper  case and lower case
def testusername(s):
    pattern ='^[a-zA-Z]{8}$'
    if re.match(pattern,s):
        return True
    return False
print(testusername('GITamhyD')) #true
print(testusername('gitAM746')) #false


# # similarly (^[a-zA-Z@#!]{6,15}$) for validate password
# # Email id validation using regular expression
# # Example:-username@domainname.extension
# user name:-
#   - length will be[6-15]
#   - No special chars apart from underscore(_)
#   - chars set :all digits and lowercase
# domainname:-
#   - length will be[3-18]
#   - no spl chars
#   - char set-all digits and lower case
# extension:-
#   - length will be[2-4]
#   - no spl chars
#   - char set:lower case chars

# In[3]:


import re
def emailidvalidation(email):
    pattern='^[a-z0-9][a-z0-9_.]{5,14}[@][a-z0-9]{3,18}[.][a-z]{2,4}$'
    if re.match(pattern,email):
        return True
    return False
print(emailidvalidation('229898@gmail.com'))


# In[ ]:


# draw a line backward
import turtle as tt
a1=tt.Turtle()
tt.backward(100)
tt.done()


# In[3]:


# Draw a square
import turtle as tt
a1=tt.Turtle()
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
tt.done()


# In[ ]:


import turtle as tt
a1=tt.Turtle()
a1.backward(150)
a1.right(90) # can use left also
a1.backward(150)
a1.right(90)
a1.backward(150)
a1.right(90)
a1.backward(150)
a1.right(90)
tt.done()


# In[2]:


# Spiraling square
import turtle as t
a1=t.Turtle()
a1.pencolor('blue')
for i in range(250):
    a1.forward(i)
    a1.left(91)
t.done()


# In[1]:


# Spiraling hexagon
from turtle import *
colors=['blue','green','yellow','orange','purple','red']
for x in range(360):
    pencolor(colors[x%6])
    width(x/100+1)
    forward(x)
    left(59)
#draw a line
# Step1: make all the turtle package to be imported
import turtle
# turtle method creates and returns a new object
a1=turtle.Turtle()
#Forward()method moves 100 pixels
turtle.forward(250)
# we are done
turtle.done()


# # 1. RECTANGLE
# # SQUARE
# # CIRCLE
# # FILL THE COLORS IN RECTANGLE AN CIRCLE
# 

# In[3]:


# learning over a range of numbers - Traditional apporach
for i in [0,1,2,3,4,5]:
    print(i**2,end=" ")


# In[4]:


# idiomatic programming
for i in range(6):
    print(i**2,end=" ")


# # Looping over a collection

# In[5]:


colors=['red','green','yellow','purple']
for i in range (len(colors)):
    print(colors[i],end=" ")


# In[6]:


for color in colors:
    print(color,end=" ")


# 
# # Looping backwards

# In[7]:


colors=['red','green','yellow','purple']
for i in range (len(colors)-1,-1,-1):
    print(colors[i],end=" ")


# In[8]:


for color in reversed(colors):
    print(color,end=" ")


# # pandas

# In[10]:


import pandas as pd


# In[11]:


dt = {'Id' : [11,12,13,14,15],
     'first name' :['A', 'B','C','D','E'],
     'company':['aa','bb','cc','dd','ee'],
     'address': ['Hyd','Hyd','Hyd','Hyd','Hyd']}
mydt = pd.DataFrame(dt)


# In[12]:


print(mydt)


# In[13]:


color=['red','green','yellow','purple']
for color in sorted (colors):
    print(color,end=" ")


# In[14]:


color=['red','green','yellow','purple']
for color in sorted (colors,reverse=True):
    print(color,end=" ")


# In[ ]:




