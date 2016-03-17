class FittingLine:
	def __init__(self, id_instal, nom_instal, adresse, code_postal, ville, latitude, longitude):
		self.id_instal = id_instal
		self.nom_instal = nom_instal
        self.adresse = adresse
        self.code_postal = code_postal
        self.ville = ville
        self.latitude = latitude
        self.longitude = longitude

	def __repr__(self):
		return "{} - {} - {} - {} - {} - {} - {}".format(self.id_instal, self.nom_instal, self.adresse, self.code_postal, self.ville, self.latitude, self.longitude )
