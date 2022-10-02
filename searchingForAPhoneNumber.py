#!/usr/bin/env python
# coding: utf-8

# In[2]:


import shutil


# In[3]:


shutil.unpack_archive('unzip_me_for_instructions.zip', 'extract', 'zip')


# In[4]:


import os
import re


# In[24]:


phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
found_dir = ''
for folder, subfolders, files in os.walk('extracted_content'):

    curr_dir = folder
    for file in files:
        f = open(folder+'\\'+file, 'r')
        match = re.search(phone_pattern, f.readline())
        if match == None:
            f.close()
            continue
        else:
            found_dir = folder+'\\'+file
            print(found_dir)
            print(match)
            f.close()
            break


# In[ ]:





# In[ ]:




