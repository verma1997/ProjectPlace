from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import requests


@login_required
def index(request):
	count = User.objects.count()
	return render(request, 'index.html',{
		'count':count,
	})

def signup(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = UserCreationForm()

	return render(request, 'registration/signup.html', {
		'form':form,
	})

@login_required
def secretpage(request):
	return render(request, 'secret_page.html')

class SecretPage(LoginRequiredMixin,TemplateView):
	template_name = 'secret_page.html'