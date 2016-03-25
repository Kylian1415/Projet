from Imports.Fitting.FittingLine import FittingLine

def parseRow(row):
    id_instal = int(row[2].strip())
    nom_instal = row[1].strip()
    adresse = row[8].strip()
    code_postal = int(row[5].strip())
    ville = row[3].strip()
    latitude = int(row[11].strip())
    longitude = int(row[10].strip())
    return FittingLine(id_instal, nom_instal, adresse, code_postal, ville, latitude, longitude)
