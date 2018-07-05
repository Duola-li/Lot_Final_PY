#coding:utf-8
'''
#*-* coding: utf-8 *-*

import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
	prin(msg['Text']) 

itchat.auto_login()
itchat.run()
'''
import requests
import re
import itchat
# from numpy import *
import urllib
import os
from os import system
import time
from PIL import ImageGrab


KEY = 'ea9c72c29cee4acf9e80727c86abb8ab'

def get_response(msg):

    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    
    pattern=re.compile(r'翻译.*')
    if msg['ToUserName'] != 'filehelper':
        
            if '撤回了一条消息' in msg['Content']:
                itchat.send(msg['Text'],'filehelper')  
            #为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
            defaultReply = 'I received: ' + msg['Text']
            #如果图灵Key出现问题，那么reply将会是None
            reply = get_response(msg['Text'])
            print(msg['Text'])
            print(reply)
            #a or b的意思是，如果a有内容，那么返回a，否则返回b
            return reply or defaultReply
    else :
        if msg['Text']=='好友头像':
            friends = itchat.get_friends(update=True)[0:]
            print(type(friends))
            user ='好友头像'
            print(user)
            os.mkdir(user)
            num = 0

            for i in friends:
                img = itchat.get_head_img(userName=i["UserName"])
                fileImage = open(user + "\\" + str(num) + ".jpg",'wb')
                fileImage.write(img)
                fileImage.close()
                num += 1

        elif msg['Text']=='截图':
            t=time.strftime('%Y-%m-%d',time.localtime(time.time()))
            im1=ImageGrab.grab()
            im1.save('1.jpg','jpeg')
            itchat.send("@img@%s" % '1.jpg', 'filehelper')
            # elif msg['Text']=='关闭记事本':
            #os.system('taskkill/F/IM notepad.exe')
        elif msg['Text']=='关机':
            system('"shutdown -s -t 0"')
            send(u'关机成功','filehelper')
        elif pattern.match(msg['Text']):
            defaultReply = '翻译失败'
            #如果图灵Key出现问题，那么reply将会是None
            print(msg['Text'][2:])
            reply = get_response('翻译'+msg['Text'][2:])
            print(msg['Text'])
            print(reply)
            itchat.send(u'翻译结果：'+reply,'filehelper')
            #a or b的意思是，如果a有内容，那么返回a，否则返回b
            return reply or defaultRepl
        elif msg['Text']=='好友男女比例':
            friends = itchat.get_friends(update=True)[0:]

            # 初始化计数器，有男有女，当然，有些人是不填的
            male = female = other = 0

            # 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算
            # 1表示男性，2女性
            for i in friends[1:]:
                sex = i["Sex"]
                if sex == 1:
                    male += 1
                elif sex == 2:
                    female += 1
                else:
                    other += 1

            # 总数算上，好计算比例啊～
            total = len(friends[1:])
            itchat.send('男生：%d  女生：%d  其他：%d'%(male,female,other),'filehelper')
        else :
            itchat.send('等待开发中。。', 'filehelper')

itchat.auto_login(hotReload=True)
itchat.run()
itchat.send('功能展示：\n1.搜索好友头像\n2.截图\n3.关机\n4.翻译**\n5.好友男女比例\n', 'filehelper')