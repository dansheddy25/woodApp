from django.db import models

# Create your models here.

class Service(models.Model):
    nom_service = models.CharField(max_length=254)
    def __str__(self):
        return self.nom_service

class Banque(models.Model):
    numero_compte = models.CharField(max_length=254)
    nom = models.CharField(max_length=254)
    prenoms = models.CharField(max_length=254)
    tel = models.CharField(max_length=254)
    def __str__(self):
        return self.nom + self.prenoms

class Profil(models.Model):
    nom = models.CharField(max_length=254)
    def __str__(self):
        return self.nom

class Personnel(models.Model):
    nom = models.CharField(max_length=254)
    prenoms = models.CharField(max_length=254)
    adresse = models.CharField(max_length=254)
    num_compte = models.CharField(max_length=254)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom +" "+ self.prenoms

class Client(models.Model):
    nom_client = models.CharField(max_length=254)
    prenom_client = models.CharField(max_length=254)
    num_compte = models.CharField(max_length=254)
    def __str__(self):
        return self.nom_client +' '+ self.prenom_client

class Fournisseur(models.Model):
    nom_four = models.CharField(max_length=254)
    tel_four = models.CharField(max_length=254)
    adresse_four = models.CharField(max_length=254)
    num_compte = models.CharField(max_length=254)
    def __str__(self):
        return self.nom_four

class Machine(models.Model):
    usage = models.CharField(max_length=254)
    responsable = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    def __str__(self):
        return self.usage

class TypeMatiere(models.Model):
    nom = models.CharField(max_length=254)
    def __str__(self):
        return self.nom

class ProduitFini(models.Model):
    type_produit = models.CharField(max_length=254)
    def __str__(self):
        return self.type_produit

class Commande(models.Model):
    type_commande = models.CharField(max_length=254)
    date_commande = models.CharField(max_length=254)
    date_livr_commande = models.CharField(max_length=254, null =True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    def __str__(self):
        return self.num_commande

class Commercial(models.Model):
    num_agent_commer = models.CharField(max_length=254)
    def __str__(self):
        return self.num_commande

class ProduitCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(ProduitFini, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    def __str__(self):
        return self.num_commande

class Production(models.Model):
    produit = models.ForeignKey(ProduitFini, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    date_production = models.CharField(max_length=254)
    def __str__(self):
        return self.produit.type_produit+ " ("+ self.quantite +")"

class Achat(models.Model):
    bois = models.ForeignKey(TypeMatiere, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    date_achat = models.CharField(max_length=254)
    def __str__(self):
        return self.bois.nom+ " ("+ self.quantite +")"