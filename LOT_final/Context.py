#coding:utf-8
import threading

class Context(object):
    """docstring for Context"""
    getPic = False
    mutex = threading.Lock()
    picname = 'D://lot.png'