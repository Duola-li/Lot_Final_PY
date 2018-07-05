# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:03:02 2018

@author: th
"""

import matplotlib.pyplot as plt
import numpy as np
import time
import random

def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

    
#plt.close()  #clf() # 清图  cla() # 清坐标轴 close() # 关窗口
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
#ax.axis("equal") #设置图像显示的时候XY轴比例
plt.grid(True) #添加网格
plt.ion()  #interactive mode on
plt.minorticks_on()
#plt.xlim(0,86400)
#plt.xlim(44500,44550)
plt.ylim(0,100)
obsx=random_int_list(0,100,200)
#obsy=[2,5,17,65,106,203,1000,2100]
print('开始仿真')
zonglist=[]
print(obsx[0:1])
#print(obsx[0:3])
#print((2**obsx[0:3]+39)/4)

try:
    for i in range(35):
        localtime = time.asctime(time.localtime(time.time()))
        print(1)
        miao=int(localtime[-6])+(int(localtime[-7]))*10
        fen=(int(localtime[-9])+int(localtime[-10])*10)*60
        hour=(int(localtime[-12])+int(localtime[-13])*10)*3600
        zong=hour+fen+miao
        zonglist.append(zong)
        print(2)

#        print("本地时间为 :", localtime))
#        print(2**obsx[0:i+1]) 
        plt.xlim(zonglist[0],zonglist[0]+30)
        ax.plot(zonglist[0:i+1],obsx[0:i+1],color='r')
        ax.scatter(zonglist[0:i+1],obsx[0:i+1],s=50,c='b')
        print(3)
        if zonglist[i]>zonglist[0]+30:
                print(4)
                plt.xlim(zonglist[0],zonglist[i]+10)
        #ax.lines.pop(1)  删除轨迹
        #下面的图,两船的距离
        print(5)
        plt.pause(1.3)
        print(6)
#        plt.close() 
except Exception as err:
    print(err)