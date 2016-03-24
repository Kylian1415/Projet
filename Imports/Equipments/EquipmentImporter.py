import csv

from Imports.Equipments.EquipmentLine import EquipmentLine
from Imports.Equipments.EquipmentLineParser import parseRow
from Imports.Equipments.EquipmentCreator import insertEquipment

def importEquipments(filename):
	importedEquipments = []

	with open(filename, 'rt') as csvfile:
		equipmentsReader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in equipmentsReader:
			try:
				equipmentLine = parseRow(row)
				if equipmentLine.id_equip not in importedEquipments:
					insertEquipment(equipmentLine)
					importedEquipments.append(equipmentLine.id_equip)
			except ValueError:
				print("Problem with row {} : {}".format(equipmentsReader.line_num, ','.join(row)))

	csvfile.close()
