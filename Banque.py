class Banque:
	def __init__(self):
		self.nom=""
		self.balance = 0
clients = {}
reponse = "oui"
while reponse == "oui":
		nom = input("Quelle est le nom du Cleint : ")
		montant = input("Quelle est le montant de stocke par ce Cleint : ")


		clients[nom] = Banque()
		clients[nom].nom = nom
		clients[nom].balance = montant
		reponse = input("Voulez-vous continuez avec un autre compte ? oui / non \n")
print("Les comptes bancaire enregistrer sont : \n")
for client in clients.values():
		print("{0} a stocker {1}".format(client.nom, client.balance))

