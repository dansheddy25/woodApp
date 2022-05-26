from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse 
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required 
import datetime
from django.contrib.auth.forms import UserCreationForm
from main_app.models import *
from main_app.forms import *
from django.http import JsonResponse
from django.core import serializers



@login_required
def commande_view(request):
	if request.method == "POST":
		form = CommandeForm(data=request.POST)
		if form.is_valid():
			instance = Commande()
			client_id= request.POST.get('client')
			client = Client.objects.get(id=client_id)
			instance.type_commande = request.POST.get('type_commande')
			instance.date_commande = request.POST.get('date_commande')
			instance.date_livr_commande = request.POST.get('date_livr_commande')
			instance.client= client
			instance.save()
		else :
			print(form.errors)

	else :
		form = CommandeForm()
	list_instances= Commande.objects.all()
	list_clients= Client.objects.all()

	return render(request,'main_app/commande_all.html', 
							{'list_instances':list_instances,
							'list_clients':list_clients,
							'form':form
							})
@login_required
def commande_delete_view(request):
	data_id = request.POST.get('data_id')		
	instance = Commande.objects.get(id=data_id) 
	instance.delete()
	return redirect('main_app:commande_view')

@login_required
def commande_produit_delete_view(request):
	data_id = request.POST.get('data_id')		
	instance = ProduitCommande.objects.get(id=data_id) 	
	commande_id= instance.commande.id
	instance.delete()
	return redirect('main_app:commande_detail_view',commande_id=commande_id )

@login_required
def commande_detail_view(request, commande_id):
	commande = Commande.objects.get(id=commande_id)
	list_instances= ProduitCommande.objects.filter(commande=commande_id)
	list_produits= ProduitFini.objects.all()
	form = ProduitCommandeForm()
	return render(request,'main_app/commande_detail.html', 
							{'commande':commande,
							 'list_instances':list_instances,
							 'list_produits':list_produits,
							 'form':form
							})


@login_required
def commande_produit_create_view(request):
	if request.method == "POST":
		form = ProduitCommandeForm(data=request.POST)
		commande_id = request.POST.get('commande_id')
		commande= Commande.objects.get(id=commande_id)
		if form.is_valid():
			instance = ProduitCommande()
			produit_id = request.POST.get('produit')
			produit = ProduitFini.objects.get(id=produit_id)
			instance.produit= produit
			instance.commande= commande
			instance.quantite = request.POST.get('quantite')
			instance.save()
		else :
			print(form.errors)

	else :
		form = ProduitCommandeForm()
	list_instances= ProduitCommande.objects.filter(commande=commande_id)
	list_produits= ProduitFini.objects.all()
	return render(request,'main_app/commande_detail.html', 
							{'commande':commande,
							 'list_instances':list_instances,
							 'list_produits':list_produits,
							 'form':form,
							})

@login_required
def commande_produit_edit_view(request):
	if request.method == "POST":
		form = ProduitCommandeForm(data=request.POST)
		if form.is_valid():
			id = request.POST.get('id')
			produit_id = request.POST.get('produit')
			produit = ProduitFini.objects.get(id=produit_id)
			instance = ProduitCommande.objects.get(id=id)
			instance.quantite = request.POST.get('quantite')
			instance.produit= produit
			instance.save()
			return redirect('main_app:commande_detail_view',commande_id=instance.commande.id )
		else :
			print('Form erros')

@login_required
def commande_edit_view(request):
	if request.method == "POST":
		commandeForm = CommandeForm(data=request.POST)
		if commandeForm.is_valid():
			id = request.POST.get('id')
			instance = Commande.objects.get(id=id)
			instance.type_commande = request.POST.get('type_commande')
			instance.date_commande = request.POST.get('date_commande')
			instance.date_livr_commande = request.POST.get('date_livr_commande')
			instance.save()
			return redirect('main_app:commande_view')
		else :
			print('Form erros')

