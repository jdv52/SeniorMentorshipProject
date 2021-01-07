import csv
import random

def main():
	with open('names.csv', 'w', newline="") as csvfile:
		fieldnames = ['x', 'y', 'z', 'gy-x', 'gy-y', 'gy-z']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		writer.writeheader()
		for i in range(100):
			nums = []
			for j in range(len(fieldnames)):
				random.seed()
				nums.append(random.randint(0, 100))
			writer.writerow({'x': nums[0], 'y': nums[1], 'z':nums[2], 'gy-x':nums[3], 'gy-y':nums[4], 'gy-z':nums[5]})


main()
