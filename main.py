# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainImg = QtWidgets.QLabel(self.centralwidget)
        self.mainImg.setGeometry(QtCore.QRect(10, 10, 20, 20))
        self.mainImg.setText("")
        self.mainImg.setObjectName("mainImg")
        self.colorPalette = QtWidgets.QLabel(self.centralwidget)
        self.colorPalette.setGeometry(QtCore.QRect(50, 10, 20, 20))
        self.colorPalette.setText("")
        self.colorPalette.setObjectName("colorPalette")
        self.hdr = QtWidgets.QLabel(self.centralwidget)
        self.hdr.setGeometry(QtCore.QRect(10, 50, 20, 20))
        self.hdr.setText("")
        self.hdr.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.hdr.setObjectName("hdr")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOperation = QtWidgets.QMenu(self.menubar)
        self.menuOperation.setObjectName("menuOperation")
        self.menuFilter = QtWidgets.QMenu(self.menuOperation)
        self.menuFilter.setObjectName("menuFilter")
        self.menuCut = QtWidgets.QMenu(self.menuOperation)
        self.menuCut.setObjectName("menuCut")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionRGB = QtWidgets.QAction(MainWindow)
        self.actionRGB.setObjectName("actionRGB")
        self.actionHSI = QtWidgets.QAction(MainWindow)
        self.actionHSI.setObjectName("actionHSI")
        self.actionEnlarge = QtWidgets.QAction(MainWindow)
        self.actionEnlarge.setObjectName("actionEnlarge")
        self.actionShrink = QtWidgets.QAction(MainWindow)
        self.actionShrink.setObjectName("actionShrink")
        self.actionBPSlc = QtWidgets.QAction(MainWindow)
        self.actionBPSlc.setObjectName("actionBPSlc")
        self.actionRotate = QtWidgets.QAction(MainWindow)
        self.actionRotate.setObjectName("actionRotate")
        self.actionCtrStr = QtWidgets.QAction(MainWindow)
        self.actionCtrStr.setObjectName("actionCtrStr")
        self.actionOverlap = QtWidgets.QAction(MainWindow)
        self.actionOverlap.setObjectName("actionOverlap")
        self.actionHistogram = QtWidgets.QAction(MainWindow)
        self.actionHistogram.setObjectName("actionHistogram")
        self.actionNegative = QtWidgets.QAction(MainWindow)
        self.actionNegative.setObjectName("actionNegative")
        self.actionOutlier = QtWidgets.QAction(MainWindow)
        self.actionOutlier.setObjectName("actionOutlier")
        self.actionMedian = QtWidgets.QAction(MainWindow)
        self.actionMedian.setObjectName("actionMedian")
        self.actionLowpass = QtWidgets.QAction(MainWindow)
        self.actionLowpass.setObjectName("actionLowpass")
        self.actionHighpass = QtWidgets.QAction(MainWindow)
        self.actionHighpass.setObjectName("actionHighpass")
        self.actionEdgeCrsp = QtWidgets.QAction(MainWindow)
        self.actionEdgeCrsp.setObjectName("actionEdgeCrsp")
        self.actionHighBoost = QtWidgets.QAction(MainWindow)
        self.actionHighBoost.setObjectName("actionHighBoost")
        self.actionGradient = QtWidgets.QAction(MainWindow)
        self.actionGradient.setObjectName("actionGradient")
        self.actionGray = QtWidgets.QAction(MainWindow)
        self.actionGray.setObjectName("actionGray")
        self.actionThresholding = QtWidgets.QAction(MainWindow)
        self.actionThresholding.setObjectName("actionThresholding")
        self.actionBrightness = QtWidgets.QAction(MainWindow)
        self.actionBrightness.setObjectName("actionBrightness")
        self.actionHistEq = QtWidgets.QAction(MainWindow)
        self.actionHistEq.setObjectName("actionHistEq")
        self.actionHistSpec = QtWidgets.QAction(MainWindow)
        self.actionHistSpec.setObjectName("actionHistSpec")
        self.actionAddNoise = QtWidgets.QAction(MainWindow)
        self.actionAddNoise.setObjectName("actionAddNoise")
        self.actionConnComp = QtWidgets.QAction(MainWindow)
        self.actionConnComp.setObjectName("actionConnComp")
        self.actionHuffman = QtWidgets.QAction(MainWindow)
        self.actionHuffman.setObjectName("actionHuffman")
        self.actionRect = QtWidgets.QAction(MainWindow)
        self.actionRect.setObjectName("actionRect")
        self.actionOval = QtWidgets.QAction(MainWindow)
        self.actionOval.setObjectName("actionOval")
        self.actionMW = QtWidgets.QAction(MainWindow)
        self.actionMW.setObjectName("actionMW")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFilter.addAction(self.actionOutlier)
        self.menuFilter.addAction(self.actionMedian)
        self.menuFilter.addAction(self.actionLowpass)
        self.menuFilter.addAction(self.actionHighpass)
        self.menuFilter.addAction(self.actionEdgeCrsp)
        self.menuFilter.addAction(self.actionHighBoost)
        self.menuFilter.addAction(self.actionGradient)
        self.menuCut.addAction(self.actionRect)
        self.menuCut.addAction(self.actionOval)
        self.menuOperation.addAction(self.actionRGB)
        self.menuOperation.addAction(self.actionHSI)
        self.menuOperation.addAction(self.actionGray)
        self.menuOperation.addAction(self.actionShrink)
        self.menuOperation.addAction(self.actionEnlarge)
        self.menuOperation.addAction(self.actionRotate)
        self.menuOperation.addAction(self.actionBrightness)
        self.menuOperation.addAction(self.menuCut.menuAction())
        self.menuOperation.addAction(self.actionMW)
        self.menuOperation.addAction(self.actionOverlap)
        self.menuOperation.addAction(self.actionHistogram)
        self.menuOperation.addAction(self.actionHistEq)
        self.menuOperation.addAction(self.actionHistSpec)
        self.menuOperation.addAction(self.actionNegative)
        self.menuOperation.addAction(self.actionThresholding)
        self.menuOperation.addAction(self.actionBPSlc)
        self.menuOperation.addAction(self.actionCtrStr)
        self.menuOperation.addAction(self.actionAddNoise)
        self.menuOperation.addAction(self.menuFilter.menuAction())
        self.menuOperation.addAction(self.actionHuffman)
        self.menuOperation.addAction(self.actionConnComp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOperation.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "M103040008"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOperation.setTitle(_translate("MainWindow", "Operation"))
        self.menuFilter.setTitle(_translate("MainWindow", "Filter"))
        self.menuCut.setTitle(_translate("MainWindow", "Cut"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionRGB.setText(_translate("MainWindow", "RGB"))
        self.actionHSI.setText(_translate("MainWindow", "HSI"))
        self.actionEnlarge.setText(_translate("MainWindow", "Enlarge"))
        self.actionShrink.setText(_translate("MainWindow", "Shrink"))
        self.actionBPSlc.setText(_translate("MainWindow", "Bit-plane slicing"))
        self.actionRotate.setText(_translate("MainWindow", "Rotate"))
        self.actionCtrStr.setText(_translate("MainWindow", "Contrast stretching"))
        self.actionOverlap.setText(_translate("MainWindow", "Overlapping"))
        self.actionHistogram.setText(_translate("MainWindow", "Histogram"))
        self.actionNegative.setText(_translate("MainWindow", "Negative"))
        self.actionNegative.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOutlier.setText(_translate("MainWindow", "Outlier"))
        self.actionMedian.setText(_translate("MainWindow", "Median"))
        self.actionLowpass.setText(_translate("MainWindow", "Lowpass"))
        self.actionHighpass.setText(_translate("MainWindow", "Highpass"))
        self.actionEdgeCrsp.setText(_translate("MainWindow", "Edge crispening"))
        self.actionHighBoost.setText(_translate("MainWindow", "High-boost"))
        self.actionGradient.setText(_translate("MainWindow", "Gradient"))
        self.actionGray.setText(_translate("MainWindow", "Gray level"))
        self.actionGray.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionThresholding.setText(_translate("MainWindow", "Thresholding"))
        self.actionBrightness.setText(_translate("MainWindow", "Brightness"))
        self.actionHistEq.setText(_translate("MainWindow", "Histogram equalization"))
        self.actionHistSpec.setText(_translate("MainWindow", "Histogram specification"))
        self.actionAddNoise.setText(_translate("MainWindow", "Add noise"))
        self.actionAddNoise.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionConnComp.setText(_translate("MainWindow", "Connected component"))
        self.actionHuffman.setText(_translate("MainWindow", "Huffman"))
        self.actionRect.setText(_translate("MainWindow", "Rectangle"))
        self.actionOval.setText(_translate("MainWindow", "Ellipse"))
        self.actionMW.setText(_translate("MainWindow", "Magic wand"))
