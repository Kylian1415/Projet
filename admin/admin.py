# Le composant Admin a pour rôle la création des tables de la base de données.

import sqlite3
conn = sqlite3.connect("myDB.db")

def connect():
    return conn.cursor()

def disconnect():
    conn.close

def creerTable():
    c = connect()
    c.execute('''DROP TABLE IF EXISTS equipments_activites''')
    c.execute('''DROP TABLE IF EXISTS activity''')
    c.execute('''DROP TABLE IF EXISTS equipment''')
    c.execute('''DROP TABLE IF EXISTS installation''')
    c.execute('''CREATE TABLE installation (
                    id_instal INTEGER PRIMARY KEY,
                    nom_instal TEXT,
                    adresse TEXT,
                    code_postal TEXT,
                    ville TEXT,
                    latitude INTEGER,
                    longitude INTEGER)''')
    c.execute('''CREATE TABLE equipment (
                    id_equip INTEGER PRIMARY KEY,
                    nom_equip TEXT,
                    id_instal INTEGER)''')
                    # FOREIGN KEY(id_instal) REFERENCES installation(id_instal))''')
    c.execute('''CREATE TABLE activity (
                    id_activ INTEGER PRIMARY KEY,
                    nom_activ TEXT)''')
    c.execute('''CREATE TABLE equipments_activites (
                    id_equip INTEGER,
                    id_activ INTEGER)''')
                    # PRIMARY KEY(id_equip, id_activ)''')
                    # FOREIGN KEY(id_equip) REFERENCES equipment(id_equip),
                    # FOREIGN KEY(id_activ) REFERENCES activite(id_activ))''')
    conn.close
