import numpy as np
from PIL import Image
import math
from itertools import combinations
from matplotlib import pyplot

def sz(imgArr):
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	return [sizeX, sizeY]

def dim(imgArr):
	try:
		dim = len(imgArr[0][0])
		return 3
	except:
		return 1

def get_rgb_hsi(imgArr, x, y):
	r = int(imgArr[y][x][0])
	g = int(imgArr[y][x][1])
	b = int(imgArr[y][x][2])
	theta = math.acos((((r - g) + (r - b)) / 2) / (math.sqrt((r - g) ** 2 + (r - b) * (g - b)) + 0.000001)) * 180 / math.pi
	if b > g:
		h = int(255 - (theta / 360) * 255)
	else:
		h = int((theta / 360) * 255)
	s = int((1 - 3 * min(r, g, b) / (r + g + b + 0.000001)) * 255)
	i = int((r + g + b) / 3)
	return [r, g, b, h, s, i]

def get_value(imgArr, x, y):
	return imgArr[y][x]

def img2rgb(imgArr):
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	imgR = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgG = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgB = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			imgR[j][i] = int(imgArr[j][i][0])
			imgG[j][i] = int(imgArr[j][i][1])
			imgB[j][i] = int(imgArr[j][i][2])
	set0 = np.array(np.uint8([[0 for i in range(sizeX)] for j in range(sizeY)]))
	imgR = np.dstack((np.array(np.uint8(imgR)), set0, set0))
	imgG = np.dstack((set0, np.array(np.uint8(imgG)), set0))
	imgB = np.dstack((set0, set0, np.array(np.uint8(imgB))))
	return [imgR, imgG, imgB]

def histRGB(imgArr):
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	cr = [0 for i in range(256)]
	cg = [0 for i in range(256)]
	cb = [0 for i in range(256)]
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			cr[imgArr[j][i][0]] += 1
			cg[imgArr[j][i][1]] += 1
			cb[imgArr[j][i][2]] += 1
	return [cr, cg, cb]

def histGray(imgArr):
	if dim(imgArr) == 3:
		imgArr = img2hsi(imgArr)[2]
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	c = [0 for i in range(256)]
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			c[imgArr[j][i]] += 1
	return c

def png2arr(fn = 'hist'):
	img = Image.open('tmp/'+fn+'.png').resize((400, 300))
	w, h = img.size
	img = img.load()
	imgR = [[0 for i in range(w)] for j in range(h)]
	imgG = [[0 for i in range(w)] for j in range(h)]
	imgB = [[0 for i in range(w)] for j in range(h)]
	imgA = [[0 for i in range(w)] for j in range(h)]
	for i in range(w):
		for j in range(h):
			imgR[j][i] = img[i, j][0]
			imgG[j][i] = img[i, j][1]
			imgB[j][i] = img[i, j][2]
			imgA[j][i] = img[i, j][3]
	imgArr = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB)), np.array(np.uint8(imgA))))
	return imgArr

def plotHistRGB(cr, cg, cb, fn = 'hist'):
	x = []
	for i in range(0, 256):
		x.append(i)
	pyplot.subplot(2, 2, 1)
	pyplot.bar(x, cr, color = 'r', align = 'center')
	pyplot.subplot(2, 2, 2)
	pyplot.bar(x, cg, color = 'g', align = 'center')
	pyplot.subplot(2, 2, 3)
	pyplot.bar(x, cb, color = 'b', align = 'center')
	pyplot.subplot(2, 2, 4)
	pyplot.bar(x, cr, color = 'r', align = 'center')
	pyplot.bar(x, cg, color = 'g', align = 'center')
	pyplot.bar(x, cb, color = 'b', align = 'center')
	pyplot.savefig('tmp/'+fn+'.png', bbox_inches = 'tight', pad_inches = 0.2)
	pyplot.close()
	return png2arr(fn)

def plotHistGray(c, fn = 'hist'):
	x = []
	for i in range(0, 256):
		x.append(i)
	pyplot.bar(x, c, color = 'k', align = 'center')
	pyplot.savefig('tmp/'+fn+'.png', bbox_inches = 'tight', pad_inches = 0.2)
	pyplot.close()
	return png2arr(fn)

def histEqual(imgArr, ER = True, EG = True, EB = True):
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	d = dim(imgArr)
	if d == 3:
		cr, cg, cb = histRGB(imgArr)
	else:
		c = histGray(imgArr)
	imgR = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgG = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgB = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	if d == 3:
		cr[0] *= 255 / (sizeX * sizeY)
		cg[0] *= 255 / (sizeX * sizeY)
		cb[0] *= 255 / (sizeX * sizeY)
		for i in range(1, 256):
			cr[i] *= 255 / (sizeX * sizeY); cr[i] += cr[i - 1]
			cg[i] *= 255 / (sizeX * sizeY); cg[i] += cg[i - 1]
			cb[i] *= 255 / (sizeX * sizeY); cb[i] += cb[i - 1]
		for i in range(256):
			cr[i] = round(cr[i])
			cg[i] = round(cg[i])
			cb[i] = round(cb[i])
	else:
		c[0] *= 255 / (sizeX * sizeY)
		for i in range(1, 256):
			c[i] *= 255 / (sizeX * sizeY); c[i] += c[i - 1]
		for i in range(256):
			c[i] = round(c[i])
	for i in range(sizeX):
		for j in range(sizeY):
			if d == 3:
				if ER:
					imgR[j][i] = cr[imgArr[j][i][0]]
				else:
					imgR[j][i] = imgArr[j][i][0]
				if EG:
					imgG[j][i] = cg[imgArr[j][i][1]]
				else:
					imgG[j][i] = imgArr[j][i][1]
				if EB:
					imgB[j][i] = cb[imgArr[j][i][2]]
				else:
					imgB[j][i] = imgArr[j][i][2]
			else:
				imgR[j][i] = c[imgArr[j][i]]
	if d == 3:
		img = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB))))
	else:
		img = np.array(np.uint8(imgR))
	return img

