from Imports.Fitting.FittingLine import EquipmentLine

def parseRow(row):
    id_instal = row[2].strip()
    nom_instal = row[1].strip()
    adresse = row[8].strip()
    code_postal = row[5].strip()
    ville = row[3].strip()
    latitude = row[11].strip()
    longitude = row[10].strip()
    return FittingLine(id_instal, nom_instal, adresse, code_postal, ville, latitude, longitude)
