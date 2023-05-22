import numpy as np
from PIL import Image

def u2le(s):
	return s[2:4]+s[0:2]

def u4le(s):
	return s[4:6]+s[2:4]+s[0:2]

def signInt(s, b):
	v = int(s, 16)
	if v & (1 << b-1):
		v -= 1 << b
	return v

def hex2bit(s):
	bs = ''
	for i in range(0, len(s)):
		d = int(s[i], 16)
		b = ''
		for j in range(0, 4):
			if d % 2 == 0:
				b = '0' + b
			else:
				b = '1' + b
				d //= 2
		bs += b
	return bs

def getImg32(sizeX, sizeY, img):
	ci = 0
	cx = 0
	cy = sizeY - 1
	imgR = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgG = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgB = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgA = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	while ci < sizeX*sizeY:
		imgB[cy][cx] = int(img[ci*8:ci*8+2], 16)
		imgG[cy][cx] = int(img[ci*8+2:ci*8+4], 16)
		imgR[cy][cx] = int(img[ci*8+4:ci*8+6], 16)
		imgA[cy][cx] = int(img[ci*8+6:ci*8+8], 16)
		ci += 1
		cx += 1
		if cx == sizeX:
			cy -= 1
			cx = 0
	imgR = np.array(np.uint8(imgR)); imgG = np.array(np.uint8(imgG)); imgB = np.array(np.uint8(imgB))
	imgArr = np.dstack((imgR, imgG, imgB))
	#imgArr = Image.fromarray(imgArr)
	return imgArr

def getImg24(sizeX, sizeY, img):
	ci = 0
	cx = 0
	cy = sizeY - 1
	imgR = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgG = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgB = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	while ci < sizeX*sizeY:
		imgB[cy][cx] = int(img[ci*6:ci*6+2], 16)
		imgG[cy][cx] = int(img[ci*6+2:ci*6+4], 16)
		imgR[cy][cx] = int(img[ci*6+4:ci*6+6], 16)
		ci += 1
		cx += 1
		if cx == sizeX:
			cy -= 1
			cx = 0
	imgR = np.array(np.uint8(imgR)); imgG = np.array(np.uint8(imgG)); imgB = np.array(np.uint8(imgB))
	imgArr = np.dstack((imgR, imgG, imgB))
	#imgArr = Image.fromarray(imgArr)
	return imgArr

def getImgCp(sizeX, sizeY, bpp, cp, img):
	if bpp == 1:
		img = hex2bit(img)
	ci = 0
	cx = 0
	cy = sizeY - 1
	imgR = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgG = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgB = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	while ci < sizeX*sizeY:
		if bpp == 8:
			imgB[cy][cx] = cp[int(img[ci:ci+2], 16)][0]
			imgG[cy][cx] = cp[int(img[ci:ci+2], 16)][1]
			imgR[cy][cx] = cp[int(img[ci:ci+2], 16)][2]
			ci += 2
		elif bpp == 4:
			imgB[cy][cx] = cp[int(img[ci], 16)][0]
			imgG[cy][cx] = cp[int(img[ci], 16)][1]
			imgR[cy][cx] = cp[int(img[ci], 16)][2]
			ci += 1
		elif bpp == 1:
			imgB[cy][cx] = cp[int(img[ci])][0]
			imgG[cy][cx] = cp[int(img[ci])][1]
			imgR[cy][cx] = cp[int(img[ci])][2]
			ci += 1
		cx += 1
		if cx == sizeX:
			cy -= 1
			cx = 0
	imgR = np.array(np.uint8(imgR)); imgG = np.array(np.uint8(imgG)); imgB = np.array(np.uint8(imgB))
	imgArr = np.dstack((imgR, imgG, imgB))
	#imgArr = Image.fromarray(np.uint8(imgArr))
	return imgArr
	
