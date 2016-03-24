import csv

from Imports.Activities.ActivityLine import ActivityLine
from Imports.Activities.ActivityLineParser import parseRow
from Imports.Activities.ActivityCreator import insertActivity

def importActivities(filename):
	importedActivities = []

	with open(filename, 'rt') as csvfile:
		activitiesReader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in activitiesReader:
			try:
				activityLine = parseRow(row)
				if activityLine.id_activ not in importedActivities:
					insertActivity(activityLine)
					importedActivities.append(activityLine.id_activ)
					# print(activityLine)
			except ValueError:
				print("Problem with row {} : {}".format(activitiesReader.line_num, ','.join(row)))

	csvfile.close()
