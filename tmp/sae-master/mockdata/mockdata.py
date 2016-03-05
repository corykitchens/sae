import os
import sys
import fileinput
import django
import random
import time
if __name__ == "__main__":
	sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
	
	os.environ["DJANGO_SETTINGS_MODULE"] = "sae.settings"
	django.setup()
	from employee.models import Employee
	MIDDLE_INITIALS = ['A','J','K','B','C','P']	
	JOB_TITLES = ['mgmt', 'admin', 'tech']
	
	entries = []
	for line in fileinput.input(os.path.abspath('EMPLOYEE_MOCK_DATA.csv')):
		e = Employee()
		entry = line.split(',')
		ssn_str = ''.join(entry[0].split('-'))
		e.ssn = int(ssn_str)
		e.first_name = entry[1]
		e.middle_initial = MIDDLE_INITIALS[random.randrange(0, len(MIDDLE_INITIALS))]
		e.last_name = entry[2]
		e.email = entry[3]
		e.sex = entry[4]
		e.job_title = JOB_TITLES[random.randrange(0, len(JOB_TITLES))]
		e.wage = random.randrange(10,30)
		e.save()
		