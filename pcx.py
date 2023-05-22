import numpy as np
from PIL import Image

def u2le(s):
	return s[2:4]+s[0:2]

def cpn3(sizeX, sizeY, img):
	ci = 0
	cx = 0
	cy = 0
	rgb = 0
	imgR = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgG = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgB = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	while cy < sizeY:
		p = int(img[ci:ci+2], 16); ci += 2
		if p > 192:
			pn = int(img[ci:ci+2], 16); ci += 2
			for i in range(0, p-192):
				if rgb == 0:
					imgR[cy][cx] = pn
					cx += 1
					if cx == sizeX:
						ci += 2
						rgb = 1
						cx = 0
				elif rgb == 1:
					imgG[cy][cx] = pn
					cx += 1
					if cx == sizeX:
						ci += 2
						rgb = 2
						cx = 0
				elif rgb == 2:
					imgB[cy][cx] = pn
					cx += 1
					if cx == sizeX:
						ci += 2
						rgb = 0
						cy += 1
						cx = 0
		else:
			if rgb == 0:
				imgR[cy][cx] = p
				cx += 1
				if cx == sizeX:
					ci += 2
					rgb = 1
					cx = 0
			elif rgb == 1:
				imgG[cy][cx] = p
				cx += 1
				if cx == sizeX:
					ci += 2
					rgb = 2
					cx = 0
			elif rgb == 2:
				imgB[cy][cx] = p
				cx += 1
				if cx == sizeX:
					ci += 2
					rgb = 0
					cy += 1
					cx = 0

	imgR = np.array(np.uint8(imgR)); imgG = np.array(np.uint8(imgG)); imgB = np.array(np.uint8(imgB))
	imgArr = np.dstack((imgR, imgG, imgB))
	#imgArr = Image.fromarray(np.uint8(imgArr))
	return imgArr

def getClrPlt(plt):
	imgR = [[-1 for i in range(256)] for j in range(256)]
	imgG = [[-1 for i in range(256)] for j in range(256)]
	imgB = [[-1 for i in range(256)] for j in range(256)]
	c = 0; dc = 0
	r = 0; dr = 0
	for i in range(0, 256):
		for j in range(0, 256):
			imgR[j][i] = int(plt[c:c+2], 16)
			imgG[j][i] = int(plt[c+2:c+4], 16)
			imgB[j][i] = int(plt[c+4:c+6], 16)
			dc += 1
			if dc == 16:
				c += 6
				dc = 0
		dr += 1
		if dr == 16:
			r += 1
			dr = 0
		c = r * 16
	
	imgR = np.array(np.uint8(imgR)); imgG = np.array(np.uint8(imgG)); imgB = np.array(np.uint8(imgB))
	imgArr = np.dstack((imgR, imgG, imgB))
	return imgArr

def cpn1(sizeX, sizeY, img):
	ci = 0
	cx = 0
	cy = 0
	plt = img[-1536:]	
	imgR = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgG = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	imgB = [[-1 for i in range(sizeX)] for j in range(sizeY)]
	while cy < sizeY:
		p = int(img[ci:ci+2], 16); ci += 2
		if p > 192:
			pn = int(img[ci:ci+2], 16); ci += 2
			for i in range(0, p-192):
				s = pn * 6
				imgR[cy][cx] = int(plt[s:s+2], 16)
				imgG[cy][cx] = int(plt[s+2:s+4], 16)
				imgB[cy][cx] = int(plt[s+4:s+6], 16)
				cx += 1
				if cx == sizeX:
					cy += 1
					cx = 0
		else:
			s = p * 6
			imgR[cy][cx] = int(plt[s:s+2], 16)
			imgG[cy][cx] = int(plt[s+2:s+4], 16)
			imgB[cy][cx] = int(plt[s+4:s+6], 16)
			cx += 1
			if cx == sizeX:
				cy += 1
				cx = 0

	pltArr = getClrPlt(plt)
	imgR = np.array(np.uint8(imgR)); imgG = np.array(np.uint8(imgG)); imgB = np.array(np.uint8(imgB))
	imgArr = np.dstack((imgR, imgG, imgB))
	#imgArr = Image.fromarray(np.uint8(imgArr))
	return [imgArr, pltArr]

