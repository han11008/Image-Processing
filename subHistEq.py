# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subHistEq.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_subHistEq(object):
    def setupUi(self, subHistEq):
        subHistEq.setObjectName("subHistEq")
        subHistEq.resize(400, 300)
        self.scrollArea = QtWidgets.QScrollArea(subHistEq)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.labelEqHist = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelEqHist.setGeometry(QtCore.QRect(100, 50, 67, 17))
        self.labelEqHist.setText("")
        self.labelEqHist.setObjectName("labelEqHist")
        self.labelImg = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelImg.setGeometry(QtCore.QRect(20, 20, 67, 17))
        self.labelImg.setText("")
        self.labelImg.setObjectName("labelImg")
        self.labelHist = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelHist.setGeometry(QtCore.QRect(100, 20, 67, 17))
        self.labelHist.setText("")
        self.labelHist.setObjectName("labelHist")
        self.labelEq = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelEq.setGeometry(QtCore.QRect(20, 50, 67, 17))
        self.labelEq.setText("")
        self.labelEq.setObjectName("labelEq")
        self.labelEqCumu = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelEqCumu.setGeometry(QtCore.QRect(180, 50, 67, 17))
        self.labelEqCumu.setText("")
        self.labelEqCumu.setObjectName("labelEqCumu")
        self.labelCumu = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelCumu.setGeometry(QtCore.QRect(180, 20, 67, 17))
        self.labelCumu.setText("")
        self.labelCumu.setObjectName("labelCumu")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(subHistEq)
        QtCore.QMetaObject.connectSlotsByName(subHistEq)

    def retranslateUi(self, subHistEq):
        _translate = QtCore.QCoreApplication.translate
        subHistEq.setWindowTitle(_translate("subHistEq", "Histogram equalization"))
