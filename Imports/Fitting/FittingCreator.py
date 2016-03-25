import sqlite3

from Imports.Fitting.FittingLine import FittingLine

def insertFitting(fitting):
    conn = sqlite3.connect('myDB.db')
    c = conn.cursor()
    insertQuery = "INSERT INTO fitting(id_instal, nom_instal, adresse, code_postal, ville, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?)"
    c.execute(insertQuery, (fitting.id_instal, fitting.nom_instal, fitting.adresse, fitting.code_postal, fitting.ville, fitting.latitude, fitting.longitude))
    conn.commit()
    conn.close()
