import csv

from Imports.Fitting.FittingLine import FittingLine
from Imports.Fitting.FittingLineParser import parseRow
from Imports.Fitting.FittingCreator import insertFitting

def importFitting(filename):
	importedFitting = []

	with open(filename, 'rt') as csvfile:
		fittingReader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in fittingReader:
			try:
				fittingLine = parseRow(row)
				if fittingLine.code not in importedFitting:
					insertFitting(fittingLine)
					importedFitting.append(fittingLine.code)
					# print(equipmentLine)
			except ValueError:
				print("Problem with row {} : {}".format(fittingReader.line_num, ','.join(row)))

	csvfile.close()
