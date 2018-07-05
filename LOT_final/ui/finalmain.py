# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\final1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication
import sys
import r1_rc
from time import sleep
import time
from common import *
# import threading

class BtnLabel(QtWidgets.QLabel):  
    def __init__(self,parent=None):  
        super(BtnLabel,self).__init__(parent)  
 
    def mousePressEvent(self,e):  
        print ('mousePressEvent(%d,%d)\n'%(e.pos().x(),e.pos().y()))
        if not common.mysocket:
            print('not ready')
            return
        common.mysocket.send('1111')

 
class Example(QMainWindow):
    # Text_deal = None
    # Text_rec = None
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        self.setObjectName("MainWindow")
        self.resize(963, 561)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.Box_config = QtWidgets.QGroupBox(self.centralwidget)
        self.Box_config.setGeometry(QtCore.QRect(20, 30, 161, 221))
        self.Box_config.setObjectName("Box_config")
        self.label = QtWidgets.QLabel(self.Box_config)
        self.label.setGeometry(QtCore.QRect(10, 20, 54, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Box_config)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 54, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Box_config)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 54, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Box_config)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 54, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Port = QtWidgets.QSpinBox(self.Box_config)
        self.Port.setGeometry(QtCore.QRect(80, 60, 61, 22))
        self.Port.setMaximum(65535)
        self.Port.setProperty("value", 9600)
        self.Port.setObjectName("Port")
        self.Protocal = QtWidgets.QComboBox(self.Box_config)
        self.Protocal.setGeometry(QtCore.QRect(80, 20, 61, 22))
        self.Protocal.setObjectName("Protocal")
        self.Protocal.addItem("")
        self.Protocal.addItem("")
        self.Protocal.addItem("")
        self.Protocal.addItem("")
        self.Port_3 = QtWidgets.QSpinBox(self.Box_config)
        self.Port_3.setGeometry(QtCore.QRect(80, 100, 61, 22))
        self.Port_3.setMinimum(1)
        self.Port_3.setMaximum(64)
        self.Port_3.setProperty("value", 8)
        self.Port_3.setDisplayIntegerBase(10)
        self.Port_3.setObjectName("Port_3")
        self.Protocal_2 = QtWidgets.QComboBox(self.Box_config)
        self.Protocal_2.setGeometry(QtCore.QRect(80, 140, 61, 22))
        self.Protocal_2.setObjectName("Protocal_2")
        self.Protocal_2.addItem("")
        self.label_5 = QtWidgets.QLabel(self.Box_config)
        self.label_5.setGeometry(QtCore.QRect(10, 180, 54, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Protocal_3 = QtWidgets.QComboBox(self.Box_config)
        self.Protocal_3.setGeometry(QtCore.QRect(80, 180, 61, 22))
        self.Protocal_3.setObjectName("Protocal_3")
        self.Protocal_3.addItem("")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(200, 10, 751, 511))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Box_recive = QtWidgets.QGroupBox(self.tab)
        self.Box_recive.setGeometry(QtCore.QRect(20, 20, 711, 221))
        self.Box_recive.setObjectName("Box_recive")
        self.Text_rec = QtWidgets.QPlainTextEdit(self.Box_recive)
        self.Text_rec.setGeometry(QtCore.QRect(10, 20, 681, 181))
        self.Text_rec.setObjectName("Text_rec")
        self.Box_recive_2 = QtWidgets.QGroupBox(self.tab)
        self.Box_recive_2.setGeometry(QtCore.QRect(20, 260, 711, 211))
        self.Box_recive_2.setObjectName("Box_recive_2")
        self.Text_deal = QtWidgets.QPlainTextEdit(self.Box_recive_2)
        self.Text_deal.setGeometry(QtCore.QRect(10, 20, 681, 171))
        self.Text_deal.setObjectName("Text_deal")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView.setGeometry(QtCore.QRect(40, 100, 191, 121))
        self.graphicsView.setObjectName("graphicsView")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(300, 40, 401, 401))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab_2, "")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 270, 161, 141))
        self.groupBox.setObjectName("groupBox")
        self.Button_clear = QtWidgets.QPushButton(self.groupBox)
        self.Button_clear.setGeometry(QtCore.QRect(40, 60, 91, 23))
        self.Button_clear.setObjectName("Button_clear")
        self.Button_fig = QtWidgets.QPushButton(self.groupBox)
        self.Button_fig.setGeometry(QtCore.QRect(40, 100, 91, 23))
        self.Button_fig.setCheckable(True)
        self.Button_fig.setObjectName("Button_fig")
        self.Button_Begin = QtWidgets.QPushButton(self.groupBox)
        self.Button_Begin.setGeometry(QtCore.QRect(40, 20, 91, 23))
        self.Button_Begin.setCheckable(True)
        self.Button_Begin.setObjectName("Button_Begin")
        # self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6 = BtnLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 430, 161, 91))
        self.label_6.setObjectName("label_6")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self._thread = MyThread_getdata(self)
        self._thread.updated.connect(self.update_rec)
        self._thread.updated2.connect(self.update_deal)

        self.retranslateUi()
        self.Myaction()

        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setWindowTitle('物联网数据采集器')
        # self.setWindowIcon(QtGui.QIcon('win.png'))
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Box_config.setTitle(_translate("MainWindow", "配置"))
        self.label.setText(_translate("MainWindow", "串口号："))
        self.label_2.setText(_translate("MainWindow", "波特率："))
        self.label_3.setText(_translate("MainWindow", "数据位："))
        self.label_4.setText(_translate("MainWindow", "校验位："))
        self.Protocal.setItemText(0, _translate("MainWindow", "COM3"))
        self.Protocal.setItemText(1, _translate("MainWindow", "COM4"))
        self.Protocal.setItemText(2, _translate("MainWindow", "COM5"))
        self.Protocal.setItemText(3, _translate("MainWindow", "COM6"))
        self.Protocal_2.setItemText(0, _translate("MainWindow", "NONE"))
        self.label_5.setText(_translate("MainWindow", "停止位："))
        self.Protocal_3.setItemText(0, _translate("MainWindow", "1"))
        self.Box_recive.setTitle(_translate("MainWindow", "接收数据"))
        self.Box_recive_2.setTitle(_translate("MainWindow", "解析结果"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">滕浩：21170211093</span></p>\n"
        "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">李阅（Octan3）：21170211058</span></p>\n"
        "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Email:Octan3@stu.ouc.edu.cn</span></p>\n"
        "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/ouc/1.png\" /></p>\n"
        "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
        "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
        "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.groupBox.setTitle(_translate("MainWindow", "操作"))
        self.Button_clear.setText(_translate("MainWindow", "清除数据"))
        self.Button_fig.setText(_translate("MainWindow", "图表分析"))
        self.Button_Begin.setText(_translate("MainWindow", "开始监听"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ouc/1.png\"/></p></body></html>"))

    def Myaction(self):
        self.Button_Begin.clicked[bool].connect(self.begin)
        self.Button_fig.clicked.connect(self.fig)
        self.Button_clear.clicked.connect(self.clear)
        # self.label_6.mousePressEvent.connect(self.testwarn)#没有信号

    def begin(self, pressed):
        #开始关闭
        if pressed: #如果按下的，参数不可变，连接县城
            self.Button_Begin.setText(u'断开连接')
            self.statusbar.showMessage(u'开始工作')
            if common.mutex.acquire():
                common.status = True    ##控制量!!
                common.mutex.release()
            # temp = threading.Thread(target=self.getdata)
            # temp.start()
            
            self._thread.start()
            # flag = False
            # self.Button_clear.setEnabled(flag)
            # self.Button_fig.setEnabled(flag)

        else:
            if common.mutex.acquire():
                common.status = False
                common.mutex.release()
            # flag = True
            # self.Button_clear.setEnabled(flag)
            # self.Button_fig.setEnabled(flag)
            self.Button_Begin.setText(u'开始监听')
            self.statusbar.showMessage('成功断开')
            ll = self.Text_deal.toPlainText()
            f = open('lot.txt', 'w')
            f.writelines(ll)
            f.close()
        
        


    def clear(self):
        self.Text_deal.clear()
        self.Text_rec.clear()
        if common.datalock.acquire():  
            common.timel = []  #时间列表
            common.warnl = []  #警告
            common.templ = []  #温度
            common.wetl  = []  #湿度
        common.datalock.release()
        self.statusbar.showMessage('clear success')

    def fig(self, pressed):
        if pressed: #如果按下的，参数不可变，连接县城
            self.Button_fig.setText(u'结束分析')
            self.statusbar.showMessage('show fig')
            common.show_status = True
            self._thread2 = MyThread_show()
            self._thread2.start()
        else:
            self.Button_fig.setText(u'图表分析')
            self.statusbar.showMessage('stop show fig')
            common.show_status = False
        
    def update_rec(self, re):
            self.Text_rec.appendPlainText(re)

    def update_deal(self, re):
            self.Text_deal.appendPlainText("%s  %s, %f, %f"%re)
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())