# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subHist.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_subHist(object):
    def setupUi(self, subHist):
        subHist.setObjectName("subHist")
        subHist.resize(400, 300)
        self.labelRGB = QtWidgets.QLabel(subHist)
        self.labelRGB.setGeometry(QtCore.QRect(10, 10, 67, 17))
        self.labelRGB.setText("")
        self.labelRGB.setObjectName("labelRGB")
        self.labelGray = QtWidgets.QLabel(subHist)
        self.labelGray.setGeometry(QtCore.QRect(100, 10, 67, 17))
        self.labelGray.setText("")
        self.labelGray.setObjectName("labelGray")

        self.retranslateUi(subHist)
        QtCore.QMetaObject.connectSlotsByName(subHist)

    def retranslateUi(self, subHist):
        _translate = QtCore.QCoreApplication.translate
        subHist.setWindowTitle(_translate("subHist", "Histogram"))
