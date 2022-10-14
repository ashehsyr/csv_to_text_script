import csv

def read_csv(csv_file):
		with open(csv_file) as f:
				content = csv.reader(f) #creates iterable reader object
				return list(content) #makes each line a list and puts all the lists into a list


def write_text(csv_list, output_location):
		with open(output_location + '\\output.txt', 'w') as output_file:
				for line in csv_list:
						for item in line:
								output_file.write(item + '\n') #writes each box of the csv on a seperate line
						output_file.write('\n')	#seperates each csv line by an extra line break

def convert_file(file_input, file_output):
		list = read_csv(file_input)
		write_text(list, file_output)
