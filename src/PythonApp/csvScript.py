import csv
import matplotlib.pyplot as plt
import math

Vector6DList1 = []
Vector6DList2 = []
Vector6DList3 = []


def main():
    # with open('HSBT5.CSV', newline="") as csvfile:
    #     reader = csv.reader(csvfile)
    #     for row in reader:
    #         vector = {}
    #         data = []
    #         for item in row:
    #             try:
    #                 if item != ' ':
    #                     a = float(item)
    #                     data.append(a)
    #             except ValueError:
    #                 break
    #         if data:
    #             while len(data) != 13:
    #                 data.append(0)
    #             vector['time'] = data[0]
    #             vector['accX_BP'] = data[1]
    #             vector['accY_BP'] = data[2]
    #             vector['accZ_BP'] = data[3]
    #             vector['gyX_BP'] = data[4]
    #             vector['gyY_BP'] = data[5]
    #             vector['gyZ_BP'] = data[6]
    #             vector['accX_HM'] = data[7]
    #             vector['accY_HM'] = data[8]
    #             vector['accZ_HM'] = data[9]
    #             vector['gyX_HM'] = data[10]
    #             vector['gyY_HM'] = data[11]
    #             vector['gyZ_HM'] = data[12]
    #             if vector['time'] < 100:
    #                 Vector6DList.append(vector)
    with open('ChestLT1.CSV', newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            vector = {}
            data = []
            for item in row:
                try:
                    if item != ' ':
                        a = float(item)
                        data.append(a)
                except ValueError:
                    break
            if data:
                vector['time1'] = data[0]
                vector['accX_BP1'] = data[1]
                vector['accY_BP1'] = data[2]
                vector['accZ_BP1'] = data[3]
                if vector['time1'] < 100:
                    Vector6DList1.append(vector)
    with open('ChestLT2.CSV', newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            vector = {}
            data = []
            for item in row:
                try:
                    if item != ' ':
                        a = float(item)
                        data.append(a)
                except ValueError:
                    break
            if data:
                vector['time2'] = data[0]
                vector['accX_BP2'] = data[1]
                vector['accY_BP2'] = data[2]
                vector['accZ_BP2'] = data[3]
                if vector['time2'] < 100:
                    Vector6DList2.append(vector)
    with open('ChestLT3.CSV', newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            vector = {}
            data = []
            for item in row:
                try:
                    if item != ' ':
                        a = float(item)
                        data.append(a)
                except ValueError:
                    break
            if data:
                vector['time3'] = data[0]
                vector['accX_BP3'] = data[1]
                vector['accY_BP3'] = data[2]
                vector['accZ_BP3'] = data[3]
                if vector['time3'] < 100:
                    Vector6DList3.append(vector)


def drawFigure():
    # x = [i['time'] for i in Vector6DList]
    # accX_BP = [(i['accX_BP'] * 9.80665) for i in Vector6DList]
    # accY_BP = [(i['accY_BP'] * 9.80665) for i in Vector6DList]
    # accZ_BP = [(i['accZ_BP'] * 9.80665) for i in Vector6DList]
    # accT_BP = [math.sqrt(((i['accX_BP'] * 9.80665) ** 2) + ((i['accY_BP'] * 9.80665) ** 2) + ((i['accZ_BP'] * 9.80665) ** 2)) for i in Vector6DList]
    # accX_HM = [(i['accX_HM'] * 9.80665) for i in Vector6DList]
    # accY_HM = [(i['accY_HM'] * 9.80665) for i in Vector6DList]
    # accZ_HM = [(i['accZ_HM'] * 9.80665) for i in Vector6DList]
    # accT_HM = [math.sqrt(((i['accX_HM'] * 9.80665) ** 2) + ((i['accY_HM'] * 9.80665) ** 2) + ((i['accZ_HM'] * 9.80665) ** 2)) for i in Vector6DList]
    # relativeAcc = [(math.sqrt(((i['accX_HM'] * 9.80665) ** 2) + ((i['accY_HM'] * 9.80665) ** 2) + ((i['accZ_HM'] * 9.80665) ** 2))) -
    #                (math.sqrt(((i['accX_BP'] * 9.80665) ** 2) + ((i['accY_BP'] * 9.80665) ** 2) + ((i['accZ_BP'] * 9.80665) ** 2)))
    #                for i in Vector6DList]
    x1 = [i['time1'] for i in Vector6DList1]
    x2 = [i['time2'] for i in Vector6DList2]
    x3 = [i['time3'] for i in Vector6DList3]
    accT1 = [math.sqrt(((i['accX_BP1'] * 9.80665) ** 2) + ((i['accY_BP1'] * 9.80665) ** 2) + ((i['accZ_BP1'] * 9.80665) ** 2)) for i in Vector6DList1]
    accT2 = [math.sqrt(((i['accX_BP2'] * 9.80665) ** 2) + ((i['accY_BP2'] * 9.80665) ** 2) + ((i['accZ_BP2'] * 9.80665) ** 2)) for i in Vector6DList2]
    accT3 = [math.sqrt(((i['accX_BP3'] * 9.80665) ** 2) + ((i['accY_BP3'] * 9.80665) ** 2) + ((i['accZ_BP3'] * 9.80665) ** 2)) for i in Vector6DList3]
    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.75, 0.75])
    ax.plot(x1, accT1, 'r', label='Trial 1')
    ax.plot(x2, accT2, 'g', label='Trial 2')
    ax.plot(x3, accT3, 'b', label='Trial 3')
    ax.set_title('Magnitude of Chest Acceleration Over Time')
    ax.set_xlabel('time (s)')
    ax.set_ylabel('acc (m/s^2)')
    ax.legend(loc=0)
    # Rotational Velocity Code
    # gyX = [i['gyX'] for i in Vector6DList]
    # gyY = [i['gyY'] for i in Vector6DList]
    # gyZ = [i['gyZ'] for i in Vector6DList]

    # Bench Testing Code
    # fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(16, 5))
    # axes[0].plot(x, accX_BP, 'r')
    # axes[0].set_xlabel('time (s)')
    # axes[0].set_ylabel('acc (m/s^2)')
    # axes[0].set_title('X-Acceleration vs. Time')
    # axes[1].plot(x, accY_BP, 'b')
    # axes[1].set_xlabel('time (s)')
    # axes[1].set_ylabel('acc (m/s^2)')
    # axes[1].set_title('Y-Acceleration vs. Time')
    # axes[2].plot(x, accZ_BP, 'g')
    # axes[2].set_xlabel('time (s)')
    # axes[2].set_ylabel('acc (m/s^2)')
    # axes[2].set_title('Z-Acceleration vs. Time')
    # axes[3].plot(x, accT_BP, color='purple')
    # axes[3].set_xlabel('time (s)')
    # axes[3].set_ylabel('acc (m/s^2)')
    # axes[3].set_title('Total Acceleration vs. Time')
    # Relative Acceleration Code
    # fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(19, 10))
    # axes[0][0].plot(x, accX_BP, 'r')
    # axes[0][0].set_xlabel('time (s)')
    # axes[0][0].set_ylabel('acc (m/s^2)')
    # axes[0][0].set_title('Backpack X-Acceleration vs. Time')
    # axes[0][1].plot(x, accY_BP, 'b')
    # axes[0][1].set_xlabel('time (s)')
    # axes[0][1].set_ylabel('acc (m/s^2)')
    # axes[0][1].set_title('Backpack Y-Acceleration vs. Time')
    # axes[0][2].plot(x, accZ_BP, 'g')
    # axes[0][2].set_xlabel('time (s)')
    # axes[0][2].set_ylabel('acc (m/s^2)')
    # axes[0][2].set_title('Backpack Z-Acceleration vs. Time')
    # axes[0][3].plot(x, accT_BP, color='purple')
    # axes[0][3].set_xlabel('time (s)')
    # axes[0][3].set_ylabel('acc (m/s^2)')
    # axes[0][3].set_title('Backpack Total Acceleration vs. Time')
    # axes[1][0].plot(x, accX_HM, 'r')
    # axes[1][0].set_xlabel('time (s)')
    # axes[1][0].set_ylabel('acc (m/s^2)')
    # axes[1][0].set_title('Human X-Acceleration vs. Time')
    # axes[1][1].plot(x, accY_HM, 'b')
    # axes[1][1].set_xlabel('time (s)')
    # axes[1][1].set_ylabel('acc (m/s^2)')
    # axes[1][1].set_title('Human Y-Acceleration vs. Time')
    # axes[1][2].plot(x, accZ_HM, 'g')
    # axes[1][2].set_xlabel('time (s)')
    # axes[1][2].set_ylabel('acc (m/s^2)')
    # axes[1][2].set_title('Human Z-Acceleration vs. Time')
    # axes[1][3].plot(x, accT_HM, color='purple')
    # axes[1][3].set_xlabel('time (s)')
    # axes[1][3].set_ylabel('acc (m/s^2)')
    # axes[1][3].set_title('Human Total Acceleration vs. Time')
    # axes[2][0].plot(x, relativeAcc, color='black')
    # axes[2][0].set_xlabel('time (s)')
    # axes[2][0].set_ylabel('acc (m/s^2)')
    # axes[2][0].set_title('Relative Acceleration vs. Time')
    # plt.delaxes(axes[2][1])
    # plt.delaxes(axes[2][2])
    # plt.delaxes(axes[2][3])

    # Graphs w/ Rotational Velocity
    # axes[0][0].plot(x, accX, 'r')
    # axes[0][0].set_xlabel('time (s)')
    # axes[0][0].set_ylabel('acceleration (m/s^2)')
    # axes[0][0].set_title('X-Acceleration vs. Time')
    # axes[0][1].plot(x, accY, 'b')
    # axes[0][1].set_xlabel('time (s)')
    # axes[0][1].set_ylabel('acceleration (m/s^2)')
    # axes[0][1].set_title('Y-Acceleration vs. Time')
    # axes[0][2].plot(x, accZ, 'g')
    # axes[0][2].set_xlabel('time (s)')
    # axes[0][2].set_ylabel('acceleration (m/s^2)')
    # axes[0][2].set_title('Z-Acceleration vs. Time')
    # axes[0][3].plot(x, accT, color='purple')
    # axes[0][3].set_xlabel('time (s)')
    # axes[0][3].set_ylabel('acceleration (m/s^2)')
    # axes[0][3].set_title('Total Acceleration vs. Time')
    # axes[1][0].plot(x, gyX, 'r')
    # axes[1][0].set_xlabel('time (s)')
    # axes[1][0].set_ylabel('velocity (m/s)')
    # axes[1][0].set_title('X-Rotational Velocity vs. Time')
    # axes[1][1].plot(x, gyY, 'b')
    # axes[1][1].set_xlabel('time (s)')
    # axes[1][1].set_ylabel('velocity (m/s)')
    # axes[1][1].set_title('Y-Rotational Velocity vs. Time')
    # axes[1][2].plot(x, gyZ, 'g')
    # axes[1][2].set_xlabel('time (s)')
    # axes[1][2].set_ylabel('velocity (m/s)')
    # axes[1][2].set_title('Z-Rotational Velocity vs. Time')
    # plt.delaxes(axes[1][0])
    # plt.delaxes(axes[1][1])
    # plt.delaxes(axes[1][2])
    # plt.delaxes(axes[1][3])
    # plt.tight_layout()
    # fig.savefig("HSBT5.png")
    plt.show()


main()
drawFigure()
