import os
import fileinput

entries = []
for line in fileinput.input(os.path.abspath('employee/EMPLOYEE_MOCK_DATA.csv')):
	entries.append(line.split(','))
	
for entry in entries:
	for col in entry:
		print col

