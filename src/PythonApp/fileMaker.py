import csv
import  matplotlib.pyplot as plt
import numpy as np

Vector6DList = []

def main():
	with open('accelSensor.csv', newline="") as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			Vector6D = {}
			data = []
			for item in row:
				try:
					a = float(item)
					data.append(a)
				except ValueError:
					break
			if data:
				while (len(data) != 7):
					data.append(0);
				Vector6D['acX'] = data[1]
				Vector6D['acY'] = data[2]
				Vector6D['acZ'] = data[3]
				Vector6D['gyX'] = data[4]
				Vector6D['gyY'] = data[5]
				Vector6D['gyZ'] = data[6]
				Vector6D['time'] = data[0]
				if Vector6D['time'] < 100:
					Vector6DList.append(Vector6D)
				# print(data)

def getXvTimePlot():
	x = [i['time'] for i in Vector6DList]
	y = [i['acX'] for i in Vector6DList]
	fig, ax = plt.subplots()
	ax.plot(x, y, label = "Raw input data")
	ax.plot(np.convolve(x, np.ones(50)/50, mode = 'valid'))
	plt.show()

main()
getXvTimePlot()
