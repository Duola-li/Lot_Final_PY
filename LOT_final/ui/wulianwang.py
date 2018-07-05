# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 15:49:36 2018

@author: th
"""

import matplotlib.pyplot as plt
import random


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

fig=plt.figure()
plt.ion()#开启交互模式
#plt.grid(True)#添加网格线
#plt.minorticks_on()#显示刻度

localtime=['15:06:15','15:06:17','15:06:19','15:06:21','15:06:23','15:06:25'
           ,'15:06:27','15:06:29','15:06:31','15:06:33','15:06:35','15:06:37'
           ,'15:06:40','15:06:42','15:06:44','15:06:46','15:06:48','15:06:50'
           ,'15:06:54','15:06:59','15:07:04','15:07:06','15:07:10','15:07:12'
           ,'15:07:14','15:07:19','15:07:24','15:07:26','15:07:30','15:07:32']#时间数据
temperature_list=random_int_list(0,100,30)#温度数据
#print(temperature_list)
humidity_list=[]#湿度数据
total_list1=[]#温度数据时间列表
total_list2=[]#湿度数据时间列表
locs_to_timelist1=[]#刻度显示列表1
locs_to_timelist2=[]#刻度显示列表2

ax1=fig.add_subplot(1,1,1)#温度图
plt.ylim(0,100)#限制y轴范围
try:
    for amount in range(30):
        #将时间转换成多少秒
        second1=int(localtime[amount][-1])+(int(localtime[amount][-2]))*10
#                 print(second1)
        minute1=(int(localtime[amount][-4])+int(localtime[amount][-5])*10)*60
#                 print(minute1)
        hour1=(int(localtime[amount][-7])+int(localtime[amount][-8])*10)*3600
#                 print(hour1)
        total1=second1+minute1+hour1
        total_list1.append(total1)
#                 print(total_list1)                 
        plt.xlabel('time')
        plt.ylabel('temperature')
         
        if total_list1[amount]>total_list1[0]+40:#只是右边的限制在变
            print('total_list1[amount]',total_list1[amount]+10)
            plt.xlim(total_list1[0],total_list1[amount]+10)
            locs2,label2=plt.xticks()
            print('locs2',locs2)
            for i in range(len(locs2)):
                real_hour2=str(int(locs2[i]//3600)).zfill(2)
#                                 print(real_hour2+'后面')
                real_minute2=str(int((locs2[i]%3600)//60)).zfill(2)
#                                 print(real_minute2+'后面')
                real_second2=str(int(locs2[i]%3600%60)).zfill(2)
#                                 print(real_second2+'后面')
                real_time2=real_hour2+':'+real_minute2+':'+real_second2
#                                 print(real_time2)
                locs_to_timelist2.append(real_time2)
#                         print('locs_to_timelist2',locs_to_timelist2)
                plt.xticks(locs2,locs_to_timelist2,rotation=65)
                # locs_to_timelist2.clear()
        else:       
                    plt.xlim(total_list1[0],total_list1[0]+50)#限制x轴限度
                    locs1,label1=plt.xticks()
                    for i in range(len(locs1)):
                        real_hour1=str(int(locs1[i]//3600)).zfill(2)
#                         print(real_hour1)
                        real_minute1=str(int((locs1[i]%3600)//60)).zfill(2)
#                         print(real_minute1)
                        real_second1=str(int(locs1[i]%3600%60)).zfill(2)
#                         print(real_second1)
                        real_time1=real_hour1+':'+real_minute1+':'+real_second1
                        locs_to_timelist1.append(real_time1)
                        plt.xticks(locs1,locs_to_timelist1,rotation=65)
                        # print(locs1)
                         
                         
        ax1.plot(total_list1[0:amount+1],temperature_list[0:amount+1],c='r')#画线
        ax1.scatter(total_list1[0:amount+1],temperature_list[0:amount+1],s=10,c='b')#标记数据点
                       
        plt.pause(0.5)        
except Exception as err:
        print(err)

#ax2=fig.add_subplot(2,1,2)#湿度图
#plt.ylim(0,10)#限制坐标轴范围

print('结束')
# plt.pause(20)
plt.ioff()
plt.show()

        


        
        
        