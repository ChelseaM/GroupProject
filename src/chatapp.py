# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatapp.ui'
#
# Created: Sun Apr 24 20:17:53 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(772, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 80, 601, 341))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.frame.setPalette(palette)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.sendMessage_Button = QtGui.QPushButton(self.frame)
        self.sendMessage_Button.setGeometry(QtCore.QRect(20, 300, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.sendMessage_Button.setFont(font)
        self.sendMessage_Button.setObjectName(_fromUtf8("sendMessage_Button"))
        self.clearLogs_Button = QtGui.QPushButton(self.frame)
        self.clearLogs_Button.setGeometry(QtCore.QRect(180, 300, 75, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.clearLogs_Button.setFont(font)
        self.clearLogs_Button.setObjectName(_fromUtf8("clearLogs_Button"))
        self.lineEdit_2 = QtGui.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 249, 541, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.listWidget = QtGui.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(20, 0, 541, 231))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet(_fromUtf8("background-color: white"))
        self.listWidget.setProperty("isWrapping", True)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(19, 30, 601, 41))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.Name_label = QtGui.QLabel(self.frame_3)
        self.Name_label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.Name_label.setFont(font)
        self.Name_label.setObjectName(_fromUtf8("Name_label"))
        self.lineEdit = QtGui.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(60, 10, 191, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.connect_Button = QtGui.QPushButton(self.frame_3)
        self.connect_Button.setGeometry(QtCore.QRect(280, 10, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.connect_Button.setFont(font)
        self.connect_Button.setObjectName(_fromUtf8("connect_Button"))
        self.frame_4 = QtGui.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(640, 30, 120, 391))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.label = QtGui.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(0, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidget_2 = QtGui.QListWidget(self.frame_4)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 60, 101, 321))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu_Actions = QtGui.QMenu(self.menubar)
        self.menuMenu_Actions.setObjectName(_fromUtf8("menuMenu_Actions"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionVersion = QtGui.QAction(MainWindow)
        self.actionVersion.setObjectName(_fromUtf8("actionVersion"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuMenu_Actions.addAction(self.actionVersion)
        self.menuMenu_Actions.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu_Actions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.sendMessage_Button.setText(_translate("MainWindow", "Send Message", None))
        self.clearLogs_Button.setText(_translate("MainWindow", "Clear Logs", None))
        self.Name_label.setText(_translate("MainWindow", "Name:", None))
        self.connect_Button.setText(_translate("MainWindow", "Connect", None))
        self.label.setText(_translate("MainWindow", "Who is Connected:", None))
        self.menuMenu_Actions.setTitle(_translate("MainWindow", "Menu Actions", None))
        self.actionVersion.setText(_translate("MainWindow", "Version", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

