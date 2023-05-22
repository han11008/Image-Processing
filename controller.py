from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage, QPixmap, QMouseEvent
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QSplashScreen
from PyQt5.QtCore import QTimer, pyqtSignal
from PIL import Image
import time
import pcx, bmp, func
import ctrlSub

from main import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.splash = QSplashScreen(QPixmap('UI/splash.png'), QtCore.Qt.WindowStaysOnTopHint)
		self.splash.show()
		QTimer.singleShot(2500, self.splash.close)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.move(100, 100)
		self.setup_control()
	
	def setup_control(self):
		self.img = 0
		self.ui.menuOperation.setEnabled(False)
		self.ui.actionOpen.triggered.connect(self.open_file)
		self.ui.actionSave.triggered.connect(self.save_file)
		self.ui.actionRGB.triggered.connect(lambda: self.img_channel(0))
		self.ui.actionHSI.triggered.connect(lambda: self.img_channel(1))
		self.ui.actionEnlarge.triggered.connect(lambda: self.img_2cmp(0))
		self.ui.actionShrink.triggered.connect(lambda: self.img_2cmp(1))
		self.ui.actionRotate.triggered.connect(lambda: self.img_2cmp(2))
		self.ui.actionGray.triggered.connect(self.img_gray)
		self.ui.actionNegative.triggered.connect(self.img_neg)
		self.ui.actionAddNoise.triggered.connect(self.img_addNoise)
		self.ui.actionThresholding.triggered.connect(lambda: self.img_2cmp(3))
		self.ui.actionBrightness.triggered.connect(self.img_brt)
		self.ui.actionBPSlc.triggered.connect(self.img_bpslc)
		self.ui.actionHistogram.triggered.connect(self.img_hist)
		self.ui.actionHistEq.triggered.connect(self.img_histEq)
		self.ui.actionHistSpec.triggered.connect(self.img_histSpec)
		self.ui.actionOverlap.triggered.connect(self.img_overlap)
		self.ui.actionRect.triggered.connect(lambda: self.img_cut(0))
		self.ui.actionOval.triggered.connect(lambda: self.img_cut(1))
		self.ui.actionMW.triggered.connect(self.img_mw)
		self.ui.actionCtrStr.triggered.connect(self.img_ctrstr)
		self.ui.actionOutlier.triggered.connect(lambda: self.img_single(0))
		self.ui.actionMedian.triggered.connect(self.img_medFltr)
		self.ui.actionLowpass.triggered.connect(self.img_lpf)
		self.ui.actionHighpass.triggered.connect(lambda: self.img_single(1))
		self.ui.actionHighBoost.triggered.connect(lambda: self.img_single(2))
		self.ui.actionEdgeCrsp.triggered.connect(self.img_edgeCrsp)
		self.ui.actionGradient.triggered.connect(self.img_grad)
		self.ui.actionHuffman.triggered.connect(self.img_cmprs)
		self.ui.actionConnComp.triggered.connect(lambda: self.img_single(3))
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.detect_mouse)
		self.timer.start(100)
	
	def open_file(self):
		fname, ftype = QFileDialog.getOpenFileName(self, 'Open file', './images/')
		self.img_path = fname
		self.display_img()
	
	def save_file(self):
		if isinstance(self.img, int):
			QMessageBox.warning(self, 'Warning', 'No valid image to save', QMessageBox.Ok)
		else:
			filename = self.img_path.split('.')[0]
			filetype = self.img_path.split('.')[1]
			newFile = filename + '_' + str(time.localtime()[1]) + str(time.localtime()[2]) + '.' + filetype
			Image.fromarray(self.img).save(newFile)
			QMessageBox.about(self, 'Image saved', 'Processed image has been saved as ' + newFile.split('/')[-1])
	
	def display_img(self):
		if self.img_path.endswith('.pcx'):
			readImg = pcx.decPcx(self.img_path)
			if len(readImg) < 2:
				QMessageBox.warning(self, 'Warning', 'Invalid image file (illegal .pcx)', QMessageBox.Ok)
				return
			self.img = readImg[1]
		elif self.img_path.endswith('.bmp'):
			readImg = bmp.decBmp(self.img_path)
			if len(readImg) < 2:
				QMessageBox.warning(self, 'Warning', 'Invalid image file (illegal .bmp)', QMessageBox.Ok)
				return
			self.img = readImg[1]
		else:
			QMessageBox.warning(self, 'Warning', 'Invalid image file', QMessageBox.Ok)
			return
		w, h = func.sz(self.img)
		self.qimg = QImage(self.img, w, h, w * 3, QImage.Format_RGB888)
		self.ui.mainImg.setGeometry(QtCore.QRect(10, 10, w, h))
		self.ui.mainImg.setPixmap(QPixmap.fromImage(self.qimg))
		self.ui.mainImg.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		if len(readImg) == 3:
			self.imgCP = readImg[2]
			self.qimgCP = QImage(self.imgCP, 256, 256, 256 * 3, QImage.Format_RGB888)
			self.ui.colorPalette.setGeometry(QtCore.QRect(10+w+10, 10, 256, 256))
			self.ui.colorPalette.setPixmap(QPixmap.fromImage(self.qimgCP))
			window_w = w + 256 + 30
		else:
			self.ui.colorPalette.setGeometry(QtCore.QRect(0, 0, 0, 0))
			window_w = max(w + 20, 440)
		self.oriImg = self.img.copy()
		self.ui.hdr.setGeometry(QtCore.QRect(10, 10+h+10, 420, 360))
		self.ui.hdr.setText(readImg[0])
		self.ui.menuOperation.setEnabled(True)
		self.ui.mainImg.setMouseTracking(True)
		self.ui.mainImg.mouseMoveEvent = self.get_mouse_pos
		self.resize(window_w, 680)
	
	def get_mouse_pos(self, event):
		self.img_posX = event.pos().x()
		self.img_posY = event.pos().y()
	
	def detect_mouse(self):
		if not isinstance(self.img, int):
			self.get_mouse_pos
			if 'img_posX' in dir(self) and 'img_posY' in dir(self):
				w, h = func.sz(self.img)
				if self.img_posX < w and self.img_posY < h:
					if func.dim(self.img) == 3:
						r, g, b, h, s, i = func.get_rgb_hsi(self.img, self.img_posX, self.img_posY)
						self.ui.statusbar.showMessage(f'(x = {self.img_posX}, y = {self.img_posY}) R:{r} G:{g} B:{b} H:{h} S:{s} I:{i}')
					else:
						v = func.get_value(self.img, self.img_posX, self.img_posY)
						self.ui.statusbar.showMessage(f'(x = {self.img_posX}, y = {self.img_posY}) value:{v}')
				
	def img_channel(self, op):
		if func.dim(self.img) == 3 :
			self.childWindow = ctrlSub.subChannel_controller(op, self.img)
			self.childWindow.show()
		else:
			QMessageBox.warning(self, 'Warning', 'Image is grayscale', QMessageBox.Ok)
	
	def childWB(self, imgWB):
		self.img = imgWB
		w, h = func.sz(self.img)
		d = func.dim(self.img)
		if d == 3:
			imgFormat = QImage.Format_RGB888
		else:
			imgFormat = QImage.Format_Grayscale8
		self.qimg = QImage(self.img, w, h, w * d, imgFormat)
		self.ui.mainImg.setPixmap(QPixmap.fromImage(self.qimg))
	
	def img_2cmp(self, op):
		self.childWindow = ctrlSub.sub2cmp_controller(op, self.img)
		self.childWindow.status_signal.connect(self.childWB)
		self.childWindow.show()
	
	def img_gray(self):
		if func.dim(self.img) == 3:
			self.img = func.img2hsi(self.img)[2]
			w, h = func.sz(self.img)
			self.qimg = QImage(self.img, w, h, w, QImage.Format_Grayscale8)
			self.ui.mainImg.setPixmap(QPixmap.fromImage(self.qimg))
	
	def img_neg(self):
		self.img = func.neg(self.img)
		w, h = func.sz(self.img)
		dim = func.dim(self.img)
		if dim == 3:
			imgFormat = QImage.Format_RGB888
		else:
			imgFormat = QImage.Format_Grayscale8
		self.qimg = QImage(self.img, w, h, w * dim, imgFormat)
		self.ui.mainImg.setPixmap(QPixmap.fromImage(self.qimg))
	
	def img_addNoise(self):
		self.img = func.addNoise(self.img)
		w, h = func.sz(self.img)
		dim = func.dim(self.img)
		if dim == 3:
			imgFormat = QImage.Format_RGB888
		else:
			imgFormat = QImage.Format_Grayscale8
		self.qimg = QImage(self.img, w, h, w * dim, imgFormat)
		self.ui.mainImg.setPixmap(QPixmap.fromImage(self.qimg))
	
	def img_brt(self):
		self.childWindow = ctrlSub.subBright_controller(self.img)
		self.childWindow.status_signal.connect(self.childWB)
		self.childWindow.show()
	
	def img_bpslc(self):
		self.childWindow = ctrlSub.subBPS_controller(self.img)
		self.childWindow.status_signal.connect(self.childWB)
		self.childWindow.show()
	
	def img_hist(self):
		self.childWindow = ctrlSub.subHist_controller(self.img)
		self.childWindow.show()
	
	def img_histEq(self):
		self.childWindow = ctrlSub.subHistEq_controller(self.img)
		self.childWindow.show()
		
	def img_histSpec(self):
		fname, ftype = QFileDialog.getOpenFileName(self, 'Open file', './images/')
		if fname.endswith('.pcx'):
			readImg = pcx.decPcx(fname)
			if len(readImg) < 2:
				QMessageBox.warning(self, 'Warning', 'Invalid image file (illegal .pcx)', QMessageBox.Ok)
				return
			imgSpec = readImg[1]
		elif fname.endswith('.bmp'):
			readImg = bmp.decBmp(fname)
			if len(readImg) < 2:
				QMessageBox.warning(self, 'Warning', 'Invalid image file (illegal .bmp)', QMessageBox.Ok)
				return
			imgSpec = readImg[1]
		else:
			QMessageBox.warning(self, 'Warning', 'Invalid image file', QMessageBox.Ok)
			return
		self.childWindow = ctrlSub.subHistSpec_controller(self.img, imgSpec)
		self.childWindow.show()
	
	def img_overlap(self):
		self.childWindow = ctrlSub.subOvlp_controller(self.img)
		self.childWindow.show()
	
	def img_cut(self, op):
		self.childWindow = ctrlSub.subCut_controller(op, self.img)
		self.childWindow.show()
	
	def img_mw(self):
		self.childWindow = ctrlSub.subMW_controller(self.img)
		self.childWindow.show()
	
	def img_ctrstr(self):
		self.childWindow = ctrlSub.subCtrStr_controller(self.img)
		self.childWindow.status_signal.connect(self.childWB)
		self.childWindow.show()
	
	def img_medFltr(self):
		self.childWindow = ctrlSub.subMedian_controller(self.img)
		self.childWindow.status_signal.connect(self.childWB)
		self.childWindow.show()
	
	def img_lpf(self):
		self.childWindow = ctrlSub.subMean_controller(self.img)
		self.childWindow.status_signal.connect(self.childWB)
		self.childWindow.show()
	
	def img_edgeCrsp(self):
		self.childWindow = ctrlSub.subEdgeCrsp_controller(self.img)
		self.childWindow.status_signal.connect(self.childWB)
		self.childWindow.show()
	
	def img_single(self, op):
		self.childWindow = ctrlSub.subSingle_controller(op, self.img)
		self.childWindow.status_signal.connect(self.childWB)
		self.childWindow.show()
	
	def img_grad(self):
		self.childWindow = ctrlSub.subGrad_controller(self.img)
		self.childWindow.show()
	
	def img_cmprs(self):
		self.childWindow = ctrlSub.subHfm_controller(self.img)
		self.childWindow.show()

