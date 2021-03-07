from django.shortcuts import render, redirect
from .forms import UserRegisterForm #, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account Has Been created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/signup.html', {'form': form})

