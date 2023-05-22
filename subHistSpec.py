# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subHistSpec.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_subHistSpec(object):
    def setupUi(self, subHistSpec):
        subHistSpec.setObjectName("subHistSpec")
        subHistSpec.resize(400, 300)
        self.scrollArea = QtWidgets.QScrollArea(subHistSpec)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.labelOrigin = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelOrigin.setGeometry(QtCore.QRect(11, 34, 55, 17))
        self.labelOrigin.setObjectName("labelOrigin")
        self.labelSpec = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelSpec.setGeometry(QtCore.QRect(11, 80, 53, 17))
        self.labelSpec.setObjectName("labelSpec")
        self.labelMatch = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelMatch.setGeometry(QtCore.QRect(11, 126, 64, 17))
        self.labelMatch.setObjectName("labelMatch")
        self.label2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label2.setGeometry(QtCore.QRect(147, 57, 89, 17))
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.label0 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label0.setGeometry(QtCore.QRect(11, 57, 72, 17))
        self.label0.setText("")
        self.label0.setObjectName("label0")
        self.label8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label8.setGeometry(QtCore.QRect(147, 149, 89, 17))
        self.label8.setText("")
        self.label8.setObjectName("label8")
        self.label3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label3.setGeometry(QtCore.QRect(11, 103, 72, 17))
        self.label3.setText("")
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label4.setGeometry(QtCore.QRect(89, 103, 52, 17))
        self.label4.setText("")
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label5.setGeometry(QtCore.QRect(147, 103, 89, 17))
        self.label5.setText("")
        self.label5.setObjectName("label5")
        self.label7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label7.setGeometry(QtCore.QRect(89, 149, 52, 17))
        self.label7.setText("")
        self.label7.setObjectName("label7")
        self.label6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label6.setGeometry(QtCore.QRect(11, 149, 72, 17))
        self.label6.setText("")
        self.label6.setObjectName("label6")
        self.label1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label1.setGeometry(QtCore.QRect(89, 57, 52, 17))
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(subHistSpec)
        QtCore.QMetaObject.connectSlotsByName(subHistSpec)

    def retranslateUi(self, subHistSpec):
        _translate = QtCore.QCoreApplication.translate
        subHistSpec.setWindowTitle(_translate("subHistSpec", "Histogram specification"))
        self.labelOrigin.setText(_translate("subHistSpec", "Original"))
        self.labelSpec.setText(_translate("subHistSpec", "Specific"))
        self.labelMatch.setText(_translate("subHistSpec", "Matching"))
