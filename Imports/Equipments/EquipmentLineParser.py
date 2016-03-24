from Imports.Equipments.EquipmentLine import EquipmentLine

def parseRow(row):
    id_equip = int(row[4].strip())
    nom_equip = row[5].strip()
    id_insta = int(row[2].strip())
    return EquipmentLine(id_equip, nom_equip, id_insta)