def decPcx(fn):
	img = open(fn, 'rb')
	header = img.read(128).hex()
	mf = header[0:2]
	ver = header[2:4]
	encd = header[4:6]
	bpp = header[6:8]
	minX = header[8:12];	minX = int(u2le(minX), 16)
	minY = header[12:16];	minY = int(u2le(minY), 16) 
	maxX = header[16:20];	maxX = int(u2le(maxX), 16)
	maxY = header[20:24];	maxY = int(u2le(maxY), 16)
	hdpi = header[24:28];	hdpi = int(u2le(hdpi), 16)
	vdpi = header[28:32];	vdpi = int(u2le(vdpi), 16)
	cm = ''
	for i in range(0, 4):
		cm += header[16*i+32:16*i+32+16]
		if i < 3:
			cm += '\n'
	rsv = header[128:130];	rsv = int(rsv, 16)
	cpn = header[130:132];	cpn = int(cpn, 16)
	bpl = header[132:136];	bpl = int(u2le(bpl), 16)
	plt = header[136:140];	plt = int(u2le(plt), 16)
	hs = header[140:144];	hs = int(u2le(hs), 16)
	vs = header[144:148];	vs = int(u2le(vs), 16)
	fill = header[148:256]

	if mf != '0a':
		return [-1]
	info = 'Manufacturer: Zsoft'
	if ver == '00':
		info += '\nVersion: PC Paintbrush version 2.5 using a fixed EGA palette'
	elif ver == '02':
		info +='\nVersion: PC Paintbrush version 2.8 using a modifiable EGA palette'
	elif ver == '03':
		info += '\nVersion: PC Paintbrush version 2.8 using no palette'
	elif ver == '04':
		info += '\nVersion: PC for Windows'
	elif ver == '05':
		info += '\nVersion: PC Paintbrush version 3.0,  including 24-bit images'
	if encd == '01':
		info +='\nEncoding: RLE'
	if bpp == '01':
		info += '\nBitsPerPixel: 1 (2 colors)'
	elif bpp == '02':
		info += '\nBitsPerPixel: 2 (4 colors)'
	elif bpp == '04':
		info += '\nBitsPerPixel: 4 (16 colors)'
	elif bpp == '08':
		info += '\nBitsPerPixel: 8 (256 colors)'
	sizeX = maxX - minX + 1
	sizeY = maxY - minY + 1
	info += '\nSize: ' + str(sizeX*sizeY) + ' (width = ' + str(sizeX) + ', height = ' + str(sizeY) + ')'
	info += '\nHorizontal DPI: ' + str(hdpi)
	info += '\nVertical DPI: ' + str(vdpi)
	info += '\nColormap (hex):\n' + cm
	info += '\nReserved byte: ' + str(rsv)
	info += '\nNumber of color planes: ' + str(cpn)
	info += '\nBytesPerLine: ' + str(bpl)
	if plt == 1:
		info += '\nPalette: color/BW'
	elif plt == 2:
		info += '\nPalette: grayscale'
	info += '\nHorizontal screen size: ' + str(hs)
	info += '\nVertical screen size: ' + str(vs)
	allZero = True
	for i in range(0, 108):
		if fill[i] != '0':
			allZero = False
			info += '\nFiller: not all bytes are set to 0'
			break
	if allZero == True:
		info += '\nFiller: all bytes are set to 0'
	
	if ver == '05' and cpn == 1:
		r = img.read().hex()
		imgArr, clrPlt = cpn1(sizeX, sizeY, r)
		img.close()
		return [info, imgArr, clrPlt]
	elif ver == '05' and cpn == 3:
		r = img.read().hex()
		imgArr = cpn3(sizeX, sizeY, r)
		img.close()
		return [info, imgArr]

