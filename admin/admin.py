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
    c.execute('''DROP TABLE IF EXISTS activite''')
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
                    id_instal INTEGER''')
                    # FOREIGN KEY(id_instal) REFERENCES installation(id_instal))''')
    c.execute('''CREATE TABLE activite (
                    id_activ INTEGER PRIMARY KEY,
                    nom_activ TEXT)''')
    c.execute('''CREATE TABLE equipments_activites (
                    id_equip INTEGER,
                    id_activ INTEGER,
                    PRIMARY KEY(id_equip, id_activ)''')
                    # FOREIGN KEY(id_equip) REFERENCES equipment(id_equip),
                    # FOREIGN KEY(id_activ) REFERENCES activite(id_activ))''')
    conn.close

# def addInstallation(numero, nom, adresse, code_postal, ville, latitude, longitude):
#     c = connect()
#     c.execute('''INSERT INTO installation (numero, nom, adresse, code_postal, ville, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (numero, nom, adresse, code_postal, ville, latitude, longitude))
#     conn.close
#
# def addEquipement(numero, nom):
#     c = connect()
#     c.execute('''INSERT INTO equipment (numero, nom) VALUES (?, ?)''', (numero, nom))
#     conn.close
#
# def addActivite(numero, nom):
#     c = connect()
#     c.execute('''INSERT INTO activite (numero, nom) VALUES (?, ?)''', (numero, nom))
#     conn.close
