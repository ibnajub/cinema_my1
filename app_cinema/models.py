from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone



class User(AbstractUser):
    money = models.PositiveIntegerField(default=0)

class СinemaHall(models.Model):
    title = models.CharField(max_length=200, blank=False, null=True)
    content = models.TextField(max_length=10000, null=True)
    number_of_seats = models.PositiveIntegerField()

class MovieSeason(models.Model):
    title = models.CharField(max_length=200, blank=False, null=True)
    content = models.TextField(max_length=10000, null=True)
    quantity_of_tickets = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    ticket_price = models.PositiveIntegerField()
    movie_show_time_starts = models.DateTimeField()
    movie_show_time_ends = models.DateTimeField()
    movie_session_start_date = models.DateTimeField()
    movie_session_end_date = models.DateTimeField()


class CinemaSession(models.Model):
    movie_season = models.ForeignKey(MovieSeason, on_delete=models.CASCADE, null=False)
    cinema_hall = models.ForeignKey(СinemaHall, on_delete=models.CASCADE, null=False)
    movie_show_starts = models.DateTimeField()
    movie_show_ends = models.DateTimeField()
    empty_seats = models.PositiveIntegerField()
    


class Purchase(models.Model):
    cinema_session = models.ForeignKey(CinemaSession, on_delete=models.CASCADE, null=False)
    movie_season = models.ForeignKey(MovieSeason, on_delete=models.CASCADE, null=False)
    cinema_hall = models.ForeignKey(СinemaHall, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='user_purchases')
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    summ = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "product: {}; siteUser: {}; quantity:{}".format(self.product, self.site_user, self.quantity)

    
    