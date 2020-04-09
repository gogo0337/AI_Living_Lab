#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import pandas as pd
import glob
from filecmp

audio_dir = "C:/Users/fyj/Desktop/test/test" #오디오 리스트의 경로
file_path = "C:/Users/fyj/Desktop/test"
csv_path = open("C:/Users/fyj/Desktop/test/input.csv") #입력할엑셀파일 (.csv로 저장 후 사용)

file_list = glob.glob(file_path+os.sep+"*")
file_name = [file for file in file_list if file.endswith(".csv")]
df=pd.read_csv(file_name[0], encoding='cp949')
temp_df=df[["음성파일", "전사", "시스템인식"]]
new_df=temp_df[(temp_df["전사"]=="1")]
print ("총 개수: ",len(df)," / 지우는 개수 : ",len(new_df), "결과물 개수 : ", len(df)-len(new_df))
temp = new_df["음성파일"].tolist()

print("하기 전: ", len(os.listdir(audio_dir)))
for i in range(len(temp)):
    os.remove(audio_dir+os.sep+temp[i])
print("done")
print("하고난 후: ",len(os.listdir(audio_dir)))

