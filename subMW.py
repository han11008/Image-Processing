# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subMW.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_subMW(object):
    def setupUi(self, subMW):
        subMW.setObjectName("subMW")
        subMW.resize(400, 300)
        self.label = QtWidgets.QLabel(subMW)
        self.label.setGeometry(QtCore.QRect(10, 10, 67, 17))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(subMW)
        QtCore.QMetaObject.connectSlotsByName(subMW)

    def retranslateUi(self, subMW):
        _translate = QtCore.QCoreApplication.translate
        subMW.setWindowTitle(_translate("subMW", "Magic wand"))
