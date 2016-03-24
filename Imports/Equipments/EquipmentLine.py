class EquipmentLine:
	def __init__(self, id_equip, nom_equip, id_instal):
		self.id_equip = id_equip
		self.nom_equip = nom_equip
		self.id_instal = id_instal

	def __repr__(self):
		return "{} - {} - {}".format(self.id_equip, self.nom_equip, self.id_instal)
