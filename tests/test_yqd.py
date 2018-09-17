# -*- coding: utf-8 -*-
"""
Created on 2018
"""

from yahoo_quote import yqd
import json
import numpy as np
def load_quote(ticker):
	print('===', ticker, '===')
	#print(yqd.load_yahoo_quote(ticker, '20170515', '20170517'))
	#print(yqd.load_yahoo_quote(ticker, '20170515', '20170517', 'dividend'))
	#print(yqd.load_yahoo_quote(ticker, '20170515', '20170517', 'split'))
	data = yqd.load_yahoo_quote(ticker, '20170101', '20171231')
	# save in csv
	with open('one.json', 'w') as outfile:
		json.dump(data, outfile)

def read_data(filename='one.json'):
	with open(filename) as f:
		data = json.load(f)
	listOpen = []
	listClose = []
	listHigh = []
	listLow = []
	listVolume = []
	listVola = []
	listAvg = []
	listNormToAvg = []
	closeDiffToAvg = []
	highLowPerc = []
	data.pop()
	data.pop(0)
	for part in data:
		arrayPart =  part.split(',')
		dateStr = arrayPart[0]
		openFloat = float(arrayPart[1])
		highFloat = float(arrayPart[2])
		lowFloat = float(arrayPart[3])
		closeFloat = float(arrayPart[4])
		volumeFloat = float(arrayPart[6])
		listOpen.append(openFloat)
		listHigh.append(highFloat)
		listLow.append(lowFloat)
		listClose.append(closeFloat)
		listVolume.append(volumeFloat)
		# high - low
		vola = highFloat-lowFloat
		listVola.append(vola)
		avg = float(lowFloat)+(vola/2)
		listAvg.append(avg)
		# close minus avg
		closeDiffToAvg.append(float(arrayPart[4])-avg)
		vola
	listCloseFloat = []
	[listCloseFloat.append(float(i)) for i in listClose]
	print(listCloseFloat)
	print("avg close= {}".format(np.average(listClose)))
	print("avg volatility= {}".format(np.average(listVola)))
	print("highest volatility= {}".format(np.max(listVola)))

	#	print(part)
	print(len(data))
def test():
	# Download quote for stocks
	#load_quote('QCOM')
	#load_quote('C')

	# Download quote for index
	#load_quote('^DJI')
	read_data()
if __name__ == '__main__':
	test()