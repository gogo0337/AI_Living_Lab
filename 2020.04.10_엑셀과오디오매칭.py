#!/usr/bin/env python
# coding: utf-8

# In[235]:


import os
import pandas as pd
import glob

dir_path=os.path.expanduser('~')
file_path = dir_path+os.sep+"Desktop"+os.sep+"test"
audio_dir = file_path+os.sep+"audio"
file_list = glob.glob(file_path+os.sep+"*")
file_name = [file for file in file_list if file.endswith(".csv")]
file_name


# In[231]:


df=pd.read_csv(file_name[0], encoding='cp949')
df.head()


# In[232]:


temp_df=df[[df.columns[len(df.columns)-3], df.columns[len(df.columns)-2], df.columns[len(df.columns)-1]]]
temp_df


# In[233]:


temp_index = temp_df.columns[0]
temp_index


# In[234]:


new_list=[]
i=0
if len(temp_df[temp_index][0]) > 18:
    for i in range(len(temp_df)):
        new_list.append(temp_df[temp_index][i][len(temp_df[temp_index][i])-18:len(temp_df[temp_index][i])])     
    
    temp_df['new']=new_list
    new_df=temp_df[(temp_df[temp_df.columns[1]]=="1")]

    #기본 columns=0
    #음성파일에 쓰레기값있으면 columns=3
    temp = new_df[new_df.columns[3]].tolist()

    #삭제 시작
    print ("쓰레기값 있을때")
    print("하기 전: ", len(os.listdir(audio_dir)))
    for i in range(len(temp)):
        os.remove(audio_dir+os.sep+temp[i])
    print("done")

    
else:    
    new_df=temp_df[(temp_df[temp_df.columns[1]]=="1")]

    #기본 columns=0
    #음성파일에 쓰레기값있으면 columns=3
    temp = new_df[new_df.columns[0]].tolist()

    #삭제 시작
    print ("쓰레기값 없을때")
    print("하기 전: ", len(os.listdir(audio_dir)))
    for i in range(len(temp)):
        os.remove(audio_dir+os.sep+temp[i])
    print("done")

print("하고난 후: ",len(os.listdir(audio_dir)))

