import csv

MY_FILE = "sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
	"""Parses a raw CSV file to a JSON-line object."""

	# Open CSV file
	opened_file = open(raw_file)
	
	# Read CSV file
	csv_data = csv.reader(opened_file, delimiter=delimiter)
	# Close CSV file

	# Build a data structure to return parsed_data
	parsed_data = []

	fields = csv_data.next() # skip over the first line of the cvs file for the headers

	for row in csv_data:
		parsed_data.append(dict(zip(fields,row)))

	# Close the CSV file
	opened_file.close()

	return parsed_data

def main():
	# Call our parse function with the parameters needed

	new_data  = parse(MY_FILE, ",")

	# Let's see what the data looks like

	print(new_data)

# Code will only be executed if you want to run the module as a program
if __name__ == "__main__":
	main()