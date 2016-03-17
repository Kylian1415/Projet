from Imports.Activities.ActivityImporter import importActivities
# TODO import other data : installations, equipements

from Imports.Equipments.EquipmentImporter import importEquipments
from admin.admin import creerTable

creerTable()

importActivities('reader/csv/activites.csv')

importEquipments('reader/csv/equipment.csv')
