from django.conf import settings
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from . import views

urlpatterns = [
                  path('', views.home, name='home'),
                  path('profile/', views.profile, name='profile'),
                  path('filmy/', views.filmy, name='filmy'),
                  path('register/', views.register, name='register'),
                  path('nowy/', views.nowy, name='nowy'),
                  path('login/', LoginView.as_view(), name='login'),
                  path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
                  # path('delete/<list_id>', views.delete, name='delete'),
                  path('activate/<uidb64>/<token>/', views.activate, name='activate'),

              ]
