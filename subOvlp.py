# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subOvlp.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_subOvlp(object):
    def setupUi(self, subOvlp):
        subOvlp.setObjectName("subOvlp")
        subOvlp.resize(400, 300)
        self.pushButtonAdd = QtWidgets.QPushButton(subOvlp)
        self.pushButtonAdd.setGeometry(QtCore.QRect(10, 10, 130, 25))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.labelAlpha = QtWidgets.QLabel(subOvlp)
        self.labelAlpha.setGeometry(QtCore.QRect(160, 12, 50, 20))
        self.labelAlpha.setObjectName("labelAlpha")
        self.spinBox = QtWidgets.QDoubleSpinBox(subOvlp)
        self.spinBox.setGeometry(QtCore.QRect(210, 10, 60, 26))
        self.spinBox.setMaximum(1.0)
        self.spinBox.setSingleStep(0.01)
        self.spinBox.setObjectName("spinBox")
        self.pushButtonOK = QtWidgets.QPushButton(subOvlp)
        self.pushButtonOK.setGeometry(QtCore.QRect(280, 12, 30, 20))
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.labelUpperImg = QtWidgets.QLabel(subOvlp)
        self.labelUpperImg.setGeometry(QtCore.QRect(20, 50, 20, 20))
        self.labelUpperImg.setText("")
        self.labelUpperImg.setObjectName("labelUpperImg")
        self.labelImg = QtWidgets.QLabel(subOvlp)
        self.labelImg.setGeometry(QtCore.QRect(80, 50, 20, 20))
        self.labelImg.setText("")
        self.labelImg.setObjectName("labelImg")

        self.retranslateUi(subOvlp)
        QtCore.QMetaObject.connectSlotsByName(subOvlp)

    def retranslateUi(self, subOvlp):
        _translate = QtCore.QCoreApplication.translate
        subOvlp.setWindowTitle(_translate("subOvlp", "Overlapping"))
        self.pushButtonAdd.setText(_translate("subOvlp", "Add upper image"))
        self.labelAlpha.setText(_translate("subOvlp", "Alpha:"))
        self.pushButtonOK.setText(_translate("subOvlp", "OK"))
