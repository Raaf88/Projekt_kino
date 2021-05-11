from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
# from .models import CinemaDb
from .forms import TaskForm, SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .models import Film, Sala, Seans, Rezerwacja, Bilet


def home(request):
    # if request.method == 'POST':
    #     form = TaskForm(request.POST or None)
    #
    #     if form.is_valid():
    #         form.save()
    #         all_items = CinemaDb.objects.all()
    #         messages.success(request, ('New item added..'))
    #         return render(request, 'index.html', {'all_items': all_items})
    # else:
    #     all_items = CinemaDb.objects.all()
    return render(request, 'index.html')


# def delete(request, list_id):
#     item = CinemaDb.objects.get(pk=list_id)
#     item.delete()
#     messages.success(request, ('Item deleted..'))
#     return redirect('home')

def filmy(request):
    filmy = Film.objects.all()
    return render(request=request, template_name='filmy.html', context={'filmy': filmy})


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def nowy(request):
    return render(request, 'nowy.html')


UserModel = get_user_model()
from .forms import SignUpForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Aktywuj swój profil.'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Proszę o potwierdzenie adresu mailowego')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'registration/poprawny.html')
    else:
        return HttpResponse('Niepoprawny token!')
