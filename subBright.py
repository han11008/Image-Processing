# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subBright.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_subBright(object):
    def setupUi(self, subBright):
        subBright.setObjectName("subBright")
        subBright.resize(400, 300)
        self.comboBox = QtWidgets.QComboBox(subBright)
        self.comboBox.setGeometry(QtCore.QRect(20, 15, 160, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.labelImg = QtWidgets.QLabel(subBright)
        self.labelImg.setGeometry(QtCore.QRect(20, 80, 20, 20))
        self.labelImg.setText("")
        self.labelImg.setObjectName("labelImg")
        self.label = QtWidgets.QLabel(subBright)
        self.label.setGeometry(QtCore.QRect(20, 50, 60, 20))
        self.label.setObjectName("label")
        self.pushButtonOK = QtWidgets.QPushButton(subBright)
        self.pushButtonOK.setEnabled(False)
        self.pushButtonOK.setGeometry(QtCore.QRect(160, 52, 30, 20))
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.spinBox = QtWidgets.QDoubleSpinBox(subBright)
        self.spinBox.setGeometry(QtCore.QRect(80, 48, 60, 26))
        self.spinBox.setDecimals(2)
        self.spinBox.setMaximum(25.0)
        self.spinBox.setSingleStep(0.01)
        self.spinBox.setProperty("value", 1.0)
        self.spinBox.setObjectName("spinBox")
        self.pushButtonWB = QtWidgets.QPushButton(subBright)
        self.pushButtonWB.setGeometry(QtCore.QRect(20, 260, 80, 20))
        self.pushButtonWB.setObjectName("pushButtonWB")
        self.labelSNR = QtWidgets.QLabel(subBright)
        self.labelSNR.setGeometry(QtCore.QRect(20, 230, 200, 20))
        self.labelSNR.setText("")
        self.labelSNR.setObjectName("labelSNR")

        self.retranslateUi(subBright)
        self.comboBox.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(subBright)

    def retranslateUi(self, subBright):
        _translate = QtCore.QCoreApplication.translate
        subBright.setWindowTitle(_translate("subBright", "Brightness"))
        self.comboBox.setCurrentText(_translate("subBright", "Identity"))
        self.comboBox.setItemText(0, _translate("subBright", "Exponential"))
        self.comboBox.setItemText(1, _translate("subBright", "Gamma correction"))
        self.comboBox.setItemText(2, _translate("subBright", "Identity"))
        self.comboBox.setItemText(3, _translate("subBright", "Inverse"))
        self.comboBox.setItemText(4, _translate("subBright", "Inverse log"))
        self.comboBox.setItemText(5, _translate("subBright", "Log"))
        self.comboBox.setItemText(6, _translate("subBright", "Squared"))
        self.comboBox.setItemText(7, _translate("subBright", "Square root"))
        self.label.setText(_translate("subBright", "Gamma:"))
        self.pushButtonOK.setText(_translate("subBright", "OK"))
        self.pushButtonWB.setText(_translate("subBright", "Write back"))
