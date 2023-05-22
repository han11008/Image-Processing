# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subCut.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_subCut(object):
    def setupUi(self, subCut):
        subCut.setObjectName("subCut")
        subCut.resize(400, 300)
        self.labelCut = QtWidgets.QLabel(subCut)
        self.labelCut.setGeometry(QtCore.QRect(100, 40, 67, 17))
        self.labelCut.setText("")
        self.labelCut.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelCut.setObjectName("labelCut")

        self.retranslateUi(subCut)
        QtCore.QMetaObject.connectSlotsByName(subCut)

    def retranslateUi(self, subCut):
        _translate = QtCore.QCoreApplication.translate
        subCut.setWindowTitle(_translate("subCut", "Cut"))