def histSpec(imgArr, imgRef):
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	d = dim(imgArr)
	imgR = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgG = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgB = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	if d == 3:
		cr, cg, cb = cumuHist(imgArr)
		if dim(imgRef) == 3:
			ref_cr, ref_cg, ref_cb = cumuHist(imgRef)
		else:
			ref_cr = cumuHist(imgRef)
			ref_cg = ref_cr.copy(); ref_cb = ref_cr.copy()
		curR = 0; curG = 0; curB = 0
		for i in range(256):
			if cr[i] <= ref_cr[curR]:
				cr[i] = curR
			else:
				while cr[i] > ref_cr[curR] and curR < 255:
					curR += 1
				if abs(cr[i] - ref_cr[curR - 1]) < abs(cr[i] - ref_cr[curR]):
					cr[i] = curR - 1
				else:
					cr[i] = curR
			if cg[i] <= ref_cg[curG]:
				cg[i] = curG
			else:
				while cg[i] > ref_cg[curG] and curG < 255:
					curG += 1
				if abs(cg[i] - ref_cg[curG - 1]) < abs(cg[i] - ref_cg[curG]):
					cg[i] = curG - 1
				else:
					cg[i] = curG
			if cb[i] <= ref_cb[curB]:
				cb[i] = curB
			else:
				while cb[i] > ref_cb[curB] and curB < 255:
					curB += 1
				if abs(cb[i] - ref_cb[curB - 1]) < abs(cb[i] - ref_cb[curB]):
					cb[i] = curB - 1
				else:
					cb[i] = curB
	else:
		c = cumuHist(imgArr)
		if dim(imgRef) == 3:
			ref_c = cumuHist(img2hsi(imgRef)[2])
		else:
			ref_c = cumuHist(imgRef)
		cur = 0
		for i in range(256):
			if c[i] <= ref_c[cur]:
				c[i] = cur
			else:
				while c[i] > ref_c[cur] and cur < 255:
					cur += 1
				if abs(c[i] - ref_c[cur - 1]) < abs(c[i] - ref_c[cur]):
					c[i] = cur - 1
				else:
					c[i] = cur
	for i in range(sizeX):
		for j in range(sizeY):
			if d == 3:
				imgR[j][i] = cr[imgArr[j][i][0]]
				imgG[j][i] = cg[imgArr[j][i][1]]
				imgB[j][i] = cb[imgArr[j][i][2]]
			else:
				imgR[j][i] = c[imgArr[j][i]]
	if d == 3:
		img = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB))))
	else:
		img = np.array(np.uint8(imgR))
	return img

def cumuHist(imgArr):
	d = dim(imgArr)
	if d == 3:
		cr, cg, cb = histRGB(imgArr)
		for i in range(1, 256):
			cr[i] += cr[i - 1]
			cg[i] += cg[i - 1]
			cb[i] += cb[i - 1]
		return [cr, cg, cb]
	else:
		c = histGray(imgArr)
		for i in range(1, 256):
			c[i] += c[i - 1]
		return c

def img2hsi(imgArr):
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	imgH = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgS = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgI = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			r = int(imgArr[j][i][0])
			g = int(imgArr[j][i][1])
			b = int(imgArr[j][i][2])
			theta = math.acos((((r - g) + (r - b)) / 2) / (math.sqrt((r - g) ** 2 + (r - b) * (g - b)) + 0.000001)) * 180 / math.pi
			if b > g:
				imgH[j][i] = int(255 - (theta / 360) * 255)
			else:
				imgH[j][i] = int((theta / 360) * 255)
			imgS[j][i] = int((1 - 3 * min(r, g, b) / (r + g + b + 0.000001)) * 255)
			imgI[j][i] = int((r + g + b) / 3)
	imgH = np.array(np.uint8(imgH))
	imgS = np.array(np.uint8(imgS))
	imgI = np.array(np.uint8(imgI))
	return [imgH, imgS, imgI]

def neg(imgArr):
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	d = dim(imgArr)
	imgR = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgG = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgB = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			if d == 3:
				imgR[j][i] = 255 - int(imgArr[j][i][0])
				imgG[j][i] = 255 - int(imgArr[j][i][1])
				imgB[j][i] = 255 - int(imgArr[j][i][2])
			else:
				imgR[j][i] = 255 - int(imgArr[j][i])
	if d == 3:
		img = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB))))
	else:
		img  = np.array(np.uint8(imgR))
	return img

def bimg(imgArr, thres):
	if dim(imgArr) == 3:
		imgArr = img2hsi(imgArr)[2]
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	img = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			if imgArr[j][i] > thres:
				img[j][i] = 255
			else:
				img[j][i] = 0
	img = np.array(np.uint8(img))
	return img

def otsu(imgArr):
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	N = sizeX * sizeY
	m = 0
	hist = histGray(imgArr)
	for i in range(0, 256):
		hist[i] /= N
		m += i * hist[i]
	otsuV = 0
	otsuT = 0
	for thres in range(1, 255):
		w1 = sum(hist[0:thres]); m1 = 0; v1 = 0
		w2 = sum(hist[thres:256]); m2 = 0; v2 = 0
		for i in range(0, thres):
			m1 += i * hist[i]
		if w1 > 0:
			m1 /= w1
		for i in range(thres, 256):
			m2 += i * hist[i]
		if w2 > 0:
			m2 /= w2
		for i in range(0, thres):
			v1 += (i - m1) ** 2 * hist[i]
		if w1 > 0:
			v1 /= w1
		for i in range(thres, 256):
			v2 += (i - m2) ** 2 * hist[i]
		if w2 > 0:
			v2 /= w2
		vb = w1 * (m1 - m) ** 2 + w2 * (m2 - m) ** 2
		if otsuV < vb:
			otsuV = vb
			otsuT = thres
	return otsuT

def ctrStr(imgArr, lb, ub, cutoff):
	hist = histGray(imgArr)
	if dim(imgArr) == 3:
		imgArr = img2hsi(imgArr)[2]
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	minV = 0; dmin = False
	maxV = 255; dmax = False
	img = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	if cutoff == 0:
		for i in range(0, 256):
			if not dmin and hist[i] != 0:
				minV = i
				dmin = True
			if not dmax and hist[255 - i] != 0:
				maxV = 255 - i
				dmax = True
			if dmin and dmax:
				break
	else:
		lower = 0; upper = 0; limit = round(cutoff * sizeX * sizeY)
		for i in range(0, 256):
			if lower < limit:
				lower += hist[i]
			elif not dmin:
				minV = i
				dmin = True
			if upper < limit:
				upper += hist[255 - i]
			elif not dmax:
				maxV = 255 - i
				dmax = True
			if dmin and dmax:
				break
	scale = (ub - lb) / (maxV - minV)
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			img[j][i] = min(max(round((imgArr[j][i] - minV) * scale + lb), 0), 255)
	img = np.array(np.uint8(img))
	return img

def gammaCorr(imgArr, gamma):
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	d = dim(imgArr)
	imgR = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgG = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgB = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	lb = 0 ** gamma; ub = 255 ** gamma
	scale = (255 - 0) / (ub - lb)
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			if d == 3:
				imgR[j][i] = imgArr[j][i][0] ** gamma * scale
				imgG[j][i] = imgArr[j][i][1] ** gamma * scale
				imgB[j][i] = imgArr[j][i][2] ** gamma * scale
			else:
				imgR[j][i] = imgArr[j][i] ** gamma * scale
	if d == 3:
		img = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB))))
	else:
		img = np.array(np.uint8(imgR))
	return img

