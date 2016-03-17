class EquipmentLine:
	def __init__(self, code, label, code_insta):
		self.code = code
		self.label = label
		self.code_insta = code_insta

	def __repr__(self):
		return "{} - {} - {}".format(self.code, self.label, self.code_insta)
