from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
def register(request):
	if request.method == "POST":
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = CustomUserCreationForm()
		return render(request,'users/register.html',{"form":form})


def home(request):
	return render(request,'users/home.html')

@login_required
def profile(request):
	if request.method == "POST":
		form = CustomUserChangeForm(request.POST,instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = CustomUserChangeForm(instance=request.user)
	return render(request,'users/profile.html',{'form':form})
	
@login_required
def delete(request,id):
	data = CustomUser.objects.get(id=id)
	data.delete()
	return redirect('home')