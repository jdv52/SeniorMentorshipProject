import csv
import matplotlib.pyplot as plt
import math
import re

from sys import argv

class Vector6D:
	def __init__(self, t, accX, accY, accZ, gyX, gyY, gyZ):
		self.t = t
		self.accX = accX * 9.80665
		self.accY = accY * 9.80665
		self.accZ = accZ * 9.80665
		self.gyX = gyX
		self.gyY = gyY
		self.gyZ = gyZ

	def getMagnitude(self):
		return math.sqrt((self.accX ** 2) + (self.accY ** 2) + (self.accZ ** 2))

	def __str__(self):
		return '[{}, {}, {}, {}, {}, {}, {}]'.format(self.t, self.accX, self.accY, self.accZ, self.gyX, self.gyY, self.gyZ)

def main(argv):
	dataSets = []
	accepted = []
	rejected = []
	print("Opening the following files...")
	for arg in argv[1:]:
		try:
			dataSets.append(fileOpener(arg))
			accepted.append(arg)
		except:
			rejected.append(arg)

	print("\nThese files were invalid or did not exist:")
	for path in rejected:
		print('    ', path)

	print("\nThe following files opened successfully:")
	for path in accepted:
		print('    ', path)
	drawFigure(dataSets)
	for dataSet in dataSets:
		movingAverage(dataSet)
	drawFigure(dataSets)

def drawFigure(dataSets):
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.75, 0.75])
    colors = ['r', 'g', 'b']
    count = 0
    trialNum = 1
    for set in dataSets:
    	x = [i.t for i in set]
    	acc = [i.accZ for i in set]
    	ax.plot(x, acc, colors[count], label = ('Trial ' + str(trialNum)))
    	count = 0 if count >= len(colors) - 1 else count + 1
    	trialNum += 1
    ax.set_title('Acceleration in the Z axis Over Time')
    ax.set_xlabel('time (s)')
    ax.set_ylabel('acc (m/s^2)')
    ax.legend(loc=0)
    plt.show()

# This method opens the specified file ands creates a list of vectors
def fileOpener(fileName):
	vectorList = []
	with open(fileName, newline="") as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			try:
				row[:] = [float(x) if x != " " else 0 for x in row]
			except ValueError:
				continue
			if len(row) == 7:
				vect = Vector6D(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
				if vect.t < 100:
					vectorList.append(vect)
	return vectorList
	
def gaussian(dataSet):
	return	

def movingAverage(dataSet):
	for i in range(len(dataSet)):
		sum = 0
		count = 0
		for j in range (-12, 12):
			try:
				sum += dataSet[i + j].accZ
				count += 1
			except:
				sum += 0
		dataSet[i].accZ = sum / count

if __name__ == "__main__":
	main(argv)
