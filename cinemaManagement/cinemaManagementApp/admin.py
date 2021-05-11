from django.contrib import admin

# from .models import CinemaDb
from .models import Film, Sala, Seans, Rezerwacja, Bilet


# admin.site.register(CinemaDb)
admin.site.register(Film)
admin.site.register(Sala)
admin.site.register(Seans)
admin.site.register(Rezerwacja)
admin.site.register(Bilet)
