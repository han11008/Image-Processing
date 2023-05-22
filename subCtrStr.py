# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subCtrStr.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_subCtrStr(object):
    def setupUi(self, subCtrStr):
        subCtrStr.setObjectName("subCtrStr")
        subCtrStr.resize(390, 300)
        self.labelCut = QtWidgets.QLabel(subCtrStr)
        self.labelCut.setGeometry(QtCore.QRect(10, 10, 50, 17))
        self.labelCut.setObjectName("labelCut")
        self.spinBoxCutoff = QtWidgets.QDoubleSpinBox(subCtrStr)
        self.spinBoxCutoff.setGeometry(QtCore.QRect(65, 6, 60, 25))
        self.spinBoxCutoff.setMaximum(49.99)
        self.spinBoxCutoff.setSingleStep(0.01)
        self.spinBoxCutoff.setObjectName("spinBoxCutoff")
        self.labelUB = QtWidgets.QLabel(subCtrStr)
        self.labelUB.setGeometry(QtCore.QRect(10, 45, 100, 17))
        self.labelUB.setObjectName("labelUB")
        self.spinBoxUB = QtWidgets.QSpinBox(subCtrStr)
        self.spinBoxUB.setGeometry(QtCore.QRect(110, 41, 48, 25))
        self.spinBoxUB.setMinimum(1)
        self.spinBoxUB.setMaximum(255)
        self.spinBoxUB.setProperty("value", 255)
        self.spinBoxUB.setObjectName("spinBoxUB")
        self.labelLB = QtWidgets.QLabel(subCtrStr)
        self.labelLB.setGeometry(QtCore.QRect(180, 45, 100, 17))
        self.labelLB.setObjectName("labelLB")
        self.spinBoxLB = QtWidgets.QSpinBox(subCtrStr)
        self.spinBoxLB.setGeometry(QtCore.QRect(280, 41, 48, 25))
        self.spinBoxLB.setMaximum(254)
        self.spinBoxLB.setObjectName("spinBoxLB")
        self.pushButtonOK = QtWidgets.QPushButton(subCtrStr)
        self.pushButtonOK.setGeometry(QtCore.QRect(350, 25, 30, 20))
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.pushButtonWB = QtWidgets.QPushButton(subCtrStr)
        self.pushButtonWB.setGeometry(QtCore.QRect(10, 80, 80, 20))
        self.pushButtonWB.setObjectName("pushButtonWB")
        self.labelImg = QtWidgets.QLabel(subCtrStr)
        self.labelImg.setGeometry(QtCore.QRect(200, 135, 67, 17))
        self.labelImg.setText("")
        self.labelImg.setObjectName("labelImg")
        self.labelOri = QtWidgets.QLabel(subCtrStr)
        self.labelOri.setGeometry(QtCore.QRect(10, 135, 67, 17))
        self.labelOri.setText("")
        self.labelOri.setObjectName("labelOri")
        self.labelL = QtWidgets.QLabel(subCtrStr)
        self.labelL.setGeometry(QtCore.QRect(10, 110, 135, 17))
        self.labelL.setObjectName("labelL")
        self.labelR = QtWidgets.QLabel(subCtrStr)
        self.labelR.setGeometry(QtCore.QRect(200, 110, 135, 17))
        self.labelR.setObjectName("labelR")

        self.retranslateUi(subCtrStr)
        QtCore.QMetaObject.connectSlotsByName(subCtrStr)

    def retranslateUi(self, subCtrStr):
        _translate = QtCore.QCoreApplication.translate
        subCtrStr.setWindowTitle(_translate("subCtrStr", "Contrast stretching"))
        self.labelCut.setText(_translate("subCtrStr", "Cutoff:"))
        self.labelUB.setText(_translate("subCtrStr", "Upper bound:"))
        self.labelLB.setText(_translate("subCtrStr", "Lower bound:"))
        self.pushButtonOK.setText(_translate("subCtrStr", "OK"))
        self.pushButtonWB.setText(_translate("subCtrStr", "Write back"))
        self.labelL.setText(_translate("subCtrStr", "Origin gray level"))
        self.labelR.setText(_translate("subCtrStr", "Contrast stretching"))
