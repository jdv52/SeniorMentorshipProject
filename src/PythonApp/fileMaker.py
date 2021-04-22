import csv
import matplotlib.pyplot as plt
import math
import re
import numpy as np

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
        return '[{}, {}, {}, {}, {}, {}, {}]'.format(self.t, self.accX, self.accY, self.accZ, self.gyX, self.gyY,
                                                     self.gyZ)


class Vector12D:
    def __init__(self, t, accX1, accY1, accZ1, gyX1, gyY1, gyZ1, accX2, accY2, accZ2, gyX2, gyY2, gyZ2):
        self.t = t
        self.accX1 = accX1 * 9.80665
        self.accY1 = accY1 * 9.80665
        self.accZ1 = accZ1 * 9.80665
        self.gyX1 = gyX1
        self.gyY1 = gyY1
        self.gyZ1 = gyZ1
        self.accX2 = accX2 * 9.80665
        self.accY2 = accY2 * 9.80665
        self.accZ2 = accZ2 * 9.80665
        self.gyX2 = gyX2
        self.gyY2 = gyY2
        self.gyZ2 = gyZ2

    def getFirstMagnitude(self):
        return math.sqrt((self.accX1 ** 2) + (self.accY1 ** 2) + (self.accZ1 ** 2))

    def getSecondMagnitude(self):
        return math.sqrt((self.accX2 ** 2) + (self.accY2 ** 2) + (self.accZ2 ** 2))

    def __str__(self):
        return '[{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]'.format(self.t, self.accX1, self.accY1, self.accZ1, self.gyX1, self.gyY1,
                                                     self.gyZ1, self.accX2, self.accY2, self.accZ2, self.gyX2, self.gyY2,
                                                     self.gyZ2)


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
    # relativeAccFigure(dataSets, 1)
    relativeAccFigure(dataSets, 10)
    # drawFigure(dataSets, 1)
    # drawFigure(dataSets, 10)
    # for dataSet in dataSets:
    #     movingAverage(dataSet)


def drawFigure(dataSets, w):
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.75, 0.75])
    colors = ['r', 'g', 'b']
    count = 0
    trialNum = 1
    for set in dataSets:
        x = [i.t for i in set]
        acc = [i.accZ2 for i in set]
        avg = np.convolve(acc, np.ones(w), 'same') / w
        ax.plot(x, avg, colors[count], label=('Trial ' + str(trialNum)))
        count = 0 if count >= len(colors) - 1 else count + 1
        trialNum += 1
    ax.set_title('Acceleration in the Z axis Over Time')
    ax.set_xlabel('time (s)')
    ax.set_ylabel('acc (m/s^2)')
    ax.legend(loc=0)
    plt.show()


def relativeAccFigure(dataSets, w):
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.75, 0.75])
    colors = ['r', 'g', 'b']
    count = 0
    trialNum = 1
    for set in dataSets:
        x = [i.t for i in set]
        # relativeAcc = [i.getFirstMagnitude() - i.getSecondMagnitude() for i in set]
        relativeAcc = [Vector6D(i.t, i.accX1 - i.accX2, i.accY1 - i.accY2, i.accZ1 - i.accZ2, 0, 0, 0).getMagnitude() for i in set]
        avg = np.convolve(relativeAcc, np.ones(w), 'same') / w
        ax.plot(x, avg, colors[count], label=('Trial ' + str(trialNum)))
        count = 0 if count >= len(colors) - 1 else count + 1
        trialNum += 1
    ax.set_title('Magnitude of Relative Acceleration Over Time')
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
            elif len(row) == 13:
                vect = Vector12D(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
                if vect.t < 100:
                    vectorList.append(vect)
    return vectorList


if __name__ == "__main__":
    main(argv)
