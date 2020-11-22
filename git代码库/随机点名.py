#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 创建一个字典student，key是学号，value是姓名
# 学生信息在student.csv文件里，从文件中读取并保存到字典
# 打开student.csv文件

file = open(r'E:\学习文件夹\人工班名单csv.csv','r')


# In[2]:


# 读取文件内容
lines = file.readlines()


# In[3]:


# 抽取每行的学号和姓名，保存到字典
students = {}
for line in lines:
    tmp_list = line.split(',')
    xuehao = tmp_list[0]
    xingming = tmp_list[2]
    students[xuehao] = xingming
print(students)


# In[4]:


# 从学号中随机抽取N个学号
import random
num = int(input("请输入你要抽取的人数："))
# 如何把字典中的key（学号）抽取成列表
xuehao_list = random.sample(students.keys(),num)
xuehao_list


# In[5]:


# 根据随机的学号，打印输出对应的姓名
for xuehao in xuehao_list:
    print(students[xuehao])


# In[ ]:




