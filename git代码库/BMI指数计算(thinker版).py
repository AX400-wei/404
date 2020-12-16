#!/usr/bin/env python
# coding: utf-8

# In[7]:


import tkinter
import tkinter.messagebox

def msgbox():
#         tkinter.messagebox.showinfo(title="name",message=name.get())
#         tkinter.messagebox.showinfo(title="age",message=age.get())
#         tkinter.messagebox.showinfo(title="weight",message=weight.get())
#         tkinter.messagebox.showinfo(title="height",message=height.get())
         tkinter.messagebox.showinfo(title="status",message=status.get())

root = tkinter.Tk()

button = tkinter.Button(root,text='点击计算你的BMI指数',command=msgbox)
button.place(x=60,y=30,height=30,width=140)

name1 =tkinter.Label(root,text='请输入你的名字:')
name1.place(x=5,y=90,height=30,width=90)

age1 =tkinter.Label(root,text='请输入你的年龄:')
age1.place(x=5,y=130,height=30,width=90)

weight1 =tkinter.Label(root,text='请输入你的体重:')
weight1.place(x=5,y=170,height=30,width=90)

height1 =tkinter.Label(root,text='请输入你的身高:')
height1.place(x=5,y=210,height=30,width=90)

#以上为标签属性设置

name = tkinter.StringVar(root)
entryName = tkinter.Entry(root,width=150,textvariable=name)
entryName.place(x=100,y=90,height=30,width=100)

age = tkinter.StringVar(root)
entryAge= tkinter.Entry(root,width=150,textvariable=age)
entryAge.place(x=100,y=130,height=30,width=100)

weight = tkinter.StringVar(root)
entryWeight = tkinter.Entry(root,width=150,textvariable=weight)
entryWeight.place(x=100,y=170,height=30,width=100)

height = tkinter.StringVar(root)
entryHeight = tkinter.Entry(root,width=150,textvariable=height)
entryHeight.place(x=100,y=210,height=30,width=100)

#以上为输入框属性设置

class BMI:
    def __init__(self,name,age,weight,height,status):
        
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.bmi = self.weight / (self.height * self.height)
        self.status
        
    def get_name(self):
        #print(self.name)
        return self.name
    
    def get_bmi(self):
        return self.bmi
    
    def get_status(self):
        
        if self.bmi < 18.5:
            self.status = ("偏瘦")
            
        else:
            self.status = ("正常")
        return self.status
#bmi1 = BMI(name.get(),age.get(),weight.get(),height.get(),status.get())  #实例化

root.mainloop()


# In[5]:


print(name.get(),age.get(),weight.get(),height.get())


# In[ ]:




