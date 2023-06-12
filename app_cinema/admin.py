from django.contrib import admin

from app_cinema.models import User, CinemaHall, MovieSeason, CinemaSession, Purchase

admin.site.register(User)
admin.site.register(CinemaHall)
admin.site.register(MovieSeason)
admin.site.register(CinemaSession)
admin.site.register(Purchase)
