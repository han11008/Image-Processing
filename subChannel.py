# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subChannel.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_subChannel(object):
    def setupUi(self, subChannel):
        subChannel.setObjectName("subChannel")
        subChannel.resize(400, 300)
        subChannel.setWindowTitle("")
        self.label0 = QtWidgets.QLabel(subChannel)
        self.label0.setGeometry(QtCore.QRect(10, 10, 50, 20))
        self.label0.setObjectName("label0")
        self.label1 = QtWidgets.QLabel(subChannel)
        self.label1.setGeometry(QtCore.QRect(80, 10, 50, 20))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(subChannel)
        self.label2.setGeometry(QtCore.QRect(10, 40, 50, 20))
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(subChannel)
        self.label3.setGeometry(QtCore.QRect(80, 40, 50, 20))
        self.label3.setObjectName("label3")
        self.labelImg0 = QtWidgets.QLabel(subChannel)
        self.labelImg0.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.labelImg0.setText("")
        self.labelImg0.setObjectName("labelImg0")
        self.labelImg1 = QtWidgets.QLabel(subChannel)
        self.labelImg1.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.labelImg1.setText("")
        self.labelImg1.setObjectName("labelImg1")
        self.labelImg2 = QtWidgets.QLabel(subChannel)
        self.labelImg2.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.labelImg2.setText("")
        self.labelImg2.setObjectName("labelImg2")
        self.labelImg3 = QtWidgets.QLabel(subChannel)
        self.labelImg3.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.labelImg3.setText("")
        self.labelImg3.setObjectName("labelImg3")

        self.retranslateUi(subChannel)
        QtCore.QMetaObject.connectSlotsByName(subChannel)

    def retranslateUi(self, subChannel):
        _translate = QtCore.QCoreApplication.translate
        self.label0.setText(_translate("subChannel", "Origin"))
        self.label1.setText(_translate("subChannel", "Red"))
        self.label2.setText(_translate("subChannel", "Green"))
        self.label3.setText(_translate("subChannel", "Blue"))
