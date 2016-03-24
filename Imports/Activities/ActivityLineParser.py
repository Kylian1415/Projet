from Imports.Activities.ActivityLine import ActivityLine

def parseRow(row):
    id_activ = int(row[4].strip())
    nom_activ = row[5].strip()
    return ActivityLine(id_activ, nom_activ)
