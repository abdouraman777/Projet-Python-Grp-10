class Agent:
	def __init__(self, nom_agent, prenom_agent):
		self.nom = nom_agent
		self.prenom = prenom_agent
				#identifiant = lambda:print(18A908FS)

	def peut_effectuer(self):
		print("L'agent {} à effectuer ".format(self.nom))
		#print("L'agent {} a supprimer".format(self.prenom))	
	def peut_ajouter(self):
		print("L'agent {} peut ajouter".format(self.prenom))

class guichetier(Agent):
	def __init__(self, nom_guichetier, prenom, poste):
		Agent.__init__(self, nom_guichetier, prenom)	
		self.poste = poste

guichetier1 = guichetier("alioum", "mana", 12)	
guichetier1.peut_effectuer()
print(guichetier1.poste, "Enregistrement")	


class controleur(Agent):
	def __init__(self, nom_controleur, prenom, identifiant):
		Agent.__init__(self, nom_controleur, prenom)	
		self.identifiant = identifiant	


controleur1 = controleur("Kaou", "mana", 17)	
controleur1.peut_ajouter()
print(controleur1.identifiant, "client")	


class gestionnaire(Agent):
	def __init__(self, nom_gestionnaire, prenom_gestionnaire, poste_gestionnaire, id_gestionnaire):
		Agent.__init__(self, nom_gestionnaire, prenom_gestionnaire, id_gestionnaire)	
		self.id_gestionnaire = identifiant	