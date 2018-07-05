#coding:utf-8
import socket   #socket模块
import threading
from Context import Context
from My_wechat import * #RUN, send_warn
from datetime import datetime
        

def run():
    '''运行监听服务，开启微信，'''

    #微信登陆线程
    itchat.auto_login(hotReload=True)
    t =threading.Thread(target=RUN)
    t.start()

    #监听数据服务
    HOST='127.0.0.1'
    PORT=4735
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #定义socket类型，网络通信，TCP
    s.bind((HOST,PORT))   #套接字绑定的IP与端口
    s.listen(1)         #开始TCP监听,监听1个请求
      
    while 1:
        print '\n\nSystem start. Waiting for connect...\n'    
        conn,addr=s.accept()   #接受TCP连接，并返回新的套接字与IP地址
        print 'Connected by',addr    #输出客户端的IP地址
        while 1:
            try:
                data=conn.recv(1024)    #把接收的数据实例化
            except Exception as e:
                print e
                print 'lose connected.'
                break   #丢失链接，跳出循环，开始新的链接
            print 'get:',data
            try:
                temp = threading.Thread(target=analisys_data,args=(data,))
                temp.start()
            except Exception as e:
                print 'data error.'
            re = getresponce(data)
            conn.sendall(re)
        conn.close()     #关闭连接

def analisys_data(string):
    #就4位0000
    if len(string) != 4:
        print 'error data:%s.'%string
        return 
    now = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    if string[0] == '1':
        send_warn('%s 警报：烟感异常！'%(now))
    if string[1] == '1':
        send_warn('%s 警报：火感异常！'%(now))
    if string[2] == '1':
        send_warn('%s 警报：非法闯入！'%(now))
    if string[3] == '1':
        send_warn('%s 警报：水浸异常！'%(now))

def getresponce(string):
    responce = 'ok'
    if Context.mutex.acquire():
        #加锁，然后设置变量
        if Context.getPic:
            responce = 'pic'
            Context.getPic = False
        Context.mutex.release()
    return responce

if __name__ == '__main__':
    run()