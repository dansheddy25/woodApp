from django.conf.urls import include
from django.urls import re_path
from django.urls import path 
from . import views

app_name = 'main_app'

urlpatterns = [
    re_path(r'^$', views.index,name='index'),
    re_path(r'^client/edit/',views.client_edit_view,name='client_edit_view'),
    re_path(r'^client/delete/',views.client_delete_view,name='client_delete_view'),
    re_path(r'^client/',views.client_view,name='client_view'),
    re_path(r'^personnel/edit/',views.personnel_edit_view,name='personnel_edit_view'),
    re_path(r'^personnel/delete/',views.personnel_delete_view,name='personnel_delete_view'),
    re_path(r'^personnel/',views.personnel_view,name='personnel_view'),
    re_path(r'^produit/edit/',views.produit_edit_view,name='produit_edit_view'),
    re_path(r'^produit/delete/',views.produit_delete_view,name='produit_delete_view'),
    re_path(r'^produit/',views.produit_view,name='produit_view'),
    re_path(r'^profil/edit/',views.profil_edit_view,name='profil_edit_view'),
    re_path(r'^profil/delete/',views.profil_delete_view,name='profil_delete_view'),
    re_path(r'^profil/',views.profil_view,name='profil_view'),
    re_path(r'^machine/edit/',views.machine_edit_view,name='machine_edit_view'),
    re_path(r'^machine/delete/',views.machine_delete_view,name='machine_delete_view'),
    re_path(r'^machine/',views.machine_view,name='machine_view'),
    re_path(r'^bois/edit/',views.bois_edit_view,name='bois_edit_view'),
    re_path(r'^bois/delete/',views.bois_delete_view,name='bois_delete_view'),
    re_path(r'^bois/',views.bois_view,name='bois_view'),
    re_path(r'^production/edit/',views.production_edit_view,name='production_edit_view'),
    re_path(r'^production/delete/',views.production_delete_view,name='production_delete_view'),
    re_path(r'^production/',views.production_view,name='production_view'),
    re_path(r'^fournisseur/edit/',views.fournisseur_edit_view,name='fournisseur_edit_view'),
    re_path(r'^fournisseur/delete/',views.fournisseur_delete_view,name='fournisseur_delete_view'),
    re_path(r'^fournisseur/',views.fournisseur_view,name='fournisseur_view'),
    re_path(r'^achat/edit/',views.achat_edit_view,name='achat_edit_view'),
    re_path(r'^achat/delete/',views.achat_delete_view,name='achat_delete_view'),
    re_path(r'^achat/',views.achat_view,name='achat_view'),
    re_path(r'^commande/edit/',views.commande_edit_view,name='commande_edit_view'),
    re_path(r'^commande/delete/',views.commande_delete_view,name='commande_delete_view'),
    re_path(r'^commande/detail/(?P<commande_id>[0-9])',views.commande_detail_view,name='commande_detail_view'),
    re_path(r'^commande/produit/delete/',views.commande_produit_delete_view,name='commande_produit_delete_view'),
    re_path(r'^commande/produit/edit/',views.commande_produit_edit_view,name='commande_produit_edit_view'),
    re_path(r'^commande/produit/create/',views.commande_produit_create_view,name='commande_produit_create_view'),
    re_path(r'^commande/',views.commande_view,name='commande_view'),

]
