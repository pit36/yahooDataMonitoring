# -*- coding: utf-8 -*-
"""
Created on 2018
"""

from yahoo_quote import yqd
import json
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
def read_balancesheet(ticker):
	print("Reading Balancesheet: {}".format(ticker))
	filename = 'bs_data.csv'
	data = pd.read_csv(filename)
	data['date'] = pd.to_datetime(data['date'], format='%Y%m%d')
	#df = pd.DataFrame(data)#columns=['model', 'launched', 'discontinued'])
	dfLiab = (data.loc[data['tag'] == 'Liabilities'])
	dfLiabCurrent = (data.loc[data['tag'] == 'LiabilitiesCurrent'])
	dfAsset = (data.loc[data['tag'] == 'Assets'])
	dfAssetCurrent = (data.loc[data['tag'] == 'AssetsCurrent'])

	allFrames = [dfLiab,dfLiabCurrent,dfAsset,dfAssetCurrent]

	all = pd.concat(allFrames)
	fig, ax = plt.subplots()

	all.groupby('tag').plot(x='date', y='value', ax=ax, legend=False)
	#dfLiab.plot(x='date', y='value')
	#dfAsset.plot(x='date', y='value')

	plt.show()
	print(dfLiabVal)
	#liabBoth = df[df['tag'].str.match("Liabil")]
	#print(liabBoth)
def download_balancesheet(ticker):
	print("Downloading balance sheet: {}".format(ticker))
	#url = "https://data.invisement.com/q/{}.csv".format(ticker)
	url = 'https://data.invisement.com/q/AAPL.csv'
	r = requests.get(url, stream=True)
	filename = 'bs_data.csv'
	with open(filename, 'w') as outfile:
		outfile.write(r.content.decode())

	#data = pd.read_csv(filename)
	#print(data)
	
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
	#read_data()
	# pandas
	read_balancesheet('VALE')
if __name__ == '__main__':
	test()