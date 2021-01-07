import csv

def main():
	with open('names.csv', 'w', newline="") as csvfile:
		fieldnames = ['first_name', 'last_name']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		writer.writeheader()
		writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})


main()