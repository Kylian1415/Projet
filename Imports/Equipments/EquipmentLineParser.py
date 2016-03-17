from Imports.Equipments.EquipmentLine import EquipmentLine

def parseRow(row):
    code = int(row[4].strip())
    label = row[5].strip()
    return EquipmentLine(code, label)
