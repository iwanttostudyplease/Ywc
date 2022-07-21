# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(930, 648)
        Form.setMinimumSize(QtCore.QSize(930, 648))
        Form.setMaximumSize(QtCore.QSize(930, 648))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/weather.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-image: url(:/login_bak/images/login_bak.png);\n"
"")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(430, 290, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:transparent;\n"
"color: rgb(85, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.edt_username = QtWidgets.QLineEdit(Form)
        self.edt_username.setGeometry(QtCore.QRect(690, 390, 191, 31))
        self.edt_username.setStyleSheet("background:transparent;")
        self.edt_username.setObjectName("edt_username")
        self.edt_password = QtWidgets.QLineEdit(Form)
        self.edt_password.setGeometry(QtCore.QRect(690, 450, 191, 31))
        self.edt_password.setStyleSheet("background:transparent;")
        self.edt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edt_password.setObjectName("edt_password")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(620, 390, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background:transparent;")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(620, 450, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background:transparent;")
        self.label_3.setObjectName("label_3")
        self.label_ewm = QtWidgets.QLabel(Form)
        self.label_ewm.setGeometry(QtCore.QRect(10, 10, 91, 91))
        self.label_ewm.setText("")
        self.label_ewm.setPixmap(QtGui.QPixmap("images/weather_web.png"))
        self.label_ewm.setObjectName("label_ewm")
        self.label_ewmjs = QtWidgets.QLabel(Form)
        self.label_ewmjs.setGeometry(QtCore.QRect(10, 110, 81, 16))
        self.label_ewmjs.setObjectName("label_ewmjs")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(690, 520, 195, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_login = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_login.setStyleSheet("background:transparent;")
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout.addWidget(self.btn_login)
        self.btn_return = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_return.setStyleSheet("background:transparent;")
        self.btn_return.setObjectName("btn_return")
        self.horizontalLayout.addWidget(self.btn_return)
        self.layoutWidget.raise_()
        self.edt_username.raise_()
        self.edt_password.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_ewm.raise_()
        self.label_ewmjs.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录"))
        self.label_2.setText(_translate("Form", "气候查询小工具登录系统"))
        self.edt_username.setPlaceholderText(_translate("Form", "用户名"))
        self.edt_password.setPlaceholderText(_translate("Form", "密码"))
        self.label.setText(_translate("Form", "用户名："))
        self.label_3.setText(_translate("Form", "密码:"))
        self.label_ewmjs.setText(_translate("Form", "中国天气网"))
        self.btn_login.setText(_translate("Form", "登录"))
        self.btn_return.setText(_translate("Form", "退出"))
import images_rc
