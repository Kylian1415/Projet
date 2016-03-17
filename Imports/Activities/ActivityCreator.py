import sqlite3

from Imports.Activities.ActivityLine import ActivityLine

def insertActivity(activity):
    conn = sqlite3.connect('installations.db')
    c = conn.cursor()
    insertQuery = "INSERT INTO activities(id_activ, nom_activ) VALUES (?, ?)"
    c.execute(insertQuery, (activity.code, activity.label))
    conn.commit()
    conn.close()
