from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# from .forms import CustomUserCreationForm
#
#
# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})
#
#
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('profile')
#         else:
#             return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
#     return render(request, 'registration/login.html')
#
#
# @login_required
# def user_logout(request):
#     logout(request)
#     return redirect('login')
#
#
# @login_required
# def profile(request):
#     user = request.user
#     return render(request, 'profile.html', {'user': user})