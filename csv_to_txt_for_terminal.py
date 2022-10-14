import csv

csv_file = input('Filepath for csv(include file name): ')

with open(csv_file) as f:
		content = csv.reader(f) #creates iterable reader object
		csv_list = list(content) #makes each line a list and puts all the lists into a list


output_location = input('Destination filepath for output: ')

with open(output_location + '\output.txt', 'w') as output_file:
		for line in csv_list:
				for item in line:
						output_file.write(item + '\n') #writes each box of the csv on a seperate line
				output_file.write('\n')	#seperates each csv line by an extra line break