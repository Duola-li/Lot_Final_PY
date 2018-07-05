#coding:utf-8
import socket
import time
import random
HOST='127.0.0.1'
PORT=4735
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
s.connect((HOST,PORT))       #要连接的IP与端口
while 1:
    # cmd = random.choice('abcdefghij')
    # print 'send:', cmd
    cmd=input("Please input cmd:") 
    print ('send:', cmd)
    s.sendall(cmd.encode())      #把命令发送给对端
    data=s.recv(1024)     #把接收的数据定义为变量
    print (data)         #输出变量
    time.sleep(1)
s.close()   #关闭连接