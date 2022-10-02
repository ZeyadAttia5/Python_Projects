#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output

r1= ['0','1','2']
r2= ['3','4','5']
r3= ['6','7','8']
X = False

def display():
    print(r1)
    print(r2)
    print(r3)

def reset():
    r1= ['0','1','2']
    r2= ['3','4','5']
    r3= ['6','7','8']


# In[2]:


def user_input():
    valid_input = range(0,9)
    digit = False
    while(digit == False):
        user = input("enter the number of the cell that you want to change: ")
        if user.isdigit():
            digit = True
        else:
            print("your input has to be a digit between 0 and 8")
            
        if digit and int(user) in valid_input:
            return int(user)
    return int(user)
    


# In[3]:


def change_turn():
    return not X


# In[4]:


def manipulate_list(index):
    if index in range(0,3):
        if(r1[index] != 'X' and r1[index] != 'O'):
            if(X):
                r1[index] = 'X'
                return
            else:
                r1[index] = 'O'
                return
    elif index in range(3,6):
        if(r2[index-3] != 'X' and r2[index-3] != 'O'):
            if(X):
                r2[index-3] = 'X'
                return
            else:
                r2[index-3] = 'O'
                return
    elif index in range(6,9):
        if(r3[index-6] != 'X' and r3[index-6] != 'O'):
            if(X):
                r3[index-6] = 'X'
                return
            else:
                r3[index-6] = 'O'
                return


# In[5]:


def check_rows():
    if len(set(r1)) == 1:
        return r1[0]
    elif(len(set(r2)) == 1):
         return r2[1]
    elif(len(set(r3)) == 1):
         return r3[0]
    else:
         return False
         
def check_diagonals():
    if(r1[0] == r2[1] == r3[2]):
        return r1[0]
    elif(r1[2] == r2[1] == r3[0]):
         return r3[0]
    else:
         return False
         
def check_col():
    for i in range(0,3):
        if(r1[i] == r2[i] == r3[i]):
             return r1[i]
    return False
         
def check_winner():
    if check_col() != False:
         return check_col()
    elif check_diagonals() != False:
         return check_diagonals()
    elif check_rows() != False:
         return check_rows()
    else:
         return False


# In[6]:


display()
for i in range(0,9):
    if(check_winner() != False):
        print(f"The winner is {check_winner()}")
        break
    c = user_input()
    manipulate_list(c)
    clear_output()
    display()
    X = change_turn()
    if i == 8 and check_winner() == False:
        print("no clear winner")
        i = 0
        reset()
    


# In[ ]:





# In[ ]:




