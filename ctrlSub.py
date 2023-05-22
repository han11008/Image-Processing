from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage, QPixmap, QStandardItem, QStandardItemModel, QPainter, QBrush, QColor
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PIL import Image
import pcx, bmp, func, cmprs
import numpy as np

from subChannel import Ui_subChannel
from sub2cmp import Ui_sub2cmp
from subBright import Ui_subBright
from subBPS import Ui_subBPS
from subOvlp import Ui_subOvlp
from subHist import Ui_subHist
from subHistEq import Ui_subHistEq
from subHistSpec import Ui_subHistSpec
from subMedian import Ui_subMedian
from subMean import Ui_subMean
from subSingle import Ui_subSingle
from subEdgeCrsp import Ui_subEdgeCrsp
from subGrad import Ui_subGrad
from subCtrStr import Ui_subCtrStr
from subHfm import Ui_subHfm
from subCut import Ui_subCut
from subMW import Ui_subMW

class subCut_controller(QtWidgets.QWidget):		
	def __init__(self, op, img):
		super().__init__()
		self.ui = Ui_subCut()
		self.ui.setupUi(self)
		self.img = img
		self.methType = op
		w, h = func.sz(self.img)
		self.ui.labelCut.setGeometry(QtCore.QRect(10+w+10, 10, w, h))
		self.setMouseTracking(True)
		self.startPos = QtCore.QPoint(0, 0)
		self.endPos = QtCore.QPoint(0, 0)
		self.mousePressEvent = self.msPress
		self.mouseMoveEvent = self.msMove
		self.mouseReleaseEvent = self.msRelease
		self.resize(10+w+10+w+10, 10+h+10)
	
	def paintEvent(self, event):
		w, h = func.sz(self.img)
		d = func.dim(self.img)
		if d == 3:
			imgFormat = QImage.Format_RGB888
		else:
			imgFormat = QImgae.Format_Grayscale8
		qimg = QPixmap.fromImage(QImage(self.img, w, h, w * d, imgFormat))
		pt = QPainter(self)
		pt.drawPixmap(QtCore.QRect(10, 10, w, h), qimg)
		pt.setBrush(QColor(255, 0, 0, 70))
		pt.setPen(QColor(255, 0, 0, 0))
		if self.methType == 0:
			pt.drawRect(QtCore.QRect(self.startPos, self.endPos))
		elif self.methType == 1:
			pt.drawEllipse(QtCore.QRect(self.startPos, self.endPos))
		pt.end()
	
	def msPress(self, event):
		self.startPos = event.pos()
		self.endPos = event.pos()
		self.update()
	
	def msMove(self, event):
		if event.buttons() and QtCore.Qt.LeftButton:
			if event.pos() != self.endPos:
				self.endPos = event.pos()
				self.update()

	def msRelease(self, event):
		self.endPos = event.pos()
		self.update()
		self.cutoff()

	def cutoff(self):
		w, h = func.sz(self.img)
		sx = self.startPos.x() - 10; sx = max(min(w-1, sx), 0)
		sy = self.startPos.y() - 10; sy = max(min(h-1, sy), 0)
		ex = self.endPos.x() - 10; ex = max(min(w-1, ex), 0)
		ey = self.endPos.y() - 10; ey = max(min(h-1, ey), 0)
		if self.methType == 0:
			img = func.cutRect(self.img, sx, sy, ex, ey)
			w, h = func.sz(img)
			d = func.dim(img)
			if d == 3:
				imgFormat = QImage.Format_RGB888
			else:
				imgFormat = QImgae.Format_Grayscale8
			qimg = QImage(img, w, h, w * d, imgFormat)
		elif self.methType == 1:
			img = func.cutElps(self.img, sx, sy, ex, ey)
			w, h = func.sz(img)
			qimg = QImage(img, w, h, w * 4, QImage.Format_RGBA8888)
		self.ui.labelCut.setPixmap(QPixmap.fromImage(qimg))

class subMW_controller(QtWidgets.QWidget):		
	def __init__(self, img):
		super().__init__()
		self.ui = Ui_subMW()
		self.ui.setupUi(self)
		self.img = img
		w, h = func.sz(self.img)
		d = func.dim(self.img)
		if d == 3:
			imgFormat = QImage.Format_RGB888
		else:
			imgFormat = QImgae.Format_Grayscale8
		qimg = QImage(self.img, w, h, w * d, imgFormat)
		self.ui.label.setPixmap(QPixmap.fromImage(qimg))
		self.ui.label.setGeometry(QtCore.QRect(10, 10, w, h))
		self.ui.label.setMouseTracking(True)
		self.ui.label.mousePressEvent = self.msPress
		self.resize(10+w+10, 10+h+10)
	
	def msPress(self, event):
		sx = event.pos().x(); sy = event.pos().y()
		self.img = func.copyPaste(self.img, sx, sy)
		w, h = func.sz(self.img)
		d = func.dim(self.img)
		if d == 3:
			imgFormat = QImage.Format_RGB888
		else:
			imgFormat = QImgae.Format_Grayscale8
		qimg = QImage(self.img, w, h, w * d, imgFormat)
		self.ui.label.setPixmap(QPixmap.fromImage(qimg))

class subChannel_controller(QtWidgets.QWidget):
	def __init__(self, op, img):
		super().__init__()
		self.ui = Ui_subChannel()
		self.ui.setupUi(self)
		if op == 0:
			imgR, imgG, imgB = func.img2rgb(img)
			self.setWindowTitle('RGB')
			w, h = func.sz(img)
			self.qimg = QImage(img, w, h, w * 3, QImage.Format_RGB888)
			self.ui.labelImg0.setGeometry(QtCore.QRect(10, 40, w, h))
			self.ui.labelImg0.setPixmap(QPixmap.fromImage(self.qimg))
			self.qimgR = QImage(imgR, w, h, w * 3, QImage.Format_RGB888)
			self.ui.label1.setGeometry(QtCore.QRect(10+w+20, 10, 50, 20))
			self.ui.labelImg1.setGeometry(QtCore.QRect(10+w+20, 40, w, h))
			self.ui.labelImg1.setPixmap(QPixmap.fromImage(self.qimgR))
			self.qimgG = QImage(imgG, w, h, w * 3, QImage.Format_RGB888)
			self.ui.label2.setGeometry(QtCore.QRect(10, 40+h+20, 50, 20))
			self.ui.labelImg2.setGeometry(QtCore.QRect(10, 40+h+50, w, h))
			self.ui.labelImg2.setPixmap(QPixmap.fromImage(self.qimgG))
			self.qimgB = QImage(imgB, w, h, w * 3, QImage.Format_RGB888)
			self.ui.label3.setGeometry(QtCore.QRect(10+w+20, 40+h+20, 50, 20))
			self.ui.labelImg3.setGeometry(QtCore.QRect(10+w+20, 40+h+50, w, h))
			self.ui.labelImg3.setPixmap(QPixmap.fromImage(self.qimgB))
			self.resize(10+w+20+w+10, 40+h+50+h+10)
		elif op == 1:
			w, h = func.sz(img)
			imgH, imgS, imgI = func.img2hsi(img)
			self.qimg = QImage(img, w, h, w * 3, QImage.Format_RGB888)
			self.setWindowTitle('HSI')
			self.ui.labelImg0.setGeometry(QtCore.QRect(10, 40, w, h))
			self.ui.labelImg0.setPixmap(QPixmap.fromImage(self.qimg))
			self.qimgH = QImage(imgH, w, h, w, QImage.Format_Grayscale8)
			self.ui.label1.setText('Hue')
			self.ui.label1.setGeometry(QtCore.QRect(10+w+20, 10, 100, 20))
			self.ui.labelImg1.setGeometry(QtCore.QRect(10+w+20, 40, w, h))
			self.ui.labelImg1.setPixmap(QPixmap.fromImage(self.qimgH))
			self.qimgS = QImage(imgS, w, h, w, QImage.Format_Grayscale8)
			self.ui.label2.setText('Saturation')
			self.ui.label2.setGeometry(QtCore.QRect(10, 40+h+20, 100, 20))
			self.ui.labelImg2.setGeometry(QtCore.QRect(10, 40+h+50, w, h))
			self.ui.labelImg2.setPixmap(QPixmap.fromImage(self.qimgS))
			self.qimgI = QImage(imgI, w, h, w, QImage.Format_Grayscale8)
			self.ui.label3.setText('Intensity')
			self.ui.label3.setGeometry(QtCore.QRect(10+w+20, 40+h+20, 100, 20))
			self.ui.labelImg3.setGeometry(QtCore.QRect(10+w+20, 40+h+50, w, h))
			self.ui.labelImg3.setPixmap(QPixmap.fromImage(self.qimgI))
			self.resize(10+w+20+w+10, 40+h+50+h+10)

class sub2cmp_controller(QtWidgets.QWidget):
	status_signal = pyqtSignal(np.ndarray)
	def __init__(self, op, img):
		super().__init__()
		self.ui = Ui_sub2cmp()
		self.ui.setupUi(self)
		self.ui.pushButton1.clicked.connect(lambda: self.wb(0))
		self.ui.pushButton2.clicked.connect(lambda: self.wb(1))
		self.ui.pushButtonOK.clicked.connect(self.update)
		self.processType = op
		self.img = img
		w, h = func.sz(img)
		dim = func.dim(img)
		if op == 3:
			thres = func.otsu(img)
			img = func.bimg(img, thres)
			dim = 1
		if dim == 3:
			imgFormat = QImage.Format_RGB888
		else:
			imgFormat = QImage.Format_Grayscale8
		self.img1 = img
		self.qimg1 = QImage(self.img1, w, h, w * dim, imgFormat)
		self.ui.labelImg1.setGeometry(QtCore.QRect(20, 90, w, h))
		self.ui.labelImg1.setPixmap(QPixmap.fromImage(self.qimg1))
		self.img2 = img
		self.qimg2 = QImage(self.img2, w, h, w * dim, imgFormat)
		self.ui.labelImg2.setGeometry(QtCore.QRect(20+w+20, 90, w, h))
		self.ui.labelImg2.setPixmap(QPixmap.fromImage(self.qimg2))
		self.ui.label2.setGeometry(QtCore.QRect(20+w+20, 60, 100, 20))
		self.ui.pushButton2.setGeometry(QtCore.QRect(20+w+20+100, 58, 80, 24))
		self.resize(20+w+20+w+20, 90+h+10)
		self.ui.scrollArea.resize(20+w+20+w+20, 90+h+10)
		self.ui.scrollAreaWidgetContents.resize(20+w+20+w+20, 90+h+10)
		if op == 0:
			self.setWindowTitle('Enlarge')
		elif op == 1:
			self.setWindowTitle('Shrink')
			self.ui.label1.setText('Decimation')
			self.ui.label2.setText('Average')
		elif op == 2:
			self.setWindowTitle('Rotate')
			self.ui.label1.setText('Forward')
			self.ui.label2.setText('Backward')
			self.ui.labelSpinBox.setText('Degree:')
			self.ui.spinBox.setGeometry(QtCore.QRect(85, 10, 60, 30))
			self.ui.spinBox.setMinimum(-360)
			self.ui.spinBox.setMaximum(360)
			self.ui.spinBox.setValue(0)
			self.ui.pushButtonOK.setGeometry(QtCore.QRect(160, 15, 30, 20))
		elif op == 3:
			self.setWindowTitle('Binary')
			self.ui.label1.setText('Manual')
			self.ui.label2.setText('Otsu('+ str(thres) +')')
			self.ui.labelSpinBox.setText('Threshold:')
			self.ui.spinBox.setMinimum(0)
			self.ui.spinBox.setMaximum(255)
			self.ui.spinBox.setValue(thres)
	
	def wb(self, wbImg):
		if wbImg == 0:
			self.status_signal.emit(self.img1)
		elif wbImg == 1:
			self.status_signal.emit(self.img2)
	
	def update(self):
		if self.processType == 0:
			self.img1 = func.enlarge(self.img, self.ui.spinBox.value(), 0)
			self.img2 = func.enlarge(self.img, self.ui.spinBox.value(), 1)
			w, h = func.sz(self.img1)
			dim = func.dim(self.img1)
			if dim == 3:
				imgFormat = QImage.Format_RGB888
			else:
				imgFormat = QImage.Format_Grayscale8
			self.qimg1 = QImage(self.img1, w, h, w * dim, imgFormat)
			self.ui.labelImg1.setGeometry(QtCore.QRect(20, 90, w, h))
			self.ui.labelImg1.setPixmap(QPixmap.fromImage(self.qimg1))
			self.qimg2 = QImage(self.img2, w, h, w * dim, imgFormat)
			self.ui.labelImg2.setGeometry(QtCore.QRect(20+w+20, 90, w, h))
			self.ui.labelImg2.setPixmap(QPixmap.fromImage(self.qimg2))
			self.ui.label2.setGeometry(QtCore.QRect(20+w+20, 60, 100, 20))
			self.ui.pushButton2.setGeometry(QtCore.QRect(20+w+20+100, 58, 80, 24))
			window_w = min(20+w+20+w+20, 1200)
			window_h = min(90+h+10, 740)
			self.resize(window_w, window_h)
			self.ui.scrollArea.resize(window_w, window_h)
			self.ui.scrollAreaWidgetContents.setMinimumSize(20+w+20+w+20, 90+h+10)
			self.ui.scrollAreaWidgetContents.resize(window_w, window_h)
		elif self.processType == 1:
			self.img1 = func.shrink(self.img, self.ui.spinBox.value(), 0)
			self.img2 = func.shrink(self.img, self.ui.spinBox.value(), 1)
			w, h = func.sz(self.img1)
			dim = func.dim(self.img1)
			if dim == 3:
				imgFormat = QImage.Format_RGB888
			else:
				imgFormat = QImage.Format_Grayscale8
			self.qimg1 = QImage(self.img1, w, h, w * dim, imgFormat)
			self.ui.labelImg1.setGeometry(QtCore.QRect(20, 90, w, h))
			self.ui.labelImg1.setPixmap(QPixmap.fromImage(self.qimg1))
			self.qimg2 = QImage(self.img2, w, h, w * dim, imgFormat)
			self.ui.labelImg2.resize(w, h)
			self.ui.labelImg2.setPixmap(QPixmap.fromImage(self.qimg2))
		elif self.processType == 2:
			self.img1 = func.frtt(self.img, self.ui.spinBox.value())
			self.img2 = func.brtt(self.img, self.ui.spinBox.value())
			w1, h1 = func.sz(self.img1)
			w2, h2 = func.sz(self.img2)
			dim = func.dim(self.img1)
			if dim == 3:
				imgFormat = QImage.Format_RGB888
			else:
				imgFormat = QImage.Format_Grayscale8
			self.qimg1 = QImage(self.img1, w1, h1, w1 * dim, imgFormat)
			self.ui.labelImg1.setGeometry(QtCore.QRect(20, 90, w1, h1))
			self.ui.labelImg1.setPixmap(QPixmap.fromImage(self.qimg1))
			self.qimg2 = QImage(self.img2, w2, h2, w2 * dim, imgFormat)
			self.ui.labelImg2.setGeometry(QtCore.QRect(20+w1+20, 90, w2, h2))
			self.ui.labelImg2.setPixmap(QPixmap.fromImage(self.qimg2))
			self.ui.label2.setGeometry(QtCore.QRect(20+w1+20, 60, 100, 20))
			self.ui.pushButton2.setGeometry(QtCore.QRect(20+w1+20+100, 58, 80, 24))
			window_w = min(20+w1+20+w2+20, 1200)
			window_h = min(90+max(h1, h2)+10, 740)
			self.resize(window_w, window_h)
			self.ui.scrollArea.resize(window_w, window_h)
			self.ui.scrollAreaWidgetContents.setMinimumSize(20+w1+20+w2+20, 90+max(h1, h2)+10)
			self.ui.scrollAreaWidgetContents.resize(window_w, window_h)
		elif self.processType == 3:
			self.img1 = func.bimg(self.img, self.ui.spinBox.value())
			w, h = func.sz(self.img1)
			self.qimg1 = QImage(self.img1, w, h, w, QImage.Format_Grayscale8)
			self.ui.labelImg1.setPixmap(QPixmap.fromImage(self.qimg1))

class subMedian_controller(QtWidgets.QWidget):
	status_signal = pyqtSignal(np.ndarray)
	def __init__(self, img):
		super().__init__()
		self.ui = Ui_subMedian()
		self.ui.setupUi(self)
		self.img = img
		self.ui.radioButtonSqr.toggled.connect(self.ktDecide)
		self.ui.radioButtonCrs.toggled.connect(self.ktDecide)
		self.ui.radioButtonSqr.setChecked(True)
		self.ui.radioButtonM0.toggled.connect(self.methDecide)
		self.ui.radioButtonM1.toggled.connect(self.methDecide)
		self.ui.radioButtonM2.toggled.connect(self.methDecide)
		self.ui.radioButtonM0.setChecked(True)
		w, h = func.sz(img)
		dim = func.dim(img)
		if dim == 3:
			imgFormat = QImage.Format_RGB888
		else:
			imgFormat = QImage.Format_Grayscale8
		self.showImg = func.medFltr(img, self.ui.spinBox.value(), self.kernelType, self.meth)
		self.qimg = QImage(self.showImg[0], w, h, w * dim, imgFormat)
		self.ui.labelImg.setGeometry(QtCore.QRect(160, 15, w, h))
		self.ui.labelImg.setPixmap(QPixmap.fromImage(self.qimg))
		self.ui.labelSNR.setText('SNR: '+str(round(self.showImg[1], 2))+' dB')
		self.ui.labelSNR.setGeometry(QtCore.QRect(160, 15+h+10, 200, 20))
		self.ui.pushButtonWB.setGeometry(QtCore.QRect(160, 15+h+30, 80, 20))
		self.resize(160+w+10, max(15+h+60, 270))
		self.ui.pushButtonWB.clicked.connect(self.wb)
		self.ui.pushButton.clicked.connect(self.update)
	
	def wb(self):
		self.status_signal.emit(self.showImg[0])
	
	def ktDecide(self):
		rdBtn = self.sender()
		tp = [' Square', ' Cross']
		if rdBtn.isChecked():
			self.kernelType = tp.index(rdBtn.text())
	
	def methDecide(self):
		rdBtn = self.sender()
		tp = ['Median', 'Maxmin', 'Minmax']
		if rdBtn.isChecked():
			self.meth = tp.index(rdBtn.text())
	
	def update(self):
		self.ui.pushButton.setEnabled(False)
		self.showImg = func.medFltr(self.img, self.ui.spinBox.value(), self.kernelType, self.meth)
		w, h = func.sz(self.img)
		dim = func.dim(self.img)
		if dim == 3:
			imgFormat = QImage.Format_RGB888
		else:
			imgFormat = QImage.Format_Grayscale8
		self.qimg = QImage(self.showImg[0], w, h, w * dim, imgFormat)
		self.ui.labelImg.setPixmap(QPixmap.fromImage(self.qimg))
		self.ui.labelSNR.setText('SNR: '+str(round(self.showImg[1], 2))+' dB')
		self.ui.pushButton.setEnabled(True)

class subMean_controller(QtWidgets.QWidget):
	status_signal = pyqtSignal(np.ndarray)
	def __init__(self, img):
		super().__init__()
		self.ui = Ui_subMean()
		self.ui.setupUi(self)
		self.img = img
		self.ui.radioButtonSqr.toggled.connect(self.ktDecide)
		self.ui.radioButtonCrs.toggled.connect(self.ktDecide)
		self.ui.radioButtonSqr.setChecked(True)
		w, h = func.sz(img)
		dim = func.dim(img)
		if dim == 3:
			imgFormat = QImage.Format_RGB888
		else:
			imgFormat = QImage.Format_Grayscale8
		self.showImg = func.meanFltr(img, self.ui.spinBox.value(), self.kernelType)
		self.qimg = QImage(self.showImg[0], w, h, w * dim, imgFormat)
		self.ui.labelImg.setGeometry(QtCore.QRect(160, 15, w, h))
		self.ui.labelImg.setPixmap(QPixmap.fromImage(self.qimg))
		self.ui.labelSNR.setText('SNR: '+str(round(self.showImg[1], 2))+' dB')
		self.ui.labelSNR.setGeometry(QtCore.QRect(160, 15+h+10, 200, 20))
		self.ui.pushButtonWB.setGeometry(QtCore.QRect(160, 15+h+30, 80, 20))
		self.resize(160+w+10, max(15+h+60, 270))
		self.ui.pushButtonWB.clicked.connect(self.wb)
		self.ui.pushButton.clicked.connect(self.update)
	
	def wb(self):
		self.status_signal.emit(self.showImg[0])
	
	def ktDecide(self):
		rdBtn = self.sender()
		tp = [' Square', ' Cross']
		if rdBtn.isChecked():
			self.kernelType = tp.index(rdBtn.text())
	
	def update(self):
		self.ui.pushButton.setEnabled(False)
		self.showImg = func.meanFltr(self.img, self.ui.spinBox.value(), self.kernelType)
		w, h = func.sz(self.img)
		dim = func.dim(self.img)
		if dim == 3:
			imgFormat = QImage.Format_RGB888
		else:
			imgFormat = QImage.Format_Grayscale8
		self.qimg = QImage(self.showImg[0], w, h, w * dim, imgFormat)
		self.ui.labelImg.setPixmap(QPixmap.fromImage(self.qimg))
		self.ui.labelSNR.setText('SNR: '+str(round(self.showImg[1], 2))+' dB')
		self.ui.pushButton.setEnabled(True)
		
class subBright_controller(QtWidgets.QWidget):
	status_signal = pyqtSignal(np.ndarray)
	def __init__(self, img):
		super().__init__()
		self.ui = Ui_subBright()
		self.ui.setupUi(self)
		self.img = img; self.showImg = img
		w, h = func.sz(img)
		dim = func.dim(img)
		if dim == 3:
			imgFormat = QImage.Format_RGB888
		else:
			imgFormat = QImage.Format_Grayscale8
		self.qimg = QImage(self.showImg, w, h, w * dim, imgFormat)
		self.ui.labelImg.setPixmap(QPixmap.fromImage(self.qimg))
		self.ui.labelImg.setGeometry(QtCore.QRect(20, 85, w, h))
		self.ui.labelSNR.setGeometry(QtCore.QRect(20, 85+h+10, 200, 20))
		self.ui.pushButtonWB.setGeometry(QtCore.QRect(20, 85+h+30, 80, 20))
		self.ui.pushButtonWB.clicked.connect(self.wb)
		self.ui.comboBox.currentIndexChanged.connect(self.update)
		self.ui.pushButtonOK.clicked.connect(self.update)
		self.resize(max(20+w+20, 210), 85+h+60)
		
	def wb(self):
		self.status_signal.emit(self.showImg)
	
	def update(self):
		w, h = func.sz(self.img)
		dim = func.dim(self.img)
		if dim == 3:
			imgFormat = QImage.Format_RGB888
		else:
			imgFormat = QImage.Format_Grayscale8
		self.ui.pushButtonOK.setEnabled(False)
		if self.ui.comboBox.currentIndex() == 0: #exp
			self.showImg = func.adjBright(self.img, 5)
			snr = func.calSNR(self.img, self.showImg)
		elif self.ui.comboBox.currentIndex() == 1: #gamma
			self.ui.pushButtonOK.setEnabled(True)
			self.showImg = func.gammaCorr(self.img, self.ui.spinBox.value())
			snr = func.calSNR(self.img, self.showImg)
		elif self.ui.comboBox.currentIndex() == 2: #identity
			self.showImg = func.adjBright(self.img, 0)
		elif self.ui.comboBox.currentIndex() == 3: #inverse
			self.showImg = func.adjBright(self.img, 6)
			snr = func.calSNR(self.img, self.showImg)
		elif self.ui.comboBox.currentIndex() == 4: #inverse log
			self.showImg = func.adjBright(self.img, 2)
			snr = func.calSNR(self.img, self.showImg)
		elif self.ui.comboBox.currentIndex() == 5: #log
			self.showImg = func.adjBright(self.img, 1)
			snr = func.calSNR(self.img, self.showImg)
		elif self.ui.comboBox.currentIndex() == 6: #square
			self.showImg = func.adjBright(self.img, 4)
			snr = func.calSNR(self.img, self.showImg)
		elif self.ui.comboBox.currentIndex() == 7: #square root
			self.showImg = func.adjBright(self.img, 3)
			snr = func.calSNR(self.img, self.showImg)
		self.qimg = QImage(self.showImg, w, h, w * dim, imgFormat)
		self.ui.labelImg.setPixmap(QPixmap.fromImage(self.qimg))
		if self.ui.comboBox.currentIndex() == 2 or (self.ui.comboBox.currentIndex() == 1 and self.ui.spinBox.value() == 1.0):
			self.ui.labelSNR.setText('')
		else:
			self.ui.labelSNR.setText('SNR: '+str(round(snr, 2))+' dB')
			
class subBPS_controller(QtWidgets.QWidget):
	status_signal = pyqtSignal(np.ndarray)
	def __init__(self, img):
		super().__init__()
		self.ui = Ui_subBPS()
		self.ui.setupUi(self)
		self.img = img
		w, h = func.sz(img)
		self.qimg = [0 for i in range(9)]
		col1 = 10+w+10; col2 = 10+w+10+w+10; col3 = 10+w+10+w+10+w+10
		lbRow1 = 85+h+20; row1 = 85+h+20+25
		lbRow2 = 85+h+20+25+h+20; row2 = 85+h+20+25+h+20+25
		self.ui.labelImg0.setGeometry(QtCore.QRect(10, 85, w, h))
		self.ui.labelImg1.setGeometry(QtCore.QRect(col1, 85, w, h))
		self.ui.label1.setGeometry(QtCore.QRect(col1, 60, 40, 20))
		self.ui.labelImg2.setGeometry(QtCore.QRect(col2, 85, w, h))
		self.ui.label2.setGeometry(QtCore.QRect(col2, 60, 40, 20))
		self.ui.labelImg3.setGeometry(QtCore.QRect(col3, 85, w, h))
		self.ui.label3.setGeometry(QtCore.QRect(col3, 60, 40, 20))
		self.ui.labelImg4.setGeometry(QtCore.QRect(10, row1, w, h))
		self.ui.label4.setGeometry(QtCore.QRect(10, lbRow1, 40, 20))
		self.ui.labelImg5.setGeometry(QtCore.QRect(col1, row1, w, h))
		self.ui.label5.setGeometry(QtCore.QRect(col1, lbRow1, 40, 20))
		self.ui.labelImg6.setGeometry(QtCore.QRect(col2, row1, w, h))
		self.ui.label6.setGeometry(QtCore.QRect(col2, lbRow1, 40, 20))
		self.ui.labelImg7.setGeometry(QtCore.QRect(col3, row1, w, h))
		self.ui.label7.setGeometry(QtCore.QRect(col3, lbRow1, 40, 20))
		self.ui.labelImg8.setGeometry(QtCore.QRect(10, row2, w, h))
		self.ui.label8.setGeometry(QtCore.QRect(10, lbRow2, 70, 20))
		self.ui.radioButtonBit.toggled.connect(self.rdBtnClk)
		self.ui.radioButtonGray.toggled.connect(self.rdBtnClk)
		self.ui.radioButtonBit.setChecked(True)
		self.ui.pushButton.clicked.connect(self.callWM)
		self.ui.pushButtonWB.clicked.connect(self.wb)
		self.ui.pushButtonWB.setGeometry(QtCore.QRect(col1, row2+h-20, 80, 20))
		window_w = min(col3+w+24, 1200)
		self.resize(window_w, row2)
		self.ui.scrollArea.resize(window_w, row2)
		self.ui.scrollAreaWidgetContents.setMinimumSize(col3+w+20, row2+h+20)
		self.ui.scrollAreaWidgetContents.resize(window_w, row2)
		
	def rdBtnClk(self):
		rdBtn = self.sender()
		tp = ['Bit-plane slicing', 'Gray code']
		if rdBtn.isChecked():
			w, h = func.sz(self.img)
			if tp.index(rdBtn.text()) == 0:
				self.bimg = func.sbpln(self.img)
			elif tp.index(rdBtn.text()) == 1:
				self.bimg = func.gbpln(self.img)
			for i in range(8):
				self.qimg[i] = QImage(self.bimg[i], w, h, w, QImage.Format_Grayscale8)
			self.showImg = func.watermark(self.bimg[0], self.bimg[1], self.bimg[2], self.bimg[3], self.bimg[4], self.bimg[5], self.bimg[6], self.bimg[7], self.bimg[0])[0]
			self.qimg[8] = QImage(self.showImg[0], w, h, w, QImage.Format_Grayscale8)
			self.ui.labelImg0.setPixmap(QPixmap.fromImage(self.qimg[0]))
			self.ui.labelImg1.setPixmap(QPixmap.fromImage(self.qimg[1]))
			self.ui.labelImg2.setPixmap(QPixmap.fromImage(self.qimg[2]))
			self.ui.labelImg3.setPixmap(QPixmap.fromImage(self.qimg[3]))
			self.ui.labelImg4.setPixmap(QPixmap.fromImage(self.qimg[4]))
			self.ui.labelImg5.setPixmap(QPixmap.fromImage(self.qimg[5]))
			self.ui.labelImg6.setPixmap(QPixmap.fromImage(self.qimg[6]))
			self.ui.labelImg7.setPixmap(QPixmap.fromImage(self.qimg[7]))
			self.ui.labelImg8.setPixmap(QPixmap.fromImage(self.qimg[8]))
	
	def wb(self):
		self.status_signal.emit(self.showImg[0])
	
	def callWM(self):
		fname, ftype = QFileDialog.getOpenFileName(self, 'Open file', './images/')
		if fname.endswith('.pcx'):
			readImg = pcx.decPcx(fname)
			if len(readImg) < 2:
				QMessageBox.warning(self, 'Warning', 'Invalid image file (illegal .pcx)', QMessageBox.Ok)
				return
		elif fname.endswith('.bmp'):
			readImg = bmp.decBmp(fname)
			if len(readImg) < 2:
				QMessageBox.warning(self, 'Warning', 'Invalid image file (illegal .bmp)', QMessageBox.Ok)
				return
		else:
			QMessageBox.warning(self, 'Warning', 'Invalid image file', QMessageBox.Ok)
			return
		self.showImg = func.watermark(self.bimg[0], self.bimg[1], self.bimg[2], self.bimg[3], self.bimg[4], self.bimg[5], self.bimg[6], self.bimg[7], readImg[1])
		w, h = func.sz(self.img)
		self.bimg[0] = self.showImg[1]
		self.qimg[0] = QImage(self.showImg[1], w, h, w, QImage.Format_Grayscale8)
		self.qimg[8] = QImage(self.showImg[0], w, h, w, QImage.Format_Grayscale8)
		self.ui.labelImg0.setPixmap(QPixmap.fromImage(self.qimg[0]))
		self.ui.labelImg8.setPixmap(QPixmap.fromImage(self.qimg[8]))

class subOvlp_controller(QtWidgets.QWidget):
	def __init__(self, img):
		super().__init__()
		self.ui = Ui_subOvlp()
		self.ui.setupUi(self)
		self.btmImg = img
		self.showImg = img
		self.ui.pushButtonAdd.clicked.connect(self.addUpper)
		self.ui.pushButtonOK.clicked.connect(self.update)
		self.ui.pushButtonOK.setEnabled(False)

	def addUpper(self):
		fname, ftype = QFileDialog.getOpenFileName(self, 'Open file', './images/')
		if fname.endswith('.pcx'):
			readImg = pcx.decPcx(fname)
			if len(readImg) < 2:
				QMessageBox.warning(self, 'Warning', 'Invalid image file (illegal .pcx)', QMessageBox.Ok)
				return
		elif fname.endswith('.bmp'):
			readImg = bmp.decBmp(fname)
			if len(readImg) < 2:
				QMessageBox.warning(self, 'Warning', 'Invalid image file (illegal .bmp)', QMessageBox.Ok)
				return
		else:
			QMessageBox.warning(self, 'Warning', 'Invalid image file', QMessageBox.Ok)
			return
		self.upImg = readImg[1]
		wb, hb = func.sz(self.btmImg)
		wu, hu = func.sz(self.upImg)
		dim = func.dim(self.upImg)
		if dim == 3:
			imgFormat = QImage.Format_RGB888
		else:
			imgFormat = QImage.Format_Grayscale8
		self.qimg1 = QImage(self.upImg, min(wb, wu), min(hb, hu), min(wb, wu) * dim, imgFormat)
		self.ui.labelUpperImg.setPixmap(QPixmap.fromImage(self.qimg1))
		self.ui.labelUpperImg.setGeometry(QtCore.QRect(20, 50, min(wb, wu), min(hb, hu)))
		self.showImg = func.overlap(self.btmImg, self.upImg, self.ui.spinBox.value())
		self.qimg2 = QImage(self.showImg, wb, hb, wb * 4, QImage.Format_RGBA8888)
		self.ui.labelImg.setPixmap(QPixmap.fromImage(self.qimg2))
		self.ui.labelImg.setGeometry(QtCore.QRect(20+wb+10, 50, wb, hb))
		self.ui.pushButtonOK.setEnabled(True)
		self.resize(20+wb+10+wb+20, 50+hb+10)
		
	def update(self):
		ovlpImg = func.overlap(self.btmImg, self.upImg, self.ui.spinBox.value())
		wb, hb = func.sz(ovlpImg)
		self.qimg2 = QImage(ovlpImg, wb, hb, wb * 4, QImage.Format_RGBA8888)
		self.ui.labelImg.setPixmap(QPixmap.fromImage(self.qimg2))

class subHist_controller(QtWidgets.QWidget):
	def __init__(self, img):
		super().__init__()
		self.ui = Ui_subHist()
		self.ui.setupUi(self)
		if func.dim(img) == 3:
			cr, cg, cb = func.histRGB(img)
			histRGB = func.plotHistRGB(cr, cg, cb, 'RGB')
			qimg0 = QImage(histRGB, 400, 300, 400 * 4, QImage.Format_RGBA8888)
			self.ui.labelRGB.setPixmap(QPixmap.fromImage(qimg0))
			self.ui.labelRGB.setGeometry(QtCore.QRect(10, 10, 400, 300))
			self.ui.labelGray.setGeometry(QtCore.QRect(420, 10, 400, 300))
			self.resize(830, 320)
		else:
			self.ui.labelGray.setGeometry(QtCore.QRect(10, 10, 400, 300))
			self.resize(420, 320)
		c = func.histGray(img)
		histGray = func.plotHistGray(c, 'gray')
		qimg1 = QImage(histGray, 400, 300, 400 * 4, QImage.Format_RGBA8888)
		self.ui.labelGray.setPixmap(QPixmap.fromImage(qimg1))

class subHistEq_controller(QtWidgets.QWidget):
	def __init__(self, img):
		super().__init__()
		self.ui = Ui_subHistEq()
		self.ui.setupUi(self)
		w, h = func.sz(img)
		dim = func.dim(img)
		if dim == 3:
			imgFormat = QImage.Format_RGB888
		else:
			imgFormat = QImage.Format_Grayscale8
		qimg00 = QImage(img, w, h, w * dim, imgFormat)
		self.ui.labelImg.setPixmap(QPixmap.fromImage(qimg00))
		self.ui.labelImg.setGeometry(QtCore.QRect(10, 10, w, h))
		col2 = 10+w+10; col3 = 10+w+10+400+10
		row2 = 10+max(300, h)+10
		imgEq = func.histEqual(img)
		qimg10 = QImage(imgEq, w, h, w * dim, imgFormat)
		self.ui.labelEq.setPixmap(QPixmap.fromImage(qimg10))
		self.ui.labelEq.setGeometry(QtCore.QRect(10, row2, w, h))
		if dim == 3:
			cr, cg, cb  = func.histRGB(img)
			hist = func.plotHistRGB(cr, cg, cb, 'origin')
			qimg01 = QImage(hist, 400, 300, 400 * 4, QImage.Format_RGBA8888)
			self.ui.labelHist.setPixmap(QPixmap.fromImage(qimg01))
			self.ui.labelHist.setGeometry(QtCore.QRect(col2, 10, 400, 300))
			cr, cg, cb = func.cumuHist(img)
			hist = func.plotHistRGB(cr, cg, cb, 'originCumu')
			qimg02 = QImage(hist, 400, 300, 400 * 4, QImage.Format_RGBA8888)
			self.ui.labelCumu.setPixmap(QPixmap.fromImage(qimg02))
			self.ui.labelCumu.setGeometry(QtCore.QRect(col3, 10, 400, 300))
			cr, cg, cb  = func.histRGB(imgEq)
			hist = func.plotHistRGB(cr, cg, cb, 'equal')
			qimg11 = QImage(hist, 400, 300, 400 * 4, QImage.Format_RGBA8888)
			self.ui.labelEqHist.setPixmap(QPixmap.fromImage(qimg11))
			self.ui.labelEqHist.setGeometry(QtCore.QRect(col2, row2, 400, 300))
			cr, cg, cb = func.cumuHist(imgEq)
			hist = func.plotHistRGB(cr, cg, cb, 'originCumu')
			qimg12 = QImage(hist, 400, 300, 400 * 4, QImage.Format_RGBA8888)
			self.ui.labelEqCumu.setPixmap(QPixmap.fromImage(qimg12))
			self.ui.labelEqCumu.setGeometry(QtCore.QRect(col3, row2, 400, 300))
		else:
			c = func.histGray(img)
			histGray = func.plotHistGray(c, 'origin')
			qimg01 = QImage(hist, 400, 300, 400 * 4, QImage.Format_RGBA8888)
			self.ui.labelHist.setPixmap(QPixmap.fromImage(qimg01))
			self.ui.labelHist.setGeometry(QtCore.QRect(col2, 10, 400, 300))
			c = func.cumuHist(img)
			histGray = func.plotHistGray(c, 'originCumu')
			qimg02 = QImage(hist, 400, 300, 400 * 4, QImage.Format_RGBA8888)
			self.ui.labelCumu.setPixmap(QPixmap.fromImage(qimg02))
			self.ui.labelCumu.setGeometry(QtCore.QRect(col3, 10, 400, 300))
			c = func.histGray(imgEq)
			histGray = func.plotHistGray(c, 'equal')
			qimg11 = QImage(hist, 400, 300, 400 * 4, QImage.Format_RGBA8888)
			self.ui.labelEqHist.setPixmap(QPixmap.fromImage(qimg11))
			self.ui.labelEqHist.setGeometry(QtCore.QRect(col2, row2, 400, 300))
			c = func.cumuHist(imgEq)
			histGray = func.plotHistGray(c, 'equalCumu')
			qimg12 = QImage(hist, 400, 300, 400 * 4, QImage.Format_RGBA8888)
			self.ui.labelEqCumu.setPixmap(QPixmap.fromImage(qimg12))
			self.ui.labelEqCumu.setGeometry(QtCore.QRect(col3, row2, 400, 300))
		window_w = min(col3+414, 1200)
		window_h = min(row2+314, 740)
		self.resize(window_w, window_h)
		self.ui.scrollArea.resize(window_w, window_h)
		self.ui.scrollAreaWidgetContents.setMinimumSize(col3+410, row2+310)
		self.ui.scrollAreaWidgetContents.resize(window_w, window_h)

class subHistSpec_controller(QtWidgets.QWidget):
	def __init__(self, img, imgSpec):
		super().__init__()
		self.ui = Ui_subHistSpec()
		self.ui.setupUi(self)
		if func.dim(img) == 3:
			img = func.img2hsi(img)[2]
		if func.dim(imgSpec) == 3:
			imgSpec = func.img2hsi(imgSpec)[2]
		w, h = func.sz(img)
		ws, hs = func.sz(imgSpec)
		row1 = 10; row2 = row1+20; row3 = row2+max(300, h)+20; row4 = row3+20; row5 = row4+max(300, hs)+20; row6 = row5+20
		col1 = 10; col2 = col1+max(w, ws)+10; col3 = col2+400+10
		self.ui.labelOrigin.setGeometry(QtCore.QRect(col1, row1, 70, 17))
		self.ui.labelSpec.setGeometry(QtCore.QRect(col1, row3, 70, 17))
		self.ui.labelMatch.setGeometry(QtCore.QRect(col1, row5, 70, 17))
		qimg0 = QImage(img, w, h, w, QImage.Format_Grayscale8)
		self.ui.label0.setPixmap(QPixmap.fromImage(qimg0))
		self.ui.label0.setGeometry(QtCore.QRect(col1, row2, w, h))
		c = func.histGray(img); hist = func.plotHistGray(c, 'oriHist')
		qimg1 = QImage(hist, 400, 300, 400 * 4, QImage.Format_RGBA8888)
		self.ui.label1.setPixmap(QPixmap.fromImage(qimg1))
		self.ui.label1.setGeometry(QtCore.QRect(col2, row2, 400, 300))
		c = func.cumuHist(img); hist = func.plotHistGray(c, 'oriCumu')
		qimg2 = QImage(hist, 400, 300, 400 * 4, QImage.Format_RGBA8888)
		self.ui.label2.setPixmap(QPixmap.fromImage(qimg2))
		self.ui.label2.setGeometry(QtCore.QRect(col3, row2, 400, 300))
		qimg3 = QImage(imgSpec, ws, hs, ws, QImage.Format_Grayscale8)
		self.ui.label3.setPixmap(QPixmap.fromImage(qimg3))
		self.ui.label3.setGeometry(QtCore.QRect(col1, row4, ws, hs))
		c = func.histGray(imgSpec); hist = func.plotHistGray(c, 'specHist')
		qimg4 = QImage(hist, 400, 300, 400 * 4, QImage.Format_RGBA8888)
		self.ui.label4.setPixmap(QPixmap.fromImage(qimg4))
		self.ui.label4.setGeometry(QtCore.QRect(col2, row4, 400, 300))
		c = func.cumuHist(imgSpec); hist = func.plotHistGray(c, 'specCumu')
		qimg5 = QImage(hist, 400, 300, 400 * 4, QImage.Format_RGBA8888)
		self.ui.label5.setPixmap(QPixmap.fromImage(qimg5))
		self.ui.label5.setGeometry(QtCore.QRect(col3, row4, 400, 300))
		newImg = func.histSpec(img, imgSpec)
		qimg6 = QImage(newImg, w, h, w, QImage.Format_Grayscale8)
		self.ui.label6.setPixmap(QPixmap.fromImage(qimg6))
		self.ui.label6.setGeometry(QtCore.QRect(col1, row6, w, h))
		c = func.histGray(newImg); hist = func.plotHistGray(c, 'newHist')
		qimg7 = QImage(hist, 400, 300, 400 * 4, QImage.Format_RGBA8888)
		self.ui.label7.setPixmap(QPixmap.fromImage(qimg7))
		self.ui.label7.setGeometry(QtCore.QRect(col2, row6, 400, 300))
		c = func.cumuHist(newImg); hist = func.plotHistGray(c, 'newCumu')
		qimg8 = QImage(hist, 400, 300, 400 * 4, QImage.Format_RGBA8888)
		self.ui.label8.setPixmap(QPixmap.fromImage(qimg8))
		self.ui.label8.setGeometry(QtCore.QRect(col3, row6, 400, 300))
		window_w = min(col3+414, 1200)
		window_h = min(row6+max(300, h)+14, 740)
		self.resize(window_w, window_h)
		self.ui.scrollArea.resize(window_w, window_h)
		self.ui.scrollAreaWidgetContents.setMinimumSize(col3+410, row6+max(300, h)+10)
		self.ui.scrollAreaWidgetContents.resize(window_w, window_h)
		