@login_required
def achat_view(request):
	if request.method == "POST":
		form =AchatForm(data=request.POST)
		if form.is_valid():
			instance = Achat()
			bois_id= request.POST.get('bois')
			bois = TypeMatiere.objects.get(id=bois_id)
			fournisseur_id= request.POST.get('fournisseur')
			fournisseur = Fournisseur.objects.get(id=fournisseur_id)
			instance.quantite = request.POST.get('quantite')
			instance.date_achat = request.POST.get('date_achat')
			instance.bois = bois
			instance.fournisseur = fournisseur
			instance.save()
		else :
			print(form.errors)

	else :
		form = AchatForm()
	list_instances= Achat.objects.all()
	list_bois= TypeMatiere.objects.all()
	list_fournisseurs= Fournisseur.objects.all()

	return render(request,'main_app/achat_all.html', 
							{'list_instances':list_instances,
							'list_bois':list_bois,
							'list_fournisseurs':list_fournisseurs,
							'form':form
							})
@login_required
def achat_delete_view(request):
	data_id = request.POST.get('data_id')		
	instance = Achat.objects.get(id=data_id) 
	instance.delete()
	return redirect('main_app:achat_view')

@login_required
def achat_edit_view(request):
	if request.method == "POST":
		achatForm = AchatForm(data=request.POST)
		if achatForm.is_valid():
			id = request.POST.get('id')
			bois_id= request.POST.get('bois')
			bois = TypeMatiere.objects.get(id=bois_id)
			fournisseur_id= request.POST.get('fournisseur')
			fournisseur = Fournisseur.objects.get(id=fournisseur_id)
			instance = Achat.objects.get(id=id)
			instance.quantite = request.POST.get('quantite')
			instance.date_achat = request.POST.get('date_achat')
			instance.bois = bois
			instance.fournisseur = fournisseur
			instance.save()
			return redirect('main_app:achat_view')
		else :
			print('Form erros')

@login_required
def fournisseur_view(request):
	if request.method == "POST":
		form = FournisseurForm(data=request.POST)
		if form.is_valid():
			instance = Fournisseur()
			instance.nom_four = request.POST.get('nom_four')
			instance.tel_four = request.POST.get('tel_four')
			instance.adresse_four = request.POST.get('adresse_four')
			instance.num_compte = request.POST.get('num_compte')
			instance.save()
		else :
			print(form.errors)

	else :
		form = FournisseurForm()
	list_instances= Fournisseur.objects.all()

	return render(request,'main_app/fournisseur_all.html', 
							{'list_instances':list_instances,
							'form':form
							})
@login_required
def fournisseur_delete_view(request):
	data_id = request.POST.get('data_id')		
	instance = Fournisseur.objects.get(id=data_id) 
	instance.delete()
	return redirect('main_app:fournisseur_view')

@login_required
def fournisseur_edit_view(request):
	if request.method == "POST":
		fournisseurForm = FournisseurForm(data=request.POST)
		if fournisseurForm.is_valid():
			id = request.POST.get('id')
			instance = Fournisseur.objects.get(id=id)
			instance.nom_four = request.POST.get('nom_four')
			instance.tel_four = request.POST.get('tel_four')
			instance.adresse_four = request.POST.get('adresse_four')
			instance.num_compte = request.POST.get('num_compte')
			instance.save()
			return redirect('main_app:fournisseur_view')
		else :
			print('Form erros')


@login_required
def production_view(request):
	if request.method == "POST":
		form = ProductionForm(data=request.POST)
		if form.is_valid():
			instance = Production()
			produit_id= request.POST.get('produit')
			produit = ProduitFini.objects.get(id=produit_id)
			instance.quantite = request.POST.get('quantite')
			instance.date_production = request.POST.get('date_production')
			instance.produit = produit
			instance.save()
		else :
			print(form.errors)

	else :
		form = ProductionForm()
	list_instances= Production.objects.all()
	list_produits= ProduitFini.objects.all()

	return render(request,'main_app/production_all.html', 
							{'list_instances':list_instances,
							'list_produits':list_produits,
							'form':form
							})
@login_required
def production_delete_view(request):
	data_id = request.POST.get('data_id')		
	instance = Production.objects.get(id=data_id) 
	instance.delete()
	return redirect('main_app:production_view')

