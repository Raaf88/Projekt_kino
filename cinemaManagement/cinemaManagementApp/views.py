from django.shortcuts import render, redirect
from .models import CinemaDb
from .forms import TaskForm, SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = CinemaDb.objects.all()
            messages.success(request, ('New item added..'))
            return render(request, 'index.html', {'all_items': all_items})
    else:
        all_items = CinemaDb.objects.all()
        return render(request, 'index.html', {'all_items': all_items})


def delete(request, list_id):
    item = CinemaDb.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item deleted..'))
    return redirect('home')


@login_required
def profile(request):
    return render(request, 'profile.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
