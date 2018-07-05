#coding:utf-8
import threading
import socket
import serial
import serial.tools.list_ports
from binascii import a2b_hex,b2a_hex
from datetime import datetime
import time
from PyQt5 import QtCore
import matplotlib.pyplot as plt
from matplotlib.widgets import MultiCursor


class common(object):
    """docstring for common"""
    wechat = True  #微信开关
    status = False  #系统开关
    show_status = False
    mutex = threading.Lock()
    com = None
    mysocket = None
    #下面是数据结果，前两个可以不同列表。时间可以不要。
    datalock = threading.Lock()
    timel = []  #时间列表
    warnl = []  #警告
    templ = []  #温度
    wetl  = []  #湿度

    saveflag = False
    file_img = 'D://lot.png'
    falsh_time = 1  #刷新时间，数据获取时间


    #就不close了，没有设置暂定。关闭就是暂停。
    @classmethod
    def getdata(cls):
        try:
            cls.mysocket = MySocket()    
        except Exception as e:
            print(e)
            cls.wechat = False
        else:
            cls.wechat = True
            print('new socket')
        

        if not cls.com:
            cls.com = Com_client('COM3')

        while True:
            if cls.mutex.acquire():
                if not cls.status:
                    cls.mutex.release()
                    cls.s.close()
                    break
                cls.mutex.release()

            re = cls.com.send()
            # Example.Text_deal.appendPlainText(re)
            re = cls.com.r2d_w6000(re)
            # Example.Text_rec.appendPlainText("%s  %s, %f, %f"%re)
            #没有解析，处理数据。发送给请求端。
            print(re)
            cls.warnl.append(re[1])
            cls.templ.append(re[2])
            cls.wetl.append(re[3])
            if cls.wechat and cls.mysocket:
                re2 = cls.mysocket.send(re[1])
                
                #要图片!!!!!!!!!!!!!!!!!!!!
                print(re2)
            else:
                print ('no wechat')




class Com_client(object):
    """串口COM 通信代理类"""
    def __init__(self, com):
        self.port = serial.Serial(port=com, baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=common.falsh_time)

    def close(self):
        self.port.flush()
        self.port.close()

    # 发送指令的完整流程
    def send(self):
        order = '010400000004f1c9'
        order = a2b_hex(order)
        self.port.write(order)
        response = self.port.readall()
        response = b2a_hex(response)
        return response.decode()
 
    def listport(self):
        '''列出当前机器所有可用的串口'''
        plist = list(serial.tools.list_ports.comports())
        # print plist
        if len(plist) <= 0:
            print("Not find port")
        else:
            plist_0 = list(plist[0])
            serialName = plist_0[0]
            print('find port!')
            print(serialName)

    def r2d_w6000(slef, string):
        now = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        if not string:
            print('nothing, use fragilism')
            return (now, '0000', 24.1, 85.2)
        bb = bin(int(string[8], 16))
        bb = '0'*(6-len(bb)) + bb[2:]
        wendu = int(string[14:18], 16) / 10.0
        shidu = int(string[18:22], 16) / 10.0
        ss = (now, bb, wendu, shidu)    #时间， 报警， 温度， 湿度
        return ss