@login_required
def production_edit_view(request):
	if request.method == "POST":
		productionForm = ProductionForm(data=request.POST)
		if productionForm.is_valid():
			id = request.POST.get('id')
			produit_id= request.POST.get('produit')
			produit = ProduitFini.objects.get(id=produit_id)
			instance = Production.objects.get(id=id)
			instance.quantite = request.POST.get('quantite')
			instance.date_production = request.POST.get('date_production')
			instance.produit = produit
			instance.save()
			return redirect('main_app:production_view')
		else :
			print('Form erros')


@login_required
def bois_view(request):
	if request.method == "POST":
		form = TypeMatiereForm(data=request.POST)
		if form.is_valid():
			instance = TypeMatiere()
			instance.nom = request.POST.get('nom')
			instance.save()
		else :
			print(form.errors)

	else :
		form = TypeMatiereForm()
	list_instances= TypeMatiere.objects.all()

	return render(request,'main_app/bois_all.html', 
							{'list_instances':list_instances,
							'form':form
							})
@login_required
def bois_delete_view(request):
	data_id = request.POST.get('data_id')	
	instance = TypeMatiere.objects.get(id=data_id) 
	instance.delete()
	return redirect('main_app:bois_view')

@login_required
def bois_edit_view(request):
	if request.method == "POST":
		typeMatiereForm = TypeMatiereForm(data=request.POST)
		if typeMatiereForm.is_valid():
			id = request.POST.get('id')
			instance = TypeMatiere.objects.get(id=id)
			instance.nom = request.POST.get('nom')
			instance.save()
			return redirect('main_app:bois_view')
		else :
			print('Form erros')

@login_required
def machine_view(request):
	if request.method == "POST":
		form = MachineForm(data=request.POST)
		if form.is_valid():
			instance = Machine()
			personnel_id= request.POST.get('responsable')
			responsable = Personnel.objects.get(id=personnel_id)
			instance.usage = request.POST.get('usage')
			instance.responsable = responsable
			instance.save()
		else :
			print(form.errors)

	else :
		form = MachineForm()
	list_instances= Machine.objects.all()
	list_personnels= Personnel.objects.filter(profil=1)

	return render(request,'main_app/machine_all.html', 
							{'list_instances':list_instances,
							'list_personnels':list_personnels,
							'form':form
							})
@login_required
def machine_delete_view(request):
	data_id = request.POST.get('data_id')		
	instance = Machine.objects.get(id=data_id) 
	instance.delete()
	return redirect('main_app:machine_view')

@login_required
def machine_edit_view(request):
	if request.method == "POST":
		machineForm = MachineForm(data=request.POST)
		if machineForm.is_valid():
			id = request.POST.get('id')
			instance = Machine.objects.get(id=id)
			personnel_id= request.POST.get('responsable')
			responsable = Personnel.objects.get(id=personnel_id)
			instance.usage = request.POST.get('usage')
			instance.responsable = responsable
			instance.save()
			return redirect('main_app:machine_view')
		else :
			print('Form erros')


@login_required
def profil_view(request):
	if request.method == "POST":
		form = ProfilForm(data=request.POST)
		if form.is_valid():
			instance = Profil()
			instance.nom = request.POST.get('nom')
			instance.save()
		else :
			print(form.errors)

	else :
		form = ProfilForm()
	list_instances= Profil.objects.all()

	return render(request,'main_app/profil_all.html', 
							{'list_instances':list_instances,
							'form':form
							})
@login_required
def profil_delete_view(request):
	data_id = request.POST.get('data_id')	
	instance = Profil.objects.get(id=data_id) 
	instance.delete()
	return redirect('main_app:profil_view')

@login_required
def profil_edit_view(request):
	if request.method == "POST":
		profilForm = ProfilForm(data=request.POST)
		if profilForm.is_valid():
			id = request.POST.get('id')
			instance = Profil.objects.get(id=id)
			instance.nom = request.POST.get('nom')
			instance.save()
			return redirect('main_app:profil_view')
		else :
			print('Form erros')



