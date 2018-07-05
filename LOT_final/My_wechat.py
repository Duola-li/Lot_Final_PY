#coding=utf-8
import itchat
from itchat.content import *
import threading
from Context import Context
import os

@itchat.msg_register([TEXT])
def simple_reply(msg):
    print msg['Content']
    if msg['Content'] == 'show':
        if Context.mutex.acquire():
            #加锁，然后设置变量
            Context.getPic = True
            Context.mutex.release()
        i = 0
        while not os.path.exists(Context.picname):
            i = i + 1
            if i >= 5:
                break
            time.sleep(1)
        if i >= 5:
            itchat.send_msg('timeout. try again')
        else:
            itchat.send_image(Context.picname.decode('utf-8'), 'filehelper')
            #!!!!!!删除图片！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
            os.remove(Context.picname)
            
    elif msg['Content'] == 'about':
        itchat.send_msg('微信传感监控器。作者：李阅，滕浩', 'filehelper')
    else:
        itchat.send_msg('无效命令', 'filehelper')

def send_warn(string):
    if not string:
        return
    itchat.send_msg(string, 'filehelper')



def RUN():
    # itchat.auto_login(hotReload=True)
    itchat.run()