class MyThread_show(QtCore.QThread):
    def run(self):
        fig=plt.figure()
        plt.ion()#开启交互模式
        plt.grid(True)#添加网格线
        plt.minorticks_on()#显示刻度
        plt.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
        plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

        #数据获取
        if common.datalock.acquire():    
            localtime = common.timel
            #common.warnl
            temperature_list = common.templ
            humidity_list = common.wetl
        common.datalock.release()

        first_time = int(localtime[0])
        base = 60
        splitn = 10
        end_time = first_time+base

        ax1=fig.add_subplot(1,1,1)#温度图
        plt.ylim(-10,110)#限制y轴范围

        plt.xlabel('time')
        plt.ylabel('data')
        plt.xlim((first_time, end_time))
        locs, labels = plt.xticks()
        time_locs = [time.strftime('%H:%M:%S',time.localtime(x)) for x in locs]
        plt.xticks(locs, time_locs, rotation=-45)
        print (locs, time_locs,)
        new_loc = False
        while common.show_status:
            try:
                #更新数据
                if common.datalock.acquire():    
                    localtime = common.timel
                    #common.warnl
                    temperature_list = common.templ
                    humidity_list = common.wetl
                common.datalock.release()

                #设置x轴
                if localtime[-1] > end_time or new_loc:#可以换成while
                    if new_loc:
                        first_time = int(localtime[0])
                        end_time = first_time+base
                        new_loc = False
                    else:
                        end_time = end_time+base
                    print('\nnew label')
                    plt.xlabel('time')
                    plt.ylabel('temperature')
                    plt.xlim((first_time, end_time))
                    locs = list( range(first_time, end_time, (end_time-first_time)//splitn) )
                    time_locs = [time.strftime('%H:%M:%S',time.localtime(x)) for x in locs]
                    plt.xticks(locs, time_locs, rotation=-45)
                    print (locs, time_locs,)
                
                # print(temperature_list,localtime)
                ax1.plot(localtime, temperature_list,c='b', label='温度')#画线
                # ax1.scatter(localtime, temperature_list,s=10,c='r')#标记数据点
                ax1.plot(localtime, humidity_list,c='g', label='湿度')#画线
                # ax1.scatter(localtime, humidity_list,s=10,c='r')#标记数据点

                # multi = MultiCursor(fig.canvas,(ax1,),color='r',lw=1, horizOn=True)
                labels = ['温度 max:%f; min:%f'%(max(temperature_list), min(temperature_list)), '湿度 max:%f; min:%f'%(max(temperature_list),min(temperature_list))]
                plt.legend(labels, loc = 1, ncol = 1) 
                if common.saveflag:
                    plt.savefig(common.file_img)
                    print('saved!')
                    common.saveflag = False
                        
            except Exception as e:
                if not localtime:
                    #空
                    new_loc = True
                print(e)
                # raise e
            plt.pause(common.falsh_time)

        print('show over')
        plt.ioff()  
        
class MyThread_getdata(QtCore.QThread):
    #获取数据线程
    updated = QtCore.pyqtSignal(str)
    updated2 = QtCore.pyqtSignal(tuple)

    def run( self ):
        try:
            common.mysocket = MySocket()    
        except Exception as e:
            print(e)
            common.wechat = False
        else:
            common.wechat = True
            print('new socket')

        if not common.com:
            common.com = Com_client('COM3')

        while True:
            if common.mutex.acquire():
                if not common.status:
                    common.mutex.release()
                    if common.mysocket:
                        common.mysocket.close()
                    break
                common.mutex.release()
            re = common.com.send()
            self.updated.emit(re)       #xinhao
            re = common.com.r2d_w6000(re)
            self.updated2.emit(re)       #xinhao
            #没有解析，处理数据。发送给请求端。
            print(re)
            if common.datalock.acquire():    
                common.timel.append(int(time.time()))
                common.warnl.append(re[1])
                common.templ.append(re[2])
                common.wetl.append(re[3])
            common.datalock.release()
            if common.wechat and common.mysocket:
                re2 = common.mysocket.send(re[1])
                ##########
                #要图片!!!!!!!!!!!!!!!!!!!!
                if re2=='pic':
                    print('ready to save picture')
                    common.saveflag = True
                print('we_response:',re2)
            else:
                print ('no wechat')

class MySocket(object):
    """发送报警信息"""
    def __init__(self):    
        HOST='127.0.0.1'
        PORT=4735
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
        self.s.connect((HOST,PORT))       #要连接的IP与端口
        
    def send(self, cmd):
        print('send:', cmd)
        self.s.sendall(cmd.encode())      #把命令发送给对端
        data = self.s.recv(1024)     #把接收的数据定义为变量
        return data.decode()     
    def close(self):
        self.s.close()   
        print('close socket.') 


