from django import forms 
from django.contrib.auth.models import User 
from .models import * 

class ClientForm(forms.ModelForm):
    class Meta():
        model = Client 
        fields = ('nom_client','prenom_client', 'num_compte' )
        widgets = { 
            'nom_client': forms.TextInput(attrs={'class':'form-control input-group input-group-merge '}), 
            'prenom_client': forms.TextInput(attrs={'class':'form-control input-group input-group-merge '}), 
            'num_compte': forms.TextInput(attrs={'class':'form-control input-group input-group-merge '}),
        }

class PersonnelForm(forms.ModelForm):
    class Meta():
        model = Personnel 
        fields = ('nom','prenoms', 'num_compte', 'adresse' )
        widgets = { 
            'nom': forms.TextInput(attrs={'class':'form-control input-group input-group-merge '}), 
            'prenoms': forms.TextInput(attrs={'class':'form-control input-group input-group-merge '}), 
            'num_compte': forms.TextInput(attrs={'class':'form-control input-group input-group-merge '}),
            'adresse': forms.TextInput(attrs={'class':'form-control input-group input-group-merge '}),
        }
    def __init__(self, *args, **kwargs):
        super(PersonnelForm, self).__init__(*args, **kwargs)
        self.fields['profil'] =  forms.ModelChoiceField( 
                       label='Profil',
                       queryset = Profil.objects.all(),
                       widget=forms.Select(attrs={'class':'form-control selectpicker'}),
                       initial = 1
               )

class ProduitForm(forms.ModelForm):
    class Meta():
        model = ProduitFini 
        fields = ('type_produit',)
        widgets = { 
            'type_produit': forms.TextInput(attrs={'class':'form-control input-group input-group-merge '}), 
        }

class ProfilForm(forms.ModelForm):
    class Meta():
        model = Profil 
        fields = ('nom',)
        widgets = { 
            'nom': forms.TextInput(attrs={'class':'form-control input-group input-group-merge '}), 
        }


class MachineForm(forms.ModelForm):
    class Meta():
        model = Machine 
        fields = ('usage', )
        widgets = { 
            'usage': forms.TextInput(attrs={'class':'form-control input-group input-group-merge '}),
        }
    def __init__(self, *args, **kwargs):
        super(MachineForm, self).__init__(*args, **kwargs)
        self.fields['responsable'] =  forms.ModelChoiceField( 
                       label='Responsable',
                       queryset = Personnel.objects.filter(profil=1),
                       widget=forms.Select(attrs={'class':'form-control selectpicker'}),
                       initial = 1
               )

class TypeMatiereForm(forms.ModelForm):
    class Meta():
        model = Profil 
        fields = ('nom',)
        widgets = { 
            'nom': forms.TextInput(attrs={'class':'form-control input-group input-group-merge '}), 
        }

class ProductionForm(forms.ModelForm):
    class Meta():
        model = Production 
        fields = ('produit','quantite', 'date_production' )
        widgets = { 
            'quantite': forms.TextInput(attrs={'class':'form-control input-group input-group-merge '}),
            'date_production': forms.TextInput(attrs={'class':'form-control datepicker'}),
        }
    def __init__(self, *args, **kwargs):
        super(ProductionForm, self).__init__(*args, **kwargs)
        self.fields['produit'] =  forms.ModelChoiceField( 
                       label='Produit',
                       queryset = ProduitFini.objects.all(),
                       widget=forms.Select(attrs={'class':'form-control selectpicker'}),
                       initial = 1
               )

class FournisseurForm(forms.ModelForm):
    class Meta():
        model = Fournisseur 
        fields = ('nom_four','tel_four','adresse_four', 'num_compte' )
        widgets = { 
            'nom_four': forms.TextInput(attrs={'class':'form-control input-group input-group-merge '}), 
            'tel_four': forms.TextInput(attrs={'class':'form-control input-group input-group-merge '}), 
            'adresse_four': forms.TextInput(attrs={'class':'form-control input-group input-group-merge '}),
            'num_compte': forms.TextInput(attrs={'class':'form-control input-group input-group-merge '}),
        }


class AchatForm(forms.ModelForm):
    class Meta():
        model = Achat 
        fields = ('fournisseur','bois','quantite', 'date_achat' )
        widgets = { 
            'quantite': forms.TextInput(attrs={'class':'form-control input-group input-group-merge '}),
            'date_achat': forms.TextInput(attrs={'class':'form-control datepicker'}),
        }
    def __init__(self, *args, **kwargs):
        super(AchatForm, self).__init__(*args, **kwargs)
        self.fields['fournisseur'] =  forms.ModelChoiceField( 
                       label='Fournisseur',
                       queryset = Fournisseur.objects.all(),
                       widget=forms.Select(attrs={'class':'form-control selectpicker'}),
                       initial = 1
               )
        self.fields['bois'] =  forms.ModelChoiceField( 
                       label='Bois',
                       queryset = TypeMatiere.objects.all(),
                       widget=forms.Select(attrs={'class':'form-control selectpicker'}),
                       initial = 1
               )

class CommandeForm(forms.ModelForm):
    class Meta():
        model = Commande 
        fields = ('client','type_commande','date_commande', 'date_livr_commande' )
        widgets = {
            'type_commande': forms.TextInput(attrs={'class':'form-control input-group input-group-merge '}), 
            'date_commande': forms.TextInput(attrs={'class':'form-control datepicker'}),
            'date_livr_commande': forms.TextInput(attrs={'class':'form-control datepicker'}),
        }
    def __init__(self, *args, **kwargs):
        super(CommandeForm, self).__init__(*args, **kwargs)
        self.fields['client'] =  forms.ModelChoiceField( 
                       label='Client',
                       queryset = Client.objects.all(),
                       widget=forms.Select(attrs={'class':'form-control selectpicker'}),
                       initial = 1
               )

class ProduitCommandeForm(forms.ModelForm):
    class Meta():
        model = ProduitCommande 
        fields = ('produit','quantite' )
        widgets = { 
            'quantite': forms.TextInput(attrs={'class':'form-control input-group input-group-merge '}),
        }
    def __init__(self, *args, **kwargs):
        super(ProduitCommandeForm, self).__init__(*args, **kwargs)
        self.fields['produit'] =  forms.ModelChoiceField( 
                       label='Produit',
                       queryset = ProduitFini.objects.all(),
                       widget=forms.Select(attrs={'class':'form-control selectpicker'}),
                       initial = 1
               )