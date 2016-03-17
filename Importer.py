from Imports.Activities.ActivityImporter import importActivities
# TODO import other data : installations, equipements

from Imports.Equipments.EquipmentImporter import importEquipments
from admin.admin import creerTable

creerTable()

importEquipments('reader/csv/equipment.csv')

importActivities('reader/csv/activites.csv')