def adjBright(imgArr, meth):
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	d = dim(imgArr)
	imgR = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgG = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgB = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	if meth == 0: # in = out
		img = imgArr
	elif meth == 1: # log(in) = out
		lb = math.log(0 + 1); ub = math.log(255 + 1)
		scale = (255 - 0) / (ub - lb)
		for i in range(0, sizeX):
			for j in range(0, sizeY):
				if d == 3:
					imgR[j][i] = min(round(math.log(imgArr[j][i][0] + 1) * scale), 255)
					imgG[j][i] = min(round(math.log(imgArr[j][i][1] + 1) * scale), 255)
					imgB[j][i] = min(round(math.log(imgArr[j][i][2] + 1) * scale), 255)
				else:
					imgR[j][i] = min(round(math.log(imgArr[j][i] + 1) * scale), 255)
		if d == 3:
			img = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB))))
		else:
			img = np.array(np.uint8(imgR))
	elif meth == 2: # log(1/in) = out
		lb = math.log(0 + 1); ub = math.log(255 + 1)
		scale = (255 - 0) / (ub - lb)
		for i in range(0, sizeX):
			for j in range(0, sizeY):
				if d == 3:
					imgR[j][i] = min(round(255 - math.log(255 - imgArr[j][i][0] + 1) * scale), 255)
					imgG[j][i] = min(round(255 - math.log(255 - imgArr[j][i][1] + 1) * scale), 255)
					imgB[j][i] = min(round(255 - math.log(255 - imgArr[j][i][2] + 1) * scale), 255)
				else:
					imgR[j][i] = min(round(255 - math.log(255 - imgArr[j][i] + 1) * scale), 255)
		if d == 3:
			img = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB))))
		else:
			img = np.array(np.uint8(imgR))
	elif meth == 3: # sqrt(in) = out
		lb = math.sqrt(0); ub = math.sqrt(255)
		scale = (255 - 0) / (ub - lb)
		for i in range(0, sizeX):
			for j in range(0, sizeY):
				if d == 3:
					imgR[j][i] = min(round(math.sqrt(imgArr[j][i][0]) * scale), 255)
					imgG[j][i] = min(round(math.sqrt(imgArr[j][i][1]) * scale), 255)
					imgB[j][i] = min(round(math.sqrt(imgArr[j][i][2]) * scale), 255)
				else:
					imgR[j][i] = min(round(math.sqrt(imgArr[j][i]) * scale), 255)
		if d == 3:
			img = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB))))
		else:
			img = np.array(np.uint8(imgR))
	elif meth == 4: # in^2 = out
		lb = 0 ** 2; ub = 255 ** 2
		scale = (255 - 0) / (ub - lb)
		for i in range(0, sizeX):
			for j in range(0, sizeY):
				if d == 3:
					imgR[j][i] = min(round(int(imgArr[j][i][0]) ** 2 * scale), 255)
					imgG[j][i] = min(round(int(imgArr[j][i][1]) ** 2 * scale), 255)
					imgB[j][i] = min(round(int(imgArr[j][i][2]) ** 2 * scale), 255)
				else:
					imgR[j][i] = min(round(int(imgArr[j][i]) ** 2 * scale), 255)
		if d == 3:
			img = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB))))
		else:
			img = np.array(np.uint8(imgR))
	elif meth == 5: # exp(in) = out
		base = 1.005
		lb = math.pow(base, 0); ub = math.pow(base, 255)
		scale = (255 - 0) / (ub - lb)
		for i in range(0, sizeX):
			for j in range(0, sizeY):
				if d == 3:
					imgR[j][i] = min(round((math.pow(base, imgArr[j][i][0]) - lb) * scale), 255)
					imgG[j][i] = min(round((math.pow(base, imgArr[j][i][1]) - lb) * scale), 255)
					imgB[j][i] = min(round((math.pow(base, imgArr[j][i][2]) - lb)* scale), 255)
				else:
					imgR[j][i] = min(round((math.pow(base, imgArr[j][i]) - lb) * scale), 255)
		if d == 3:
			img = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB))))
		else:
			img = np.array(np.uint8(imgR))
	elif meth == 6: # 255-in = out
		img = neg(imgArr)
	return img

def enlarge(imgArr, n, meth):
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	cp = dim(imgArr)
	imgR1 = [[-1 for i in range(sizeX)] for j in range(sizeY * n)]
	imgG1 = [[-1 for i in range(sizeX)] for j in range(sizeY * n)]
	imgB1 = [[-1 for i in range(sizeX)] for j in range(sizeY * n)]
	imgR = [[-1 for i in range(sizeX * n)] for j in range(sizeY * n)]
	imgG = [[-1 for i in range(sizeX * n)] for j in range(sizeY * n)]
	imgB = [[-1 for i in range(sizeX * n)] for j in range(sizeY * n)]
	if meth == 0:	#duplication
		for i in range(0, sizeX):
			for j in range(0, sizeY):
				for k in range(0, n):
					if cp == 3:
						imgR1[j * n + k][i] = int(imgArr[j][i][0])
						imgG1[j * n + k][i] = int(imgArr[j][i][1])
						imgB1[j * n + k][i] = int(imgArr[j][i][2])
					else:
						imgR1[j * n + k][i] = int(imgArr[j][i])
		for j in range(0, sizeY * n):
			for i in range(0, sizeX):
				for k in range(0, n):
					imgR[j][i * n + k] = imgR1[j][i]
					if cp == 3:
						imgG[j][i * n + k] = imgG1[j][i]
						imgB[j][i * n + k] = imgB1[j][i]
	elif meth == 1:	#interpolation
		d = (sizeY - 1) / (sizeY * n - 1)
		for i in range(0, sizeX):
			for j in range(0, sizeY * n - 1):
				if cp == 3:
					imgR1[j][i] = int(imgArr[math.floor(j * d)][i][0]) + (int(imgArr[math.floor(j * d) + 1][i][0]) - int(imgArr[math.floor(j * d)][i][0])) * (j * d - math.floor(j * d))
					imgG1[j][i] = int(imgArr[math.floor(j * d)][i][1]) + (int(imgArr[math.floor(j * d) + 1][i][1]) - int(imgArr[math.floor(j * d)][i][1])) * (j * d - math.floor(j * d))
					imgB1[j][i] = int(imgArr[math.floor(j * d)][i][2]) + (int(imgArr[math.floor(j * d) + 1][i][2]) - int(imgArr[math.floor(j * d)][i][2])) * (j * d - math.floor(j * d))
				else:
					imgR1[j][i] = int(imgArr[math.floor(j * d)][i]) + (int(imgArr[math.floor(j * d) + 1][i]) - int(imgArr[math.floor(j * d)][i])) * (j * d - math.floor(j * d))
			if cp == 3:
				imgR1[sizeY * n - 1][i] = int(imgArr[sizeY - 1][i][0])
				imgG1[sizeY * n - 1][i] = int(imgArr[sizeY - 1][i][1])
				imgB1[sizeY * n - 1][i] = int(imgArr[sizeY - 1][i][2])
			else:
				imgR1[sizeY * n - 1][i] = int(imgArr[sizeY - 1][i])
		d = (sizeX - 1) / (sizeX * n - 1)
		for j in range(0, sizeY * n):
			for i in range(0, sizeX * n - 1):
				imgR[j][i] = imgR1[j][math.floor(i * d)] + (imgR1[j][math.floor(i * d) + 1] - imgR1[j][math.floor(i * d)]) * (i * d - math.floor(i * d))
				if cp == 3:
					imgG[j][i] = imgG1[j][math.floor(i * d)] + (imgG1[j][math.floor(i * d) + 1] - imgG1[j][math.floor(i * d)]) * (i * d - math.floor(i * d))
					imgB[j][i] = imgB1[j][math.floor(i * d)] + (imgB1[j][math.floor(i * d) + 1] - imgB1[j][math.floor(i * d)]) * (i * d - math.floor(i * d))
			imgR[j][sizeX * n - 1] = imgR1[sizeY - 1][sizeX - 1]
			if cp == 3:
				imgG[j][sizeX * n - 1] = imgG1[sizeY - 1][sizeX - 1]
				imgB[j][sizeX * n - 1] = imgB1[sizeY - 1][sizeX - 1]
	if cp == 3:
		img = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB))))
	else:
		img = np.array(np.uint8(imgR))
	return img

