# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdesign.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 314)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 40, 301, 115))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.txt_password = QtWidgets.QLineEdit(self.widget)
        self.txt_password.setObjectName("txt_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_password)
        self.lbl_id = QtWidgets.QLabel(self.widget)
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lbl_id.setObjectName("lbl_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_id)
        self.txt_id = QtWidgets.QLineEdit(self.widget)
        self.txt_id.setObjectName("txt_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_id)
        self.btn_login = QtWidgets.QPushButton(self.widget)
        self.btn_login.setObjectName("btn_login")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.btn_login)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.lbl_password = QtWidgets.QLabel(self.widget)
        self.lbl_password.setObjectName("lbl_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_password)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_id.setText(_translate("MainWindow", "Kullanıcı Adı :"))
        self.btn_login.setText(_translate("MainWindow", "Giriş Yap"))
        self.lbl_password.setText(_translate("MainWindow", "Şifre :"))

