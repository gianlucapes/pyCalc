#!/usr/bin/env python
# coding: utf-8

# In[35]:


def addition () :
    print("Add")
    number=float(input("Enter a number "))
    answer=number
    while number != 0:
        number=float(input("Enter another number (0 for calculate the sum)..."))
        answer+=number
        if number!=0 :
            print("Current Sum = "+str(answer))
    print("Final Sum = "+str(answer))


# In[34]:


addition()


# In[29]:


def substraction () :
    print("Sub")
    number=float(input("Enter a number "))
    answer=number
    while number != 0:
        number=float(input("Enter another number (0 for calculate the difference)..."))
        answer-=number
        if number!=0 :
            print("Current Difference = "+str(answer))
    print("Final Difference = "+str(answer))


# In[30]:


substraction ()


# In[40]:


def moltiplication () :
    print("Molt")
    number=float(input("Enter a number "))
    answer=number
    while number != 0 and number != 1:
        number=float(input("Enter another number (1 for calculate the product)..."))
        answer*=number
        if number!=1 :
            print("Current Product = "+str(answer))
    print("Final Product = "+str(answer))


# In[42]:


moltiplication ()


# In[48]:


def division () :
    print("Div")
    number=float(input("Enter a number "))
    answer=number
    while number != 0 and number != 1:
        number=float(input("Enter another number (1 for calculate the quotient)..."))
        if number==0:
            answer="infinite"
        else:
            answer/=number
            if number!=1 :
                print("Current Raport = "+str(answer))
    print("Final Raport = "+str(answer))


# In[50]:


division ()


# In[ ]:




