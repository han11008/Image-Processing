# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subBPS.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_subBPS(object):
    def setupUi(self, subBPS):
        subBPS.setObjectName("subBPS")
        subBPS.resize(400, 300)
        self.scrollArea = QtWidgets.QScrollArea(subBPS)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 384, 30000))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 30000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label1.setGeometry(QtCore.QRect(50, 60, 40, 20))
        self.label1.setObjectName("label1")
        self.labelImg4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelImg4.setGeometry(QtCore.QRect(110, 110, 20, 20))
        self.labelImg4.setText("")
        self.labelImg4.setObjectName("labelImg4")
        self.label5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label5.setGeometry(QtCore.QRect(40, 90, 40, 20))
        self.label5.setObjectName("label5")
        self.labelImg8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelImg8.setGeometry(QtCore.QRect(0, 150, 20, 20))
        self.labelImg8.setText("")
        self.labelImg8.setObjectName("labelImg8")
        self.label4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label4.setGeometry(QtCore.QRect(0, 90, 40, 20))
        self.label4.setObjectName("label4")
        self.labelImg6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelImg6.setGeometry(QtCore.QRect(130, 130, 20, 20))
        self.labelImg6.setText("")
        self.labelImg6.setObjectName("labelImg6")
        self.labelImg1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelImg1.setGeometry(QtCore.QRect(60, 60, 20, 20))
        self.labelImg1.setText("")
        self.labelImg1.setObjectName("labelImg1")
        self.labelImg2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelImg2.setGeometry(QtCore.QRect(70, 70, 20, 20))
        self.labelImg2.setText("")
        self.labelImg2.setObjectName("labelImg2")
        self.pushButtonWB = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButtonWB.setGeometry(QtCore.QRect(0, 250, 80, 20))
        self.pushButtonWB.setObjectName("pushButtonWB")
        self.label2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label2.setGeometry(QtCore.QRect(90, 60, 40, 20))
        self.label2.setObjectName("label2")
        self.labelImg7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelImg7.setGeometry(QtCore.QRect(140, 140, 20, 20))
        self.labelImg7.setText("")
        self.labelImg7.setObjectName("labelImg7")
        self.label0 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label0.setGeometry(QtCore.QRect(10, 60, 40, 20))
        self.label0.setObjectName("label0")
        self.label3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label3.setGeometry(QtCore.QRect(140, 60, 40, 20))
        self.label3.setObjectName("label3")
        self.labelImg0 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelImg0.setGeometry(QtCore.QRect(0, 70, 20, 20))
        self.labelImg0.setText("")
        self.labelImg0.setObjectName("labelImg0")
        self.labelImg3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelImg3.setGeometry(QtCore.QRect(100, 100, 20, 20))
        self.labelImg3.setText("")
        self.labelImg3.setObjectName("labelImg3")
        self.radioButtonBit = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButtonBit.setGeometry(QtCore.QRect(10, 30, 130, 25))
        self.radioButtonBit.setObjectName("radioButtonBit")
        self.label8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label8.setGeometry(QtCore.QRect(0, 130, 70, 20))
        self.label8.setObjectName("label8")
        self.labelImg5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelImg5.setGeometry(QtCore.QRect(120, 120, 20, 20))
        self.labelImg5.setText("")
        self.labelImg5.setObjectName("labelImg5")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 120, 20))
        self.pushButton.setObjectName("pushButton")
        self.radioButtonGray = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButtonGray.setGeometry(QtCore.QRect(150, 30, 90, 25))
        self.radioButtonGray.setObjectName("radioButtonGray")
        self.label6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label6.setGeometry(QtCore.QRect(80, 90, 40, 20))
        self.label6.setObjectName("label6")
        self.label7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label7.setGeometry(QtCore.QRect(130, 90, 40, 20))
        self.label7.setObjectName("label7")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(subBPS)
        QtCore.QMetaObject.connectSlotsByName(subBPS)

    def retranslateUi(self, subBPS):
        _translate = QtCore.QCoreApplication.translate
        subBPS.setWindowTitle(_translate("subBPS", "Bit-plane slicing"))
        self.label1.setText(_translate("subBPS", "Bit 1"))
        self.label5.setText(_translate("subBPS", "Bit 5"))
        self.label4.setText(_translate("subBPS", "Bit 4"))
        self.pushButtonWB.setText(_translate("subBPS", "Write back"))
        self.label2.setText(_translate("subBPS", "Bit 2"))
        self.label0.setText(_translate("subBPS", "Bit 0"))
        self.label3.setText(_translate("subBPS", "Bit 3"))
        self.radioButtonBit.setText(_translate("subBPS", "Bit-plane slicing"))
        self.label8.setText(_translate("subBPS", "Combine"))
        self.pushButton.setText(_translate("subBPS", "Add watermark"))
        self.radioButtonGray.setText(_translate("subBPS", "Gray code"))
        self.label6.setText(_translate("subBPS", "Bit 6"))
        self.label7.setText(_translate("subBPS", "Bit 7"))
