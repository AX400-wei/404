#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#打开PyCharm，新建一个新的py文件，取名demo，生成demo.py文件
lines_maxlenth = 0      #定义新的变量，储存最长的代码长度
line_numbers = 1        #每次加一，代表当前正在添行号的位置
code_in = open("demo.py","r").readlines()   #打开demo.py文件，读取所有内容
code_out = open("demo_new.py", "w")         #将内容写入pycharm创建的新的文件demo_new.py中
for i in code_in:                          #循环开始，目的：寻找每行字段最长的一行
    if(lines_maxlenth < len(i)):
        lines_maxlenth = len(i)
for i in code_in:                          #新的循环，目的：在最后添加行号，并对齐
    i = i.ljust(lines_maxlenth+1).replace('\n','') + "#" + str(line_numbers) + "\n"
    line_numbers += 1
    code_out.write(i)