class subSingle_controller(QtWidgets.QWidget):
	status_signal = pyqtSignal(np.ndarray)
	def __init__(self, op, img):
		super().__init__()
		self.ui = Ui_subSingle()
		self.ui.setupUi(self)
		self.img = img
		self.processType = op
		self.ui.pushButtonOK.clicked.connect(self.update)
		self.ui.pushButtonWB.clicked.connect(self.wb)
		w, h = func.sz(img)
		if op == 0:
			self.setWindowTitle('Outlier')
			self.ui.label.setText('Threshold:')
			self.ui.spinBox.setMinimum(0)
			self.ui.spinBox.setMaximum(255)
			self.ui.spinBox.setSingleStep(1)
			self.ui.spinBox.setValue(0)
			img, snr = func.outlier(self.img, self.ui.spinBox.value())
			self.ui.labelSNR.setText('SNR: '+str(round(snr, 2))+' dB')
		elif op == 1:
			self.setWindowTitle('Highpass filter')
			self.ui.label.setText('Kernel size:')
			self.ui.spinBox.setMinimum(3)
			self.ui.spinBox.setMaximum(21)
			self.ui.spinBox.setSingleStep(2)
			self.ui.spinBox.setValue(1)
			img = func.highPass(self.img, int(self.ui.spinBox.value()))
		elif op == 2:
			self.setWindowTitle('High-Boost')
			self.ui.label.setText('Amplification:')
			self.ui.spinBox.setMinimum(1)
			self.ui.spinBox.setMaximum(2)
			self.ui.spinBox.setSingleStep(0.01)
			self.ui.spinBox.setValue(1)
			img = func.highBoost(self.img, self.ui.spinBox.value())
		elif op == 3:
			self.setWindowTitle('Connected component')
			self.ui.label.setText('Threshold:')
			self.ui.spinBox.setMinimum(1)
			self.ui.spinBox.setMaximum(254)
			self.ui.spinBox.setSingleStep(1)
			self.ui.spinBox.setValue(func.otsu(img))
			img, comp = func.connComp(self.img, int(self.ui.spinBox.value()))
			self.ui.labelSNR.setText(str(comp)+' component(s)')
		self.showImg = img
		dim = func.dim(img)
		if dim == 3:
			imgFormat = QImage.Format_RGB888
		else:
			imgFormat = QImage.Format_Grayscale8
		self.qimg = QImage(img, w, h, w * dim, imgFormat)
		self.ui.labelImg.setPixmap(QPixmap.fromImage(self.qimg))
		self.ui.labelImg.setGeometry(QtCore.QRect(10, 70, w, h))
		self.resize(max(10+w+10, 280), 70+h+10)
	
	def wb(self):
		self.status_signal.emit(self.showImg)
	
	def update(self):
		if self.processType == 0:
			self.showImg, snr = func.outlier(self.img, self.ui.spinBox.value())
			self.ui.labelSNR.setText('SNR: '+str(round(snr, 2))+' dB')
		elif self.processType == 1:
			ks = int(self.ui.spinBox.value())
			self.ui.spinBox.setValue(ks)
			self.showImg = func.highPass(self.img, ks)
		elif self.processType == 2:
			self.showImg = func.highBoost(self.img, self.ui.spinBox.value())
		elif self.processType == 3:
			self.showImg, comp = func.connComp(self.img, int(self.ui.spinBox.value()))
			self.ui.labelSNR.setText(str(comp)+' component(s)')
		w, h = func.sz(self.showImg)
		dim = func.dim(self.showImg)
		if dim == 3:
			imgFormat = QImage.Format_RGB888
		else:
			imgFormat = QImage.Format_Grayscale8
		self.qimg = QImage(self.showImg, w, h, w * dim, imgFormat)
		self.ui.labelImg.setPixmap(QPixmap.fromImage(self.qimg))

class subEdgeCrsp_controller(QtWidgets.QWidget):
	status_signal = pyqtSignal(np.ndarray)
	def __init__(self, img):
		super().__init__()
		self.ui = Ui_subEdgeCrsp()
		self.ui.setupUi(self)
		if func.dim(img) == 3:
			img = func.img2hsi(img)[2]
		self.img = img
		self.ui.radioButtonSqr.toggled.connect(self.ktDecide)
		self.ui.radioButtonCrs.toggled.connect(self.ktDecide)
		self.ui.radioButtonSqr.setChecked(True)
		self.ui.radioButtonM0.toggled.connect(self.methDecide)
		self.ui.radioButtonM1.toggled.connect(self.methDecide)
		self.ui.radioButtonM0.setChecked(True)
		w, h = func.sz(self.img)
		if self.meth == 0:
			self.imgBlur = func.meanFltr(self.img, self.ui.spinBox.value(), self.kernelType)
		elif self.meth == 1:
			self.imgBlur = func.medFltr(self.img, self.ui.spinBox.value(), self.kernelType, 0)
		self.ui.label0.setGeometry(QtCore.QRect(160, 10, 120, 20))
		qimg = QImage(self.imgBlur[0], w, h, w, QImage.Format_Grayscale8)
		self.ui.labelImg0.setGeometry(QtCore.QRect(160, 40, w, h))
		self.ui.labelImg0.setPixmap(QPixmap.fromImage(qimg))
		self.ui.labelSNR0.setText('SNR: '+str(round(self.imgBlur[1], 2))+' dB')
		self.ui.labelSNR0.setGeometry(QtCore.QRect(160, 40+h+10, 200, 20))
		self.ui.label1.setGeometry(QtCore.QRect(160, 40+h+50, 120, 20))
		self.showImg = func.edgeCrsp(self.img, self.imgBlur[0])
		qimg = QImage(self.showImg, w, h, w , QImage.Format_Grayscale8)
		self.ui.labelImg1.setGeometry(QtCore.QRect(160, 40+h+80, w, h))
		self.ui.labelImg1.setPixmap(QPixmap.fromImage(qimg))
		snr = func.calSNR(self.img, self.showImg)
		self.ui.labelSNR1.setText('SNR: '+str(round(snr, 2))+' dB')
		self.ui.labelSNR1.setGeometry(QtCore.QRect(160, 40+h+80+h+10, 200, 20))
		self.ui.pushButtonWB.setGeometry(QtCore.QRect(160, 40+h+80+h+35, 80, 20))
		self.resize(160+w+10, max(40+h+80+h+70, 270))
		self.ui.pushButtonWB.clicked.connect(self.wb)
		self.ui.pushButton.clicked.connect(self.update)
	
	def wb(self):
		self.status_signal.emit(self.showImg)
	
	def ktDecide(self):
		rdBtn = self.sender()
		tp = [' Square', ' Cross']
		if rdBtn.isChecked():
			self.kernelType = tp.index(rdBtn.text())
	
	def methDecide(self):
		rdBtn = self.sender()
		tp = ['Mean', 'Median']
		if rdBtn.isChecked():
			self.meth = tp.index(rdBtn.text())
	
	def update(self):
		self.ui.pushButton.setEnabled(False)
		w, h = func.sz(self.img)
		if self.meth == 0:
			self.imgBlur = func.meanFltr(self.img, self.ui.spinBox.value(), self.kernelType)
		elif self.meth == 1:
			self.imgBlur = func.medFltr(self.img, self.ui.spinBox.value(), self.kernelType, 0)
		qimg = QImage(self.imgBlur[0], w, h, w, QImage.Format_Grayscale8)
		self.ui.labelImg0.setPixmap(QPixmap.fromImage(qimg))
		self.ui.labelSNR0.setText('SNR: '+str(round(self.imgBlur[1], 2))+' dB')
		self.showImg = func.edgeCrsp(self.img, self.imgBlur[0])
		qimg = QImage(self.showImg, w, h, w , QImage.Format_Grayscale8)
		self.ui.labelImg1.setPixmap(QPixmap.fromImage(qimg))
		snr = func.calSNR(self.img, self.showImg)
		self.ui.labelSNR1.setText('SNR: '+str(round(snr, 2))+' dB')
		self.ui.pushButton.setEnabled(True)

