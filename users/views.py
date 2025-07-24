from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import UserRegisterForm

# View for user registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Update with your actual login URL name
    else:
        form = UserRegisterForm()

    return render(request, 'users/profile.html')

@login_required  
def profile(request):
    return render(request, "users/profile.html")
