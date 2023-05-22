# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subSingle.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_subSingle(object):
    def setupUi(self, subSingle):
        subSingle.setObjectName("subSingle")
        subSingle.resize(400, 300)
        self.label = QtWidgets.QLabel(subSingle)
        self.label.setGeometry(QtCore.QRect(10, 10, 100, 20))
        self.label.setObjectName("label")
        self.labelImg = QtWidgets.QLabel(subSingle)
        self.labelImg.setGeometry(QtCore.QRect(10, 70, 20, 20))
        self.labelImg.setText("")
        self.labelImg.setObjectName("labelImg")
        self.pushButtonOK = QtWidgets.QPushButton(subSingle)
        self.pushButtonOK.setGeometry(QtCore.QRect(190, 10, 30, 20))
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.pushButtonWB = QtWidgets.QPushButton(subSingle)
        self.pushButtonWB.setGeometry(QtCore.QRect(10, 40, 80, 20))
        self.pushButtonWB.setObjectName("pushButtonWB")
        self.spinBox = QtWidgets.QDoubleSpinBox(subSingle)
        self.spinBox.setGeometry(QtCore.QRect(110, 8, 70, 25))
        self.spinBox.setMaximum(255.0)
        self.spinBox.setSingleStep(1.0)
        self.spinBox.setObjectName("spinBox")
        self.labelSNR = QtWidgets.QLabel(subSingle)
        self.labelSNR.setGeometry(QtCore.QRect(100, 40, 160, 20))
        self.labelSNR.setText("")
        self.labelSNR.setObjectName("labelSNR")

        self.retranslateUi(subSingle)
        QtCore.QMetaObject.connectSlotsByName(subSingle)

    def retranslateUi(self, subSingle):
        _translate = QtCore.QCoreApplication.translate
        subSingle.setWindowTitle(_translate("subSingle", "Outlier"))
        self.label.setText(_translate("subSingle", "Amplification:"))
        self.pushButtonOK.setText(_translate("subSingle", "OK"))
        self.pushButtonWB.setText(_translate("subSingle", "Write back"))