@login_required
def produit_view(request):
	if request.method == "POST":
		form = ProduitForm(data=request.POST)
		if form.is_valid():
			instance = ProduitFini()
			instance.type_produit = request.POST.get('type_produit')
			instance.save()
		else :
			print(form.errors)

	else :
		form = ProduitForm()
	list_instances= ProduitFini.objects.all()

	return render(request,'main_app/produit_all.html', 
							{'list_instances':list_instances,
							'form':form
							})
@login_required
def produit_delete_view(request):
	data_id = request.POST.get('data_id')		
	instance = ProduitFini.objects.get(id=data_id) 
	instance.delete()
	return redirect('main_app:produit_view')

@login_required
def produit_edit_view(request):
	if request.method == "POST":
		produiForm = ProduitForm(data=request.POST)
		if produiForm.is_valid():
			id = request.POST.get('id')
			instance = ProduitFini.objects.get(id=id)
			instance.type_produit = request.POST.get('type_produit')
			instance.save()
			return redirect('main_app:produit_view')
		else :
			print('Form erros')


@login_required
def personnel_view(request):
 
	list_profils= Profil.objects.all()

	return render(request,'main_app/personnel_all.html', 
							{'list_instances':list_instances,
							'list_profils':list_profils,
							'form':form
							})
@login_required
def personnel_delete_view(request):
	data_id = request.POST.get('data_id')		
	instance = Personnel.objects.get(id=data_id) 
	instance.delete()
	return redirect('main_app:personnel_view')

@login_required
def personnel_edit_view(request):
	if request.method == "POST":
		personnelForm = PersonnelForm(data=request.POST)
		if personnelForm.is_valid():
			id = request.POST.get('id')
			profil_id= request.POST.get('profil')
			profil = Profil.objects.get(id=profil_id)
			instance = Personnel.objects.get(id=id)
			instance.nom = request.POST.get('nom')
			instance.prenoms = request.POST.get('prenoms')
			instance.num_compte = request.POST.get('num_compte')
			instance.adresse = request.POST.get('adresse')
			instance.profil= profil
			instance.save()
			return redirect('main_app:personnel_view')
		else :
			print('Form erros')


@login_required
def client_view(request):
	if request.method == "POST":
		form = ClientForm(data=request.POST)
		if form.is_valid():
			instance = Client()
			instance.nom_client = request.POST.get('nom_client')
			instance.prenom_client = request.POST.get('prenom_client')
			instance.num_compte = request.POST.get('num_compte')
			instance.save()
		else :
			print(form.errors)

	else :
		form = ClientForm()
	list_instances= Client.objects.all()

	return render(request,'main_app/client_all.html', 
							{'list_instances':list_instances,
							'form':form
							})
@login_required
def client_delete_view(request):
	print("hello")	
	data_id = request.POST.get('data_id')		
	instance = Client.objects.get(id=data_id) 
	instance.delete()
	print("hello")
	return redirect('main_app:client_view')

@login_required
def client_edit_view(request):
	if request.method == "POST":
		clientForm = ClientForm(data=request.POST)
		if clientForm.is_valid():
			id = request.POST.get('id')
			client = Client.objects.get(id=id)
			client.nom_client = request.POST.get('nom_client')
			client.prenom_client = request.POST.get('prenom_client')
			client.num_compte = request.POST.get('num_compte')
			client.save()
			return redirect('main_app:client_view')
		else :
			print('Form erros')

@login_required
def index(request):

	total_client = Client.objects.all().count()
	total_commande = Commande.objects.all().count()
	total_personnel = Personnel.objects.all().count()	
	total_machine = Machine.objects.all().count()
	total_produit = ProduitFini.objects.all().count()
	total_fournisseur = Fournisseur.objects.all().count()
	
	return render(request,'main_app/index.html', 
							{'total_client':total_client,
							'total_commande':total_commande,
							'total_personnel':total_personnel,
							'total_machine':total_machine,
							'total_produit':total_produit,
							'total_fournisseur':total_fournisseur,
							})

@login_required
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserCreationForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
        else:
            print(user_form.errors)
    else:
        user_form = UserCreationForm()

    return render(request,'main_app/auth/registration.html',
                          {'user_form':user_form,
                           'registered':registered})