def decBmp(fn):
	img = open(fn, 'rb')
	mgc = img.read(2).hex()
	sz = img.read(4).hex(); sz = int(u4le(sz), 16)
	rsv1 = img.read(2).hex()
	rsv2 = img.read(2).hex()
	stAdr = img.read(4).hex(); stAdr = int(u4le(stAdr), 16)
	hdrSz = img.read(4).hex(); hdrSz = int(u4le(hdrSz), 16)
	
	if mgc == '424d':
		info = 'File: BMP'
	else:
		return [-1]
	info += '\nSize: ' + str(sz) + ' bytes'
	info += '\nReserved[6:8] (hex): ' + rsv1
	info += '\nReserved[8:10] (hex): ' + rsv2
	info += '\nStarting address: ' + str(stAdr)
	if hdrSz == 12:
		info += '\nHeader: OS/2 V1'
		width = img.read(2).hex(); width = int(u2le(width), 16)
		height = img.read(2).hex(); height = int(u2le(height), 16)
		cpn = img.read(2).hex(); cpn = int(u2le(cpn), 16)
		bpp = img.read(2).hex(); bpp = int(u2le(bpp), 16)
	elif hdrSz >= 40:
		if hdrSz == 40:
			info += '\nHeader: Windows V3'
		elif hdrSz == 108:
			info += '\nHeader: Windows V4'
		elif hdrSz == 124:
			info += '\nHeader: Windows V5'
		width = img.read(4).hex(); width = signInt(u2le(width), 32)
		height = img.read(4).hex(); height = signInt(u2le(height), 32)
		cpn = img.read(2).hex(); cpn = int(u2le(cpn), 16)
		bpp = img.read(2).hex(); bpp = int(u2le(bpp), 16)	
		cpr = img.read(4).hex(); cpr = int(u4le(cpr), 16)
		imgSz = img.read(4).hex(); imgSz = int(u4le(imgSz), 16)
		hres = img.read(4).hex(); hres = int(u4le(hres), 16)
		vres = img.read(4).hex(); vres = int(u4le(vres), 16)
		uc = img.read(4).hex(); uc = int(u4le(uc), 16)
		iuc = img.read(4).hex(); iuc = int(u4le(iuc), 16)

		info += '\nWidth: ' + str(width)
		info += '\nHeight: ' + str(height)
		if cpn == 1:
			info += '\nNumber of color planes: 1 (valid)'
		else:
			info += '\nNumber of color planes: ' + str(cpn) + ' (invalid)'
		info += '\nBitsPerPixel: ' + str(bpp)
		if cpr == 0:
			info += '\nCompression method: None'
		elif cpr == 1:
			info += '\nCompression method: RLE 8-bit/pixel'
		elif cpr == 2:
			info += '\nCompression method: RLE 4-bit/pixel'
		elif cpr == 3:
			info += '\nCompression method: Bit field'
		elif cpr == 4:
			info += '\nCompression method: JPEG'
		elif cpr == 5:
			info += '\nCompression method: PNG'
		info += '\nImage size: ' + str(imgSz)
		info += '\nHorizontal resolution (pixel per meter): ' + str(hres)
		info += '\nVertical resolution (pixel per meter): ' + str(vres)
		info += '\nUsed colors: ' + str(uc)
		info += '\nImportant used colors: ' + str(iuc)
		
		img.read(hdrSz-40)
		cp = img.read(stAdr-(14+hdrSz)).hex()
		tmp = []; i = 0
		while i < len(cp):
			tmp.append([int(cp[i:i+2], 16), int(cp[i+2:i+4], 16), int(cp[i+4:i+6], 16)])
			i += 8
		cp = tmp
		r = img.read().hex()
		if bpp == 32:
			imgArr = getImg32(width, height, r)
		elif bpp == 24:
			imgArr = getImg24(width, height, r)
		elif bpp == 8 or bpp == 4 or bpp == 1:
			imgArr = getImgCp(width, height, bpp, cp, r)
		else:
			return [info]
	
	img.close()
	return [info, imgArr]
