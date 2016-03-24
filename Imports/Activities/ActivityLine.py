class ActivityLine:
	def __init__(self, id_activ, nom_activ):
		self.id_activ = id_activ
		self.nom_activ = nom_activ

	def __repr__(self):
		return "{} - {}".format(self.id_activ, self.nom_activ)