def shrink(imgArr, n, meth):
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	cp = dim(imgArr)
	nx = math.floor(sizeX / n)
	ny = math.floor(sizeY / n)
	imgR1 = [[-1 for i in range(sizeX)] for j in range(ny)]
	imgG1 = [[-1 for i in range(sizeX)] for j in range(ny)]
	imgB1 = [[-1 for i in range(sizeX)] for j in range(ny)]
	imgR = [[-1 for i in range(nx)] for j in range(ny)]
	imgG = [[-1 for i in range(nx)] for j in range(ny)]
	imgB = [[-1 for i in range(nx)] for j in range(ny)]
	if meth == 0:	#decimation
		for i in range(0, sizeX):
			for j in range(0, ny):
				if cp == 3:
					imgR1[j][i] = int(imgArr[j * n][i][0])
					imgG1[j][i] = int(imgArr[j * n][i][1])
					imgB1[j][i] = int(imgArr[j * n][i][2])
				else:
					imgR1[j][i] = int(imgArr[j * n][i])
		for j in range(0, ny):
			for i in range(0, nx):
				imgR[j][i] = imgR1[j][i * n]
				if cp == 3:
					imgG[j][i] = imgG1[j][i * n]
					imgB[j][i] = imgB1[j][i * n]
	elif meth == 1:	#average
		d = (sizeY - 1) / (ny - 1)
		for i in range(0, sizeX):
			for j in range(0, ny - 1):
				if cp == 3:
					imgR1[j][i] = int(imgArr[math.floor(j * d)][i][0]) + (int(imgArr[math.floor(j * d) + 1][i][0]) - int(imgArr[math.floor(j * d)][i][0])) * (j * d - math.floor(j * d))
					imgG1[j][i] = int(imgArr[math.floor(j * d)][i][1]) + (int(imgArr[math.floor(j * d) + 1][i][1]) - int(imgArr[math.floor(j * d)][i][1])) * (j * d - math.floor(j * d))
					imgB1[j][i] = int(imgArr[math.floor(j * d)][i][2]) + (int(imgArr[math.floor(j * d) + 1][i][2]) - int(imgArr[math.floor(j * d)][i][2])) * (j * d - math.floor(j * d))
				else:
					imgR1[j][i] = int(imgArr[math.floor(j * d)][i]) + (int(imgArr[math.floor(j * d) + 1][i]) - int(imgArr[math.floor(j * d)][i])) * (j * d - math.floor(j * d))

			if cp == 3:
				imgR1[ny - 1][i] = int(imgArr[sizeY - 1][i][0])
				imgG1[ny - 1][i] = int(imgArr[sizeY - 1][i][1])
				imgB1[ny - 1][i] = int(imgArr[sizeY - 1][i][2])
			else:
				imgR1[ny - 1][i] = int(imgArr[sizeY - 1][i])
		d = (sizeX - 1) / (nx - 1)
		for j in range(0, ny):
			for i in range(0, nx - 1):
				imgR[j][i] = imgR1[j][math.floor(i * d)] + (imgR1[j][math.floor(i * d) + 1] - imgR1[j][math.floor(i * d)]) * (i * d - math.floor(i * d))
				if cp == 3:
					imgG[j][i] = imgG1[j][math.floor(i * d)] + (imgG1[j][math.floor(i * d) + 1] - imgG1[j][math.floor(i * d)]) * (i * d - math.floor(i * d))
					imgB[j][i] = imgB1[j][math.floor(i * d)] + (imgB1[j][math.floor(i * d) + 1] - imgB1[j][math.floor(i * d)]) * (i * d - math.floor(i * d))
			imgR[j][nx - 1] = imgR1[ny - 1][sizeX - 1]
			if cp == 3:
				imgG[j][nx - 1] = imgG1[ny - 1][sizeX - 1]
				imgB[j][nx - 1] = imgB1[ny - 1][sizeX - 1]
	if cp == 3:
		img = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB))))
	else:
		img = np.array(np.uint8(imgR))
	return img

def frtt(imgArr, dgr):
	sizeX = len(imgArr[0]); ox = round(sizeX / 2)
	sizeY = len(imgArr); oy = round(sizeY / 2)
	d = dim(imgArr)
	if dgr > 270:
		theta = math.radians(dgr - 270)
		sinT = abs(math.cos(theta)); cosT = abs(math.sin(theta))
	elif dgr > 180:
		theta = math.radians(dgr - 180)
		cosT = abs(math.cos(theta)); sinT = abs(math.sin(theta))
	elif dgr > 90:
		theta = math.radians(dgr - 90)
		sinT = abs(math.cos(theta)); cosT = abs(math.sin(theta))
	else:
		theta = math.radians(dgr)
		cosT = abs(math.cos(theta)); sinT = abs(math.sin(theta))
	dgr = math.radians(dgr)
	sizeNX = round(sizeX * cosT + sizeY * sinT); onx = round(sizeNX / 2)
	sizeNY = round(sizeX * sinT + sizeY * cosT); ony = round(sizeNY / 2)
	imgR = [[0 for i in range(sizeNX)] for j in range(sizeNY)]
	imgG = [[0 for i in range(sizeNX)] for j in range(sizeNY)]
	imgB = [[0 for i in range(sizeNX)] for j in range(sizeNY)]
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			x = i - ox
			y = j - oy
			nx = round(math.cos(dgr) * x - math.sin(dgr) * y) + onx
			ny = round(math.sin(dgr) * x + math.cos(dgr) * y) + ony
			if nx >= 0 and nx < sizeNX and ny >= 0 and ny < sizeNY:
				if d == 3:
					imgR[ny][nx] = imgArr[j][i][0]
					imgG[ny][nx] = imgArr[j][i][1]
					imgB[ny][nx] = imgArr[j][i][2]
				else:
					imgR[ny][nx] = imgArr[j][i]
	if d == 3:
		img = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB))))
	else:
		img = np.array(np.uint8(imgR))
	return img

def brtt(imgArr, dgr):
	sizeX = len(imgArr[0]); ox = round(sizeX / 2)
	sizeY = len(imgArr); oy = round(sizeY / 2)
	d = dim(imgArr)
	if dgr > 270:
		theta = math.radians(dgr - 270)
		sinT = abs(math.cos(theta)); cosT = abs(math.sin(theta))
	elif dgr > 180:
		theta = math.radians(dgr - 180)
		cosT = abs(math.cos(theta)); sinT = abs(math.sin(theta))
	elif dgr > 90:
		theta = math.radians(dgr - 90)
		sinT = abs(math.cos(theta)); cosT = abs(math.sin(theta))
	else:
		theta = math.radians(dgr)
		cosT = abs(math.cos(theta)); sinT = abs(math.sin(theta))
	dgr = math.radians(360 - dgr)
	sizeNX = round(sizeX * cosT + sizeY * sinT); onx = round(sizeNX / 2)
	sizeNY = round(sizeX * sinT + sizeY * cosT); ony = round(sizeNY / 2)
	imgR = [[0 for i in range(sizeNX)] for j in range(sizeNY)]
	imgG = [[0 for i in range(sizeNX)] for j in range(sizeNY)]
	imgB = [[0 for i in range(sizeNX)] for j in range(sizeNY)]
	for i in range(0, sizeNX):
		for j in range(0, sizeNY):
			x = i - onx
			y = j - ony
			nx = round(math.cos(dgr) * x - math.sin(dgr) * y) + ox
			ny = round(math.sin(dgr) * x + math.cos(dgr) * y) + oy
			if nx >= 0 and nx < sizeX and ny >= 0 and ny < sizeY:
				if d == 3:
					imgR[j][i] = imgArr[ny][nx][0]
					imgG[j][i] = imgArr[ny][nx][1]
					imgB[j][i] = imgArr[ny][nx][2]
				else:
					imgR[j][i] = imgArr[ny][nx]
	if d == 3:
		img = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB))))
	else:
		img = np.array(np.uint8(imgR))
	return img

def swap(a, b):
	return [b, a]

def cutRect(imgArr, sx, sy, ex, ey):
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	d = dim(imgArr)
	if sx > ex:
		sx, ex = swap(sx, ex)
	if sy > ey:
		sy, ey = swap(sy, ey)
	w = ex - sx + 1; h = ey - sy + 1
	imgR = [[-1 for i in range(w)] for j in range(h)]
	imgG = [[-1 for i in range(w)] for j in range(h)]
	imgB = [[-1 for i in range(w)] for j in range(h)]
	for i in range(w):
		for j in range(h):
			if d == 3:
				imgR[j][i] = imgArr[sy+j][sx+i][0]
				imgG[j][i] = imgArr[sy+j][sx+i][1]
				imgB[j][i] = imgArr[sy+j][sx+i][2]
			else:
				imgR[j][i] = imgArr[sy+j][sx+i]
	if d == 3:
		img = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB))))
	else:
		img = np.array(np.uint8(imgR))
	return img

def cutElps(imgArr, sx, sy, ex, ey):
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	d = dim(imgArr)
	if sx > ex:
		sx, ex = swap(sx, ex)
	if sy > ey:
		sy, ey = swap(sy, ey)
	w = ex - sx + 1; h = ey - sy + 1
	cx = (sx+ex)/2; cy = (sy+ey)/2
	imgR = [[-1 for i in range(w)] for j in range(h)]
	imgG = [[-1 for i in range(w)] for j in range(h)]
	imgB = [[-1 for i in range(w)] for j in range(h)]
	imgA = [[-1 for i in range(w)] for j in range(h)]
	for i in range(w):
		for j in range(h):
			if d == 3:
				imgR[j][i] = imgArr[sy+j][sx+i][0]
				imgG[j][i] = imgArr[sy+j][sx+i][1]
				imgB[j][i] = imgArr[sy+j][sx+i][2]
			else:
				imgR[j][i] = imgArr[sy+j][sx+i]
				imgG[j][i] = imgArr[sy+j][sx+i]
				imgB[j][i] = imgArr[sy+j][sx+i]
			r = ((((sy+j)-cy)**2)/((h/2)**2)) + ((((sx+i)-cx)**2)/((w/2)**2))
			if r > 1:
				imgA[j][i] = 0
			else:
				imgA[j][i] = 255
	img = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB)), np.array(np.uint8(imgA))))
	return img

def overlap(img1, img2, a):
	x1 = len(img1[0]); x2 = len(img2[0])
	y1 = len(img1); y2 = len(img2)
	if dim(img1) == 1:
		img1 = np.dstack((img1, img1, img1))
	if dim(img2) == 1:
		img2 = np.dstack((img2, img2, img2))
	imgR = [[-1 for i in range(x1)] for j in range(y1)]
	imgG = [[-1 for i in range(x1)] for j in range(y1)]
	imgB = [[-1 for i in range(x1)] for j in range(y1)]
	imgA = [[-1 for i in range(x1)] for j in range(y1)]
	for j in range(0, y1):
		for i in range(0, x1):
			if j < y2 and i < x2:
				imgR[j][i] = min((img2[j, i][0] * a + img1[j][i][0] * (1 - a)), 255)
				imgG[j][i] = min((img2[j, i][1] * a + img1[j][i][1] * (1 - a)), 255)
				imgB[j][i] = min((img2[j, i][2] * a + img1[j][i][2] * (1 - a)), 255)
				imgA[j][i] = 255
			else:
				imgR[j][i] = img1[j][i][0]
				imgG[j][i] = img1[j][i][1]
				imgB[j][i] = img1[j][i][2]
				imgA[j][i] = 255
	img = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB)), np.array(np.uint8(imgA))))
	return img
	
