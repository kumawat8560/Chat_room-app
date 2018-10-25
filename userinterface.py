# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userinterface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import socket 
import threading



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=10001
#uname=input('enter the username:')
#ip=input('enter the ip address::')
#s.connect((ip,port))
#s.send(uname.encode('ascii'))
clientRunning=True

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
       

class Ui_MainWindow(object):
    
    def conn(self):
        
        uname = self.userName.text()
        ip = self.ipAddr.text()
        s.connect((ip,port))
        s.send(uname.encode('ascii'))

        def receiveMsg(sock):
                serverDown=False
                while clientRunning and (not serverDown):
                    try:
                        msg=sock.recv(1024).decode('ascii')
                        self.textEdit.append(msg)
                    except:
                        print('server is down.You are now diconnected.press enter to exit.')
                        serverDown=True
        threading.Thread(target=receiveMsg,args=(s,)).start()  

    def display(self):
        uname = self.userName.text()
        clientRunning=True
        mssg = self.msgInput.text()
        self.textEdit.append(mssg)
        msg='< '+uname+' > '+mssg
        if '#quit' in msg:
            clientRunning=False
            s.send('#quit'.encode('ascii'))
        else:
            s.send(msg.encode('ascii'))




                






    def setupUi(self, MainWindow):




        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(688, 487)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.userName = QtGui.QLineEdit(self.centralwidget)
        self.userName.setObjectName(_fromUtf8("userName"))
        
        self.gridLayout.addWidget(self.userName, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.ipAddr = QtGui.QLineEdit(self.centralwidget)
        self.ipAddr.setObjectName(_fromUtf8("ipAddr"))
        
        self.gridLayout.addWidget(self.ipAddr, 0, 3, 1, 1)
        self.conBtn = QtGui.QPushButton(self.centralwidget)
        self.conBtn.setObjectName(_fromUtf8("conBtn"))
        self.conBtn.clicked.connect(self.conn)
        self.gridLayout.addWidget(self.conBtn, 0, 4, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 5)
        self.msgInput = QtGui.QLineEdit(self.centralwidget)
        self.msgInput.setObjectName(_fromUtf8("msgInput"))
        self.msgInput.returnPressed.connect(self.display)
        self.gridLayout.addWidget(self.msgInput, 2, 0, 1, 4)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.display)
        self.gridLayout.addWidget(self.pushButton, 2, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        
        MainWindow.setWindowTitle(_translate("MainWindow","chatroom", None))
        self.label.setText(_translate("MainWindow", "Username", None))
        self.label_2.setText(_translate("MainWindow", "IP Address", None))
        self.conBtn.setText(_translate("MainWindow", "connect", None))
        self.pushButton.setText(_translate("MainWindow", "Send", None))



    
        
        












if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

