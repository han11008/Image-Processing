# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subMedian.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_subMedian(object):
    def setupUi(self, subMedian):
        subMedian.setObjectName("subMedian")
        subMedian.resize(400, 270)
        self.labelSz = QtWidgets.QLabel(subMedian)
        self.labelSz.setGeometry(QtCore.QRect(10, 10, 85, 17))
        self.labelSz.setObjectName("labelSz")
        self.labelImg = QtWidgets.QLabel(subMedian)
        self.labelImg.setGeometry(QtCore.QRect(160, 20, 20, 20))
        self.labelImg.setText("")
        self.labelImg.setObjectName("labelImg")
        self.spinBox = QtWidgets.QSpinBox(subMedian)
        self.spinBox.setGeometry(QtCore.QRect(95, 7, 45, 25))
        self.spinBox.setMinimum(3)
        self.spinBox.setMaximum(21)
        self.spinBox.setSingleStep(2)
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(subMedian)
        self.pushButton.setGeometry(QtCore.QRect(10, 235, 30, 25))
        self.pushButton.setObjectName("pushButton")
        self.labelSNR = QtWidgets.QLabel(subMedian)
        self.labelSNR.setGeometry(QtCore.QRect(160, 200, 200, 20))
        self.labelSNR.setText("")
        self.labelSNR.setObjectName("labelSNR")
        self.pushButtonWB = QtWidgets.QPushButton(subMedian)
        self.pushButtonWB.setGeometry(QtCore.QRect(160, 220, 80, 20))
        self.pushButtonWB.setObjectName("pushButtonWB")
        self.groupBoxKT = QtWidgets.QGroupBox(subMedian)
        self.groupBoxKT.setGeometry(QtCore.QRect(10, 35, 120, 80))
        self.groupBoxKT.setAutoFillBackground(False)
        self.groupBoxKT.setFlat(False)
        self.groupBoxKT.setObjectName("groupBoxKT")
        self.radioButtonSqr = QtWidgets.QRadioButton(self.groupBoxKT)
        self.radioButtonSqr.setGeometry(QtCore.QRect(10, 25, 100, 25))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/square.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButtonSqr.setIcon(icon)
        self.radioButtonSqr.setAutoExclusive(True)
        self.radioButtonSqr.setObjectName("radioButtonSqr")
        self.radioButtonCrs = QtWidgets.QRadioButton(self.groupBoxKT)
        self.radioButtonCrs.setGeometry(QtCore.QRect(10, 50, 100, 25))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UI/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButtonCrs.setIcon(icon1)
        self.radioButtonCrs.setAutoExclusive(True)
        self.radioButtonCrs.setObjectName("radioButtonCrs")
        self.groupBoxMeth = QtWidgets.QGroupBox(subMedian)
        self.groupBoxMeth.setGeometry(QtCore.QRect(10, 120, 120, 105))
        self.groupBoxMeth.setFlat(False)
        self.groupBoxMeth.setObjectName("groupBoxMeth")
        self.radioButtonM0 = QtWidgets.QRadioButton(self.groupBoxMeth)
        self.radioButtonM0.setGeometry(QtCore.QRect(10, 25, 80, 25))
        self.radioButtonM0.setAutoExclusive(True)
        self.radioButtonM0.setObjectName("radioButtonM0")
        self.radioButtonM1 = QtWidgets.QRadioButton(self.groupBoxMeth)
        self.radioButtonM1.setGeometry(QtCore.QRect(10, 50, 80, 25))
        self.radioButtonM1.setAutoExclusive(True)
        self.radioButtonM1.setObjectName("radioButtonM1")
        self.radioButtonM2 = QtWidgets.QRadioButton(self.groupBoxMeth)
        self.radioButtonM2.setGeometry(QtCore.QRect(10, 75, 80, 25))
        self.radioButtonM2.setAutoExclusive(True)
        self.radioButtonM2.setObjectName("radioButtonM2")

        self.retranslateUi(subMedian)
        QtCore.QMetaObject.connectSlotsByName(subMedian)

    def retranslateUi(self, subMedian):
        _translate = QtCore.QCoreApplication.translate
        subMedian.setWindowTitle(_translate("subMedian", "Median filter"))
        self.labelSz.setText(_translate("subMedian", "Kernel size:"))
        self.pushButton.setText(_translate("subMedian", "OK"))
        self.pushButtonWB.setText(_translate("subMedian", "Write back"))
        self.groupBoxKT.setTitle(_translate("subMedian", "Kernel type:"))
        self.radioButtonSqr.setText(_translate("subMedian", " Square"))
        self.radioButtonCrs.setText(_translate("subMedian", " Cross"))
        self.groupBoxMeth.setTitle(_translate("subMedian", "Method:"))
        self.radioButtonM0.setText(_translate("subMedian", "Median"))
        self.radioButtonM1.setText(_translate("subMedian", "Maxmin"))
        self.radioButtonM2.setText(_translate("subMedian", "Minmax"))
