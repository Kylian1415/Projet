import sqlite3

from Imports.Equipments.EquipmentLine import EquipmentLine

def insertEquipment(equipment):
    conn = sqlite3.connect('myDB.db')
    c = conn.cursor()
    insertQuery = "INSERT INTO equipment(code, label) VALUES (?, ?)"
    c.execute(insertQuery, (equipment.code, equipment.label, equipment.code))
    conn.commit()
    conn.close()
