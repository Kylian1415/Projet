# Cette classe va permettre de lancer toutes les opérations nécessaire à la création
# et l'insertion des tables

# Ici, il s'agit d'omporter les méthodes pour importer les activités, équipements et installations
from Imports.Activities.ActivityImporter import importActivities
from Imports.Equipments.EquipmentImporter import importEquipments
from Imports.Fitting.FittingImporter import importFitting

# Ici, on importe la méthode pour créer les tables dans la base de données
from admin.admin import creerTable

# On crée les ravkes
creerTable()

# Puis on se sert des méthodes importés pour importer les données
importActivities('reader/csv/activity.csv')
importEquipments('reader/csv/equipment.csv')
importFitting('reader/csv/fitting.csv')
