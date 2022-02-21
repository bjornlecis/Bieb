class Boek:
    def __init__(self,id,naam,auteur):
        self.id = id
        self.naam = naam
        self.auteur = auteur
    def __str__(self):
        return "ID: {} titel: {} van {} ".format(self.id,self.naam,self.auteur)
    def toon_boek_auteur(self):
        return "Titel: {} en Schrijver: {}".format(self.naam,self.auteur)

class Persoon:
    def __init__(self,id,naam,geslacht):
        self.id = id
        self.naam = naam
        self.geslacht = geslacht

    def __str__(self):
        return "ID: {} naam: {} geslacht {} ".format(self.id,self.naam,self.geslacht)

class Uitlening:
    def __init__(self,id,boek,persoon):
        self.id = id
        self.boek = boek
        self.persoon = persoon

    def __str__(self):
        return "ID {} Boek: {} Persoon: {}".format(self.id,self.boek.naam,self.persoon.naam)

p = Persoon("P1","Jan","Man")
b = Boek("B1","Boek 1"," A1")
u = Uitlening("U1",b,p)

print(u)