class subGrad_controller(QtWidgets.QWidget):
	def __init__(self, img):
		super().__init__()
		self.ui = Ui_subGrad()
		self.ui.setupUi(self)
		imgR0, imgR1, imgR2 = func.roberts(img)
		imgS0, imgS1, imgS2 = func.sobel(img)
		imgP0, imgP1, imgP2 = func.prewitt(img)
		w, h = func.sz(img)
		row1 = 10; row2 = 34; row3 = 58; row4 = 58+h+10; row5 = row4+24; row6 = row5+h+10; row7 = row6+24
		col1 = 10; col2 = 10+w+10; col3 = 10+w+10+w+10
		self.ui.labelX.setGeometry(QtCore.QRect(col1, row1, 90, 17))
		self.ui.labelY.setGeometry(QtCore.QRect(col2, row1, 90, 17))
		self.ui.labelZ.setGeometry(QtCore.QRect(col3, row1, 90, 17))
		self.ui.labelRoberts.setGeometry(QtCore.QRect(col1, row2, 90, 17))
		self.qimgR0 = QImage(imgR0, w, h, w, QImage.Format_Grayscale8)
		self.ui.labelR0.setGeometry(QtCore.QRect(col1, row3, w, h))
		self.ui.labelR0.setPixmap(QPixmap.fromImage(self.qimgR0))
		self.qimgR1 = QImage(imgR1, w, h, w, QImage.Format_Grayscale8)
		self.ui.labelR1.setGeometry(QtCore.QRect(col2, row3, w, h))
		self.ui.labelR1.setPixmap(QPixmap.fromImage(self.qimgR1))
		self.qimgR2 = QImage(imgR2, w, h, w, QImage.Format_Grayscale8)
		self.ui.labelR2.setGeometry(QtCore.QRect(col3, row3, w, h))
		self.ui.labelR2.setPixmap(QPixmap.fromImage(self.qimgR2))
		self.ui.labelSobel.setGeometry(QtCore.QRect(col1, row4, 90, 17))
		self.qimgS0 = QImage(imgS0, w, h, w, QImage.Format_Grayscale8)
		self.ui.labelS0.setGeometry(QtCore.QRect(col1, row5, w, h))
		self.ui.labelS0.setPixmap(QPixmap.fromImage(self.qimgS0))
		self.qimgS1 = QImage(imgS1, w, h, w, QImage.Format_Grayscale8)
		self.ui.labelS1.setGeometry(QtCore.QRect(col2, row5, w, h))
		self.ui.labelS1.setPixmap(QPixmap.fromImage(self.qimgS1))
		self.qimgS2 = QImage(imgS2, w, h, w, QImage.Format_Grayscale8)
		self.ui.labelS2.setGeometry(QtCore.QRect(col3, row5, w, h))
		self.ui.labelS2.setPixmap(QPixmap.fromImage(self.qimgS2))
		self.ui.labelPrewitt.setGeometry(QtCore.QRect(col1, row6, 90, 17))
		self.qimgP0 = QImage(imgP0, w, h, w, QImage.Format_Grayscale8)
		self.ui.labelP0.setGeometry(QtCore.QRect(col1, row7, w, h))
		self.ui.labelP0.setPixmap(QPixmap.fromImage(self.qimgP0))
		self.qimgP1 = QImage(imgP1, w, h, w, QImage.Format_Grayscale8)
		self.ui.labelP1.setGeometry(QtCore.QRect(col2, row7, w, h))
		self.ui.labelP1.setPixmap(QPixmap.fromImage(self.qimgP1))
		self.qimgP2 = QImage(imgP2, w, h, w, QImage.Format_Grayscale8)
		self.ui.labelP2.setGeometry(QtCore.QRect(col3, row7, w, h))
		self.ui.labelP2.setPixmap(QPixmap.fromImage(self.qimgP2))
		window_w = min(col3+w+18, 1200)
		window_h = min(row7+h+18, 740)
		self.resize(window_w, window_h)
		self.ui.scrollArea.resize(window_w, window_h)
		self.ui.scrollAreaWidgetContents.setMinimumSize(col3+w+12, row7+h+18)
		self.ui.scrollAreaWidgetContents.resize(window_w, window_h)

class subCtrStr_controller(QtWidgets.QWidget):
	status_signal = pyqtSignal(np.ndarray)
	def __init__(self, img):
		super().__init__()
		self.ui = Ui_subCtrStr()
		self.ui.setupUi(self)
		self.ui.pushButtonOK.clicked.connect(self.update)
		self.ui.pushButtonWB.clicked.connect(self.wb)
		self.ui.spinBoxUB.valueChanged.connect(self.adjUB)
		self.ui.spinBoxLB.valueChanged.connect(self.adjLB)
		w, h = func.sz(img)
		if func.dim(img) == 3:
			img = func.img2hsi(img)[2]
		self.img = img
		self.qimg0 = QImage(self.img, w, h, w, QImage.Format_Grayscale8)
		self.ui.labelOri.setPixmap(QPixmap.fromImage(self.qimg0))
		self.ui.labelOri.setGeometry(QtCore.QRect(10, 135, w, h))
		self.ui.labelR.setGeometry(QtCore.QRect(10+w+10, 110, 135, 17))
		self.showImg = func.ctrStr(self.img, self.ui.spinBoxLB.value(), self.ui.spinBoxUB.value(), self.ui.spinBoxCutoff.value())
		self.qimg = QImage(self.showImg, w, h, w, QImage.Format_Grayscale8)
		self.ui.labelImg.setPixmap(QPixmap.fromImage(self.qimg))
		self.ui.labelImg.setGeometry(QtCore.QRect(10+w+10, 135, w, h))
		self.resize(max(390, 10+w+10+w+10), 135+h+10)
	
	def wb(self):
		self.status_signal.emit(self.showImg)
	
	def adjUB(self):
		self.ui.spinBoxUB.setMinimum(min(self.ui.spinBoxLB.value()+1, 254))
	
	def adjLB(self):
		self.ui.spinBoxLB.setMaximum(max(self.ui.spinBoxUB.value()-1, 1))
	
	def update(self):
		self.showImg = func.ctrStr(self.img, self.ui.spinBoxLB.value(), self.ui.spinBoxUB.value(), self.ui.spinBoxCutoff.value())
		w, h = func.sz(self.showImg)
		self.qimg = QImage(self.showImg, w, h, w, QImage.Format_Grayscale8)
		self.ui.labelImg.setPixmap(QPixmap.fromImage(self.qimg))

class subHfm_controller(QtWidgets.QWidget):
	def __init__(self, img):
		super().__init__()
		self.ui = Ui_subHfm()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.decmprs)
		table, ratio = cmprs.huffman(img)
		self.ui.label.setText('Compression ratio: '+str(ratio)+'%')
		model = QStandardItemModel(len(table), 3)
		model.setHorizontalHeaderLabels(['Value', 'Frequency', 'Encode'])
		for i in range(len(table)):
			val = QStandardItem(table[i][0]); model.setItem(i, 0, val)
			frq = QStandardItem(table[i][1]); model.setItem(i, 1, frq)
			ecd = QStandardItem(table[i][2]); model.setItem(i, 2, ecd)
		self.ui.tableView.setModel(model)
		self.ui.tableView.setColumnWidth(0, 20)
		self.ui.tableView.setColumnWidth(1, 90)
		self.ui.tableView.setColumnWidth(2, 160)
		
	def decmprs(self):
		img = cmprs.decd()
		w, h = func.sz(img)
		dim = func.dim(img)
		if dim == 3:
			imgFormat = QImage.Format_RGB888
		else:
			imgFormat = QImage.Format_Grayscale8
		qimg = QImage(img, w, h, w * dim, imgFormat)
		self.ui.labelImg.setPixmap(QPixmap.fromImage(qimg))
		self.ui.labelImg.setGeometry(QtCore.QRect(350, 40, w, h))
		self.resize(350+w+10, max(350, 40+h+10))
	
