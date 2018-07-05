# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import random
import time
from matplotlib.widgets import MultiCursor

def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

fig=plt.figure()
plt.ion()#开启交互模式
plt.grid(True)#添加网格线
plt.minorticks_on()#显示刻度
plt.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


localtime=['15:06:15','15:06:17','15:06:19','15:06:21','15:06:23','15:06:25'
           ,'15:06:27','15:06:29','15:06:31','15:06:33','15:06:35','15:06:37'
           ,'15:06:40','15:06:42','15:06:44','15:06:46','15:06:48','15:06:50'
           ,'15:06:54','15:06:59','15:07:04','15:07:06','15:07:10','15:07:12'
           ,'15:07:14','15:07:19','15:07:24','15:07:26','15:07:30','15:07:32']#时间数据

localtime = list(range(100, 1100, 3)[0:30])
print(len(localtime))


first_time = int(localtime[0])
base = 50
splitn = 10
end_time = first_time+base

temperature_list=random_int_list(0,100,30)#温度数据
humidity_list=random_int_list(0,100,30)#湿度数据


ax1=fig.add_subplot(1,1,1)#温度图
plt.ylim(-10,110)#限制y轴范围

plt.xlabel('time')
plt.ylabel('temperature')
plt.xlim((first_time, end_time))
locs, labels = plt.xticks()
time_locs = [time.strftime('%H:%M:%S',time.localtime(x)) for x in locs]
plt.xticks(locs, time_locs, rotation=-45)
print (locs, time_locs,)

try:
    for amount in range(30):
        #设置x轴
        if localtime[amount] > end_time:#可以换成while
            end_time = end_time+base
            print('new label')
            plt.xlabel('time')
            plt.ylabel('temperature')
            plt.xlim((first_time, end_time))
            locs = list( range(first_time, end_time, (end_time-first_time)//splitn) )
            time_locs = [time.strftime('%H:%M:%S',time.localtime(x)) for x in locs]
            plt.xticks(locs, time_locs, rotation=-45)
            print (locs, time_locs,)
        
        # print(temperature_list[0:amount+1],localtime[0:amount+1])
        ax1.plot(localtime[0:amount+1], temperature_list[0:amount+1],c='b', label='温度')#画线
        ax1.scatter(localtime[0:amount+1], temperature_list[0:amount+1],s=10,c='r')#标记数据点
        ax1.plot(localtime[0:amount+1], humidity_list[0:amount+1],c='g', label='湿度')#画线
        ax1.scatter(localtime[0:amount+1], humidity_list[0:amount+1],s=10,c='r')#标记数据点

        multi = MultiCursor(fig.canvas,(ax1,),color='r',lw=1, horizOn=True)
        labels = ['温度 max:%f; min:%f'%(max(temperature_list[0:amount+1]), min(temperature_list[0:amount+1])), '湿度 max:%f; min:%f'%(max(temperature_list),min(temperature_list))]
        plt.legend(labels, loc = 1, ncol = 1) 
        if amount == 10 or amount == 29:
            plt.savefig('D:\lot.png')
        plt.pause(0.1)        
except Exception as e:
    print(e)
    raise e

#ax2=fig.add_subplot(2,1,2)#湿度图
#plt.ylim(0,10)#限制坐标轴范围

print('over')
plt.pause(10)
plt.ioff()

        


        
        
        