def copyPaste(imgArr, sx, sy):
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	d = dim(imgArr)
	paste = imgArr.copy()
	for i in range(sx, sizeX):
		for j in range(sy, sizeY):
			imgArr[j][i] = paste[j-sy][i-sx]
	return np.array(np.uint8(imgArr))

def sbpln(imgArr):
	if dim(imgArr) == 3:
		imgArr = img2hsi(imgArr)[2]
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	img = [[[-1 for i in range(sizeX)] for j in range(sizeY)] for k in range(8)]
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			v = int(imgArr[j][i])
			for k in range(0, 8):
				img[k][j][i] = (v % 2) * 255
				v //= 2
	imgB = []
	for k in range(0, 8):
		imgB.append(np.array(np.uint8(img[k])))
	return imgB

def gbpln(imgArr):
	if dim(imgArr) == 3:
		imgArr = img2hsi(imgArr)[2]
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	img = [[[-1 for i in range(sizeX)] for j in range(sizeY)] for k in range(8)]
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			v = int(imgArr[j][i])
			b = []
			for k in range(0, 8):
				b.append(v % 2)
				v //= 2
			for k in range(0, 7):
				if b[k] == b[k+1]:
					img[k][j][i] = 0
				else:
					img[k][j][i] = 255
			img[7][j][i] = b[7] * 255
	imgB = []
	for k in range(0, 8):
		imgB.append(np.array(np.uint8(img[k])))
	return imgB

def watermark(img0, img1, img2, img3, img4, img5, img6, img7, imgWM):
	sizeX = len(img0[0])
	sizeY = len(img0)
	wmSizeX = len(imgWM[0])
	wmSizeY = len(imgWM)
	imgB = [img0, img1, img2, img3, img4, img5, img6, img7]
	imgWM = bimg(imgWM, otsu(imgWM))
	img = [[0 for i in range(sizeX)] for j in range(sizeY)]
	imgbpl0 = [[0 for i in range(sizeX)] for j in range(sizeY)]
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			for n in range(7, 0, -1):
				if imgB[n][j][i] == 255:
					img[j][i] += 1
				img[j][i] <<= 1
			if i < wmSizeX and j < wmSizeY:
				if imgWM[j][i] == 255:
					img[j][i] += 1
				imgbpl0[j][i] = imgWM[j][i]
			else:
				if imgB[0][j][i] == 255:
					img[j][i] += 1
				imgbpl0[j][i] = imgB[0][j][i]
	img = np.array(np.uint8(img))
	imgbpl0 = np.array(np.uint8(imgbpl0))
	return [img, imgbpl0]

def addNoise(imgArr):
	import random
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	d = dim(imgArr)
	imgR = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgG = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgB = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	prob = 0.002
	for i in range(sizeX):
		for j in range(sizeY):
			rdn = random.random()
			if rdn < prob:
				imgR[j][i] = 0
				if d == 3:
					imgG[j][i] = 0
					imgB[j][i] = 0
			elif rdn > (1 - prob):
				imgR[j][i] = 255
				if d == 3:
					imgG[j][i] = 255
					imgB[j][i] = 255
			else:
				if d == 3:
					imgR[j][i] = imgArr[j][i][0]
					imgG[j][i] = imgArr[j][i][1]
					imgB[j][i] = imgArr[j][i][2]
				else:
					imgR[j][i] = imgArr[j][i]
	if d == 3:
		imgNs = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB))))
	else:
		imgNs = np.array(np.uint8(imgR))
	return imgNs

def medFltr(imgArr, k, kt, pseudo):
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	d = dim(imgArr)
	imgR = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgG = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgB = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	k //= 2
	sig = 0; noise = 0.000001
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			pr = []; pg = []; pb = []; c = 0
			for ki in range(-k, k + 1):
				for kj in range(-k, k + 1):
					if i + ki >= 0 and i + ki < sizeX and j + kj >= 0 and j + kj < sizeY:
						if kt == 0:	#square kernel
							c += 1
							if d == 3:
								pr.append(imgArr[j+kj][i+ki][0])
								pg.append(imgArr[j+kj][i+ki][1])
								pb.append(imgArr[j+kj][i+ki][2])
							else:
								pr.append(imgArr[j+kj][i+ki])
						elif kt == 1:	#cross kernel
							if ki == 0 or kj == 0:
								c += 1
								if d == 3:
									pr.append(imgArr[j+kj][i+ki][0])
									pg.append(imgArr[j+kj][i+ki][1])
									pb.append(imgArr[j+kj][i+ki][2])
								else:
									pr.append(imgArr[j+kj][i+ki])
			if pseudo == 0:	
				pr.sort();
				imgR[j][i] = pr[c//2]
				if d == 3:
					pg.sort(); pb.sort()
					imgG[j][i] = pg[c//2]
					imgB[j][i] = pb[c//2]
			elif pseudo == 1:	#maxmin
				subLen = c//2 + 1
				sub = list(combinations(pr, subLen))
				maxR = min(list(sub[0]))
				for perm in range(1, len(sub)):
					maxR = max(maxR, min(list(sub[perm])))
				imgR[j][i] = maxR
				if d == 3:
					sub = list(combinations(pg, subLen))
					maxG = min(list(sub[0]))
					for perm in range(1, len(sub)):
						maxG = max(maxG, min(list(sub[perm])))
					sub = list(combinations(pb, subLen))
					maxB = min(list(sub[0]))
					for perm in range(1, len(sub)):
						maxB = max(maxB, min(list(sub[perm])))
					imgG[j][i] = maxG
					imgB[j][i] = maxB
			elif pseudo == 2:	#minmax
				subLen = c//2 + 1
				sub = list(combinations(pr, subLen))
				minR = max(list(sub[0]))
				for perm in range(1, len(sub)):
					minR = min(minR, max(list(sub[perm])))
				imgR[j][i] = minR
				if d == 3:
					sub = list(combinations(pg, subLen))
					minG = max(list(sub[0]))
					for perm in range(1, len(sub)):
						minG = min(minG, max(list(sub[perm])))
					sub = list(combinations(pb, subLen))
					minB = max(list(sub[0]))
					for perm in range(1, len(sub)):
						minB = min(minB, max(list(sub[perm])))
					imgG[j][i] = minG
					imgB[j][i] = minB
			if d == 3:
				sig += int(imgArr[j][i][0]) ** 2 + int(imgArr[j][i][1]) ** 2 + int(imgArr[j][i][2]) ** 2
				noise += (int(imgArr[j][i][0]) - int(imgR[j][i])) ** 2 + (int(imgArr[j][i][1]) - int(imgG[j][i])) ** 2 + (int(imgArr[j][i][2]) - int(imgB[j][i])) ** 2
			else:
				sig += int(imgArr[j][i]) ** 2
				noise += (int(imgArr[j][i]) - int(imgR[j][i])) ** 2
	if d == 3:
		img = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB))))
	else:
		img = np.array(np.uint8(imgR))
	snr = 10 * math.log10(sig/noise)
	return [img, snr]

