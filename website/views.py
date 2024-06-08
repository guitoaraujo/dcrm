from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, 'AIEEEEEEE')
			return redirect('home')
		else:
			messages.success(request, 'BOOOOOOOOOH')
			return redirect('home')
	else:
		return render(request, 'home.html', {})

# def login_user(request):
#     pass

def logout_user(request):
		logout(request)
		messages.success(request, 'BYE')
		return redirect('home')
