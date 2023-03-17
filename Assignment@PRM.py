#!/usr/bin/env python
# coding: utf-8

# ### You will have a number of elements and in the next n lines element of a list. You have to create a list from the given strings. You have to sort the list based on 2nd last character of a string.

# In[24]:


n = int(input("Enter the number of strings : "))

string_list = []
for i in range(n):
    string_list.append(input("Enter a string : "))
string_list.sort(key=lambda x: x[-2])


print("the sorted list :",string_list)


# ### Your task is to complete the validate_triangle and validate_rectangle functions for the classes. Hint for validating is given in the
# comments of the code. Also you will have to print the following after validation in respective functions:-
# 1.Invalid Triangle: If the triangle sum property of sides is not valid(More hint in the comments of code)
# 2.Valid Triangle: If the triangle sum property of sides is valid.
# 3.Valid Rectangle: If 2 side pairs are same and they are input in correct order like l,b,l,b
# 4.Invalid Rectangle: If Not Valid rectangle as stated above.

# In[23]:


class Triangle:
    
    def __init__(self,L1,L2,L3):
        self.L1=L1
        self.L2=L2
        self.L3=L3
    
    def Validate_Triangle(self):
        if self.L1+self.L2>self.L3 or self.L1+self.L3>self.L2 or self.L2+self.L3>self.L1:
            print("Its a Valid Traingle")
        else:
            print("Its an unvalid Triangle")
        return "" 
            
class Rectangle:
    
    def __init__(self,Length1,Breadth1,Length2,Breadth2):
        self.Length1=Length1
        self.Length2=Length2
        self.Breadth1=Breadth1
        self.Breadth2=Breadth2
    
    def Validate_Rectangle(self):
        if self.Length1==self.Length2 or self.Breadth1==self.Breadth2:
            print("Its a Valid Rectangle")
        else:
            print("Its an unvalid Rectangle")
        return "" 
            
x=Triangle(3,4,5)
print(x.Validate_Triangle())
        
            
y=Rectangle(2,4,2,4)
print(y.Validate_Rectangle())
        


# In[ ]:




