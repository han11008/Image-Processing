# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subHfm.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_subHfm(object):
    def setupUi(self, subHfm):
        subHfm.setObjectName("subHfm")
        subHfm.resize(460, 350)
        self.tableView = QtWidgets.QTableView(subHfm)
        self.tableView.setGeometry(QtCore.QRect(10, 40, 320, 300))
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setVisible(False)
        self.label = QtWidgets.QLabel(subHfm)
        self.label.setGeometry(QtCore.QRect(10, 10, 200, 17))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(subHfm)
        self.pushButton.setGeometry(QtCore.QRect(350, 10, 90, 20))
        self.pushButton.setObjectName("pushButton")
        self.labelImg = QtWidgets.QLabel(subHfm)
        self.labelImg.setGeometry(QtCore.QRect(350, 40, 67, 17))
        self.labelImg.setText("")
        self.labelImg.setObjectName("labelImg")

        self.retranslateUi(subHfm)
        QtCore.QMetaObject.connectSlotsByName(subHfm)

    def retranslateUi(self, subHfm):
        _translate = QtCore.QCoreApplication.translate
        subHfm.setWindowTitle(_translate("subHfm", "Huffman"))
        self.label.setText(_translate("subHfm", "Compression ratio:"))
        self.pushButton.setText(_translate("subHfm", "Decompress"))