def meanFltr(imgArr, k, kt):
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	d = dim(imgArr)
	imgR = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgG = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgB = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	k //= 2
	sig = 0; noise = 0.000001
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			pr = 0; pg = 0; pb = 0; c = 0
			for ki in range(-k, k + 1):
				for kj in range(-k, k + 1):
					if i + ki >= 0 and i + ki < sizeX and j + kj >= 0 and j + kj < sizeY:
						if kt == 0:	#square kernel
							c += 1
							if d == 3:
								pr += imgArr[j+kj][i+ki][0]
								pg += imgArr[j+kj][i+ki][1]
								pb += imgArr[j+kj][i+ki][2]
							else:
								pr += imgArr[j+kj][i+ki]
						elif kt == 1:	#cross kernel
							if ki == 0 or kj == 0:
								c += 1
								if d == 3:
									pr += imgArr[j+kj][i+ki][0]
									pg += imgArr[j+kj][i+ki][1]
									pb += imgArr[j+kj][i+ki][2]
								else:
									pr += imgArr[j+kj][i+ki]
			imgR[j][i] = pr//c
			if d == 3:
				imgG[j][i] = pg//c
				imgB[j][i] = pb//c
				sig += int(imgArr[j][i][0]) ** 2 + int(imgArr[j][i][1]) ** 2 + int(imgArr[j][i][2]) ** 2
				noise += (int(imgArr[j][i][0]) - int(imgR[j][i])) ** 2 + (int(imgArr[j][i][1]) - int(imgG[j][i])) ** 2 + (int(imgArr[j][i][2]) - int(imgB[j][i])) ** 2
			else:
				sig += int(imgArr[j][i]) ** 2
				noise += (int(imgArr[j][i]) - int(imgR[j][i])) ** 2
	if d == 3:
		img = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB))))
	else:
		img = np.array(np.uint8(imgR))
	snr = 10 * math.log10(sig/noise)
	return [img, snr]

def outlier(imgArr, thres):
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	d = dim(imgArr)
	imgR = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgG = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgB = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	sig = 0; noise = 0.000001
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			pr = 0; pg = 0; pb = 0; c = 0
			for ki in range(-1, 2):
				for kj in range(-1, 2):
					if i + ki >= 0 and i + ki < sizeX and j + kj >= 0 and j + kj < sizeY:
						if ki != 0 and kj != 0:
							c += 1
							if d == 3:
								pr += imgArr[j+kj][i+ki][0]
								pg += imgArr[j+kj][i+ki][1]
								pb += imgArr[j+kj][i+ki][2]
							else:
								pr += imgArr[j+kj][i+ki]
			pr = round(pr/c);
			if d == 3:
				pg = round(pg/c); pb = round(pb/c)
				if imgArr[j][i][0] - pr > thres:
					imgR[j][i] = pr
				else:
					imgR[j][i] = imgArr[j][i][0]
				if imgArr[j][i][1] - pg > thres:
					imgG[j][i] = pg
				else:
					imgG[j][i] = imgArr[j][i][1]
				if imgArr[j][i][2] - pb > thres:
					imgB[j][i] = pb
				else:
					imgB[j][i] = imgArr[j][i][2]
				sig += int(imgArr[j][i][0]) ** 2 + int(imgArr[j][i][1]) ** 2 + int(imgArr[j][i][2]) ** 2
				noise += (int(imgArr[j][i][0]) - int(imgR[j][i])) ** 2 + (int(imgArr[j][i][1]) - int(imgG[j][i])) ** 2 + (int(imgArr[j][i][2]) - int(imgB[j][i])) ** 2
			else:
				if imgArr[j][i] - pr > thres:
					imgR[j][i] = pr
				else:
					imgR[j][i] = imgArr[j][i]
				sig += int(imgArr[j][i]) ** 2
				noise += (int(imgArr[j][i]) - int(imgR[j][i])) ** 2
	if d == 3:
		img = np.dstack((np.array(np.uint8(imgR)), np.array(np.uint8(imgG)), np.array(np.uint8(imgB))))
	else:
		img = np.array(np.uint8(imgR))
	snr = 10 * math.log10(sig/noise)
	return [img, snr]

def highPass(imgArr, k):
	if dim(imgArr) == 3:
		imgArr = img2hsi(imgArr)[2]
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	imgE = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	k //= 2
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			other = 0; c = 0
			for ki in range(-k, k + 1):
				for kj in range(-k, k + 1):
					if i + ki >= 0 and i + ki < sizeX and j + kj >= 0 and j + kj < sizeY:
						if not (ki == 0 and kj == 0):
							c += 1
							other += imgArr[j+kj][i+ki]
			imgE[j][i] = min(max(round((imgArr[j][i] * c - other) / (c + 1)), 0), 255)
	imgE = np.array(np.uint8(imgE))
	return imgE

def highBoost(imgArr, a):
	if dim(imgArr) == 3:
		imgArr = img2hsi(imgArr)[2]
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	imgE = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			other = 0; c = 0
			for ki in range(-1, 2):
				for kj in range(-1, 2):
					if i + ki >= 0 and i + ki < sizeX and j + kj >= 0 and j + kj < sizeY:
						if not (ki == 0 and kj == 0):
							c += 1
							other += imgArr[j+kj][i+ki]
			imgE[j][i] = min(max(round((imgArr[j][i] * ((c+1) * a - 1) - other) / (c + 1)), 0), 255)
	imgE = np.array(np.uint8(imgE))
	return imgE

def roberts(imgArr):
	if dim(imgArr) == 3:
		imgArr = img2hsi(imgArr)[2]
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	imgX = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgY = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	img = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			if i + 1 < sizeX and j + 1 < sizeY:
				imgX[j][i] = abs(int(imgArr[j+1][i+1]) - int(imgArr[j][i]))
				imgY[j][i] = abs(int(imgArr[j+1][i]) - int(imgArr[j][i+1]))
			else:
				imgX[j][i] = 0
				imgY[j][i] = 0
			img[j][i] = min((imgX[j][i] + imgY[j][i]), 255)
	imgX = np.array(np.uint8(imgX)); imgY = np.array(np.uint8(imgY)); img = np.array(np.uint8(img))
	return [imgX, imgY, img]

def sobel(imgArr):
	if dim(imgArr) == 3:
		imgArr = img2hsi(imgArr)[2]
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	imgX = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgY = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	img = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			for ki in range(-1, 2):
				for kj in range(-1, 2):
					i_legal = (i + ki >= 0) and (i + ki < sizeX)
					j_legal = (j + kj >= 0) and (j + kj < sizeY)
					both_legal = i_legal and j_legal
					if ki != 0 and kj != 0:
						weight = 1
					else:
						weight = 2
					if both_legal:
						imgX[j][i] += int(imgArr[j+kj][i+ki]) * ki * weight
						imgY[j][i] += int(imgArr[j+kj][i+ki]) * -kj * weight
					else:
						if not both_legal:
							imgX[j][i] += int(imgArr[j][i]) * ki * weight
							imgY[j][i] += int(imgArr[j][i]) * -kj * weight
						elif not i_legal:
							imgX[j][i] += int(imgArr[j+kj][i]) * ki * weight
							imgY[j][i] += int(imgArr[j+kj][i]) * -kj * weight
						else:
							imgX[j][i] += int(imgArr[j][i+ki]) * ki * weight
							imgY[j][i] += int(imgArr[j][i+ki]) * -kj * weight
			imgX[j][i] = min(abs(imgX[j][i]), 255)
			imgY[j][i] = min(abs(imgY[j][i]), 255)
			img[j][i] = min(imgX[j][i]+imgY[j][i], 255)
	imgX = np.array(np.uint8(imgX)); imgY = np.array(np.uint8(imgY)); img = np.array(np.uint8(img))
	return [imgX, imgY, img]

def prewitt(imgArr):
	if dim(imgArr) == 3:
		imgArr = img2hsi(imgArr)[2]
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	imgX = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgY = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	img = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			for ki in range(-1, 2):
				for kj in range(-1, 2):
					i_legal = (i + ki >= 0) and (i + ki < sizeX)
					j_legal = (j + kj >= 0) and (j + kj < sizeY)
					both_legal = i_legal and j_legal
					if both_legal:
						imgX[j][i] += int(imgArr[j+kj][i+ki]) * ki
						imgY[j][i] += int(imgArr[j+kj][i+ki]) * -kj
					else:
						if not both_legal:
							imgX[j][i] += int(imgArr[j][i]) * ki
							imgY[j][i] += int(imgArr[j][i]) * -kj
						elif not i_legal:
							imgX[j][i] += int(imgArr[j+kj][i]) * ki
							imgY[j][i] += int(imgArr[j+kj][i]) * -kj
						else:
							imgX[j][i] += int(imgArr[j][i+ki]) * ki
							imgY[j][i] += int(imgArr[j][i+ki]) * -kj
			imgX[j][i] = min(abs(imgX[j][i]), 255)
			imgY[j][i] = min(abs(imgY[j][i]), 255)
			img[j][i] = min(imgX[j][i]+imgY[j][i], 255)
	imgX = np.array(np.uint8(imgX)); imgY = np.array(np.uint8(imgY)); img = np.array(np.uint8(img))
	return [imgX, imgY, img]

def edgeCrsp(imgArr, imgBlur):
	if dim(imgArr) == 3:
		imgArr = img2hsi(imgArr)[2]
	if dim(imgBlur) == 3:
		imgBlur = img2hsi(imgBlur)[2]
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	img = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	for i in range(0, sizeX):
		for j in range(0, sizeY):
			img[j][i] = min(max(imgArr[j][i] * 2 - imgBlur[j][i], 0), 255)
	img = np.array(np.uint8(img))
	return img

def calSNR(img1, img2):
	w1, h1 = sz(img1)
	w2, h2 = sz(img2)
	if not (w1 == w2 and h1 == h2):
		return -1
	if dim(img1) == 1:
		img1 = np.dstack((img1, img1, img1))
	if dim(img2) == 1:
		img2 = np.dstack((img2, img2, img2))
	sig = 0; noise = 0.000001
	for i in range(0, w1):
		for j in range(0, h1):
			sig += int(img1[j][i][0]) ** 2 + int(img1[j][i][1]) ** 2 + int(img1[j][i][2]) ** 2
			noise += (int(img1[j][i][0]) - int(img2[j][i][0])) ** 2 + (int(img1[j][i][1]) - int(img2[j][i][1])) ** 2 + (int(img1[j][i][2]) - int(img2[j][i][2])) ** 2
	snr = 10 * math.log10(sig/noise)
	return snr

def connComp(imgArr, thres):
	imgArr = bimg(imgArr, thres)
	c = histGray(imgArr)
	if c[0] < c[255]:
		imgArr = neg(imgArr)
	sizeX = len(imgArr[0])
	sizeY = len(imgArr)
	compSet = [[0 for i in range(sizeX)] for j in range(sizeY)]
	setTable = {}; setTable[0] = 0; setN = 1
	for i in range(sizeX):
		for j in range(sizeY):
			if imgArr[j][i] == 255:
				p1 = 0; p2 = 0; p3 = 0; p4 = 0
				left = (i - 1) >= 0
				up = (j - 1) >= 0
				right = (i + 1) < sizeX
				if left and up:
					p1 = compSet[j - 1][i - 1]
				if up:
					p2 = compSet[j - 1][i]
				if up and right:
					p3 = compSet[j - 1][i + 1]
				if left:
					p4 = compSet[j][i - 1]
				
				prevSet = set([p1, p2, p3, p4])
				if len(prevSet) == 1 and max(prevSet) == 0:
					setTable[setN] = setN
					compSet[j][i] = setN
					setN += 1
				else:
					setMerge = max(prevSet)
					compSet[j][i] = setTable[setMerge]
					for k in range(setN):
						if setTable[k] in prevSet and setTable[k] != 0:
							setTable[k] = setTable[setMerge]
	comp = list(set(setTable.values()) - {0})
	color = np.linspace(55, 255, num = len(comp))
	for i in range(len(color)):
		color[i] = round(color[i])
	for i in range(sizeX):
		for j in range(sizeY):
			if compSet[j][i] != 0:
				cp = comp.index(setTable[compSet[j][i]])
				compSet[j][i] = color[cp]
	return [np.array(np.uint8(compSet)), len(comp)]
