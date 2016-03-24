import sqlite3

from Imports.Equipments.EquipmentLine import EquipmentLine

def insertEquipment(equipment):
    conn = sqlite3.connect('myDB.db')
    c = conn.cursor()
    insertQuery = "INSERT INTO equipment(id_equip, nom_equip, id_instal) VALUES (?, ?, ?)"
    c.execute(insertQuery, (equipment.id_equip, equipment.nom_equip, equipment.id_instal))
    conn.commit()
    conn.close()
