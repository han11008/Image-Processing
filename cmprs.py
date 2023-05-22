from os import remove
import func
import numpy as np

class treeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
	def merge(self, t1, t2):
		self.left = t1
		self.right = t2

def huffman(imgArr, fn = 'encd.txt'):
	rtnHist = []
	if func.dim(imgArr) == 3:
		histR, histG, histB = func.histRGB(imgArr)
		hist = []
		for i in range(256):
			count = histR[i] + histG[i] + histB[i]
			if count != 0:
				if len(hist) == 0:
					hist.append((count, i))
				else:
					for j in range(len(hist)):
						if count < hist[j][0]:
							hist.insert(j, (count, i))
							break
						elif j == len(hist) - 1:
							hist.append((count, i))
			rtnHist.append(count)
	else:
		histG = func.histGray(imgArr)
		hist = []
		for i in range(256):
			if histG[i] != 0:
				if len(hist) == 0:
					hist.append((histG[i], i))
				else:
					for j in range(len(hist)):
						if histG[i] < hist[j][0]:
							hist.insert(j, (histG[i], i))
							break
						elif j == len(hist) - 1:
							hist.append((histG[i], i))
			rtnHist.append(histG[i])
	
	treeRoot = cnstrTree(hist)
	table = traversal(treeRoot, '', [])
	tableDict = {}
	for i in range(len(table)):
		tableDict[table[i][0]] = table[i][1]
	w, h = func.sz(imgArr)
	d = func.dim(imgArr)
	encd = ''
	if d == 3:
		for k in range(3):
			for i in range(w):
				for j in range(h):
					encd += tableDict[imgArr[j][i][k]]
	else:
		for i in range(w):
			for j in range(h):
				encd += tableDict[imgArr[j][i]]
	fp = open('tmp/'+fn, 'w')
	fp.write(str(w)+','+str(h)+','+str(d)+'\n')
	fp.write(str(len(tableDict))+'\n')
	k = list(tableDict.keys())
	v = list(tableDict.values())
	for i in range(len(k)):
		fp.write(str(k[i])+','+v[i]+'\n')
	fp.write(encd)
	fp.close()
	
	total = w * h
	table = []
	for i in range(256):
		if rtnHist[i] != 0:
			table.append([str(i), str(round((rtnHist[i]/total)*100, 2))+'%', tableDict[i]])
	ratio = ((d*h*w*8)/len(encd)) * 100
	return [table, ratio]

def cnstrTree(hist):
	forest = []
	while len(hist) > 1:
		if hist[0][1] == -1 or hist[1][1] == -1:
			if hist[0][1] != -1:
				t0 = treeNode(hist[0])
			else:
				t0 = None
			if hist[1][1] != -1:
				t1 = treeNode(hist[1])
			else:
				t1 = None
			chop = []
			for i in range(len(forest)):
				if forest[i].val == hist[0]:
					t0 = forest[i]; chop.append(t0)
				elif forest[i].val == hist[1]:
					t1 = forest[i]; chop.append(t1)
				if t0 != None and t1 != None:
					break
			for i in range(len(chop)):
				forest.remove(chop[i])
			root = treeNode((t0.val[0] + t1.val[0], -1))
			root.merge(t0, t1)
			del hist[0:2]
			for i in range(len(hist)):
				if root.val[0] < hist[i][0]:
					hist.insert(i, root.val)
					break
				elif i == len(hist) - 1:
					hist.append(root.val)
			forest.append(root)
		else:
			t0 = treeNode(hist[0]); t1 = treeNode(hist[1])
			root = treeNode((t0.val[0] + t1.val[0], -1))
			root.merge(t0, t1)
			del hist[0:2]
			for i in range(0, len(hist)):
				if root.val[0] < hist[i][0]:
					hist.insert(i, root.val)
					break
				elif i == len(hist) - 1:
					hist.append(root.val)
			forest.append(root)
	return forest[0]

def traversal(node, cd, table):
	if node != None:
		traversal(node.left, cd + '0', table)
		traversal(node.right, cd + '1', table)
		if node.val[1] != -1:
			table.append((node.val[1], cd))
		return table

def decd(fn = 'encd.txt'):
	cnt = open('tmp/'+fn, 'r').readlines()
	table = {}
	tmp = cnt[0].split(',')
	w = int(tmp[0]); h = int(tmp[1]); d = int(tmp[2])
	for i in range(2, int(cnt[1])+2):
		tmp = cnt[i].split(',')
		table[tmp[1].split('\n')[0]] = int(tmp[0])
	k = list(table.keys())
	cnt = cnt[-1]
	img = [[[-1 for i in range(w)] for j in range(h)] for k in range(d)]
	fillX = 0; fillY = 0; fillC = 0; tmp = ''
	for i in range(len(cnt)):
		tmp += cnt[i]
		if tmp in k:
			if fillC >= d or fillX >= w or fillY >= h:
				print(fillC, d, fillY, h, fillX, w, i)
			img[fillC][fillY][fillX] = table[tmp]
			tmp = ''; fillY += 1
			if fillY == h:
				fillY = 0; fillX += 1;
				if fillX == w:
					fillX = 0; fillC += 1
	if d == 3:
		imgRB = np.dstack((np.array(np.uint8(img[0])), np.array(np.uint8(img[1])), np.array(np.uint8(img[2]))))
	else:
		imgRB = np.array(np.uint8(img[0]))
	return imgRB
