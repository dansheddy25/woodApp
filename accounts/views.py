# views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User


# Create your views here.

@login_required
def user_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
	        form.save()
        return redirect("accounts:user_view")
    else:
        form = RegisterForm()
    list_instances= User.objects.all()

    return render(request, "accounts/user_all.html", 
            {"form":form,
            "list_instances":list_instances
            })

@login_required
def user_delete_view(request):
	data_id = request.POST.get('data_id')		
	instance = User.objects.get(id=data_id) 
	instance.delete()
	return redirect('accounts:user_view')

@login_required
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
	        form.save()
        return redirect("accounts:user_view")
    else:
        form = RegisterForm()

    return render(request, "registration/signup.html", {"form":form})
