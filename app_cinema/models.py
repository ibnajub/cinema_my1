from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


# from django.utils import timezone


class User(AbstractUser):
    money = models.PositiveIntegerField(default=0)


class CinemaHall(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=10000)
    number_of_seats = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return f"title: {self.title}; number_of_seats: {self.number_of_seats}"


class MovieSeason(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=10000, null=True)
    img = models.ImageField()
    movie_session_start_date = models.DateField()
    movie_session_end_date = models.DateField()
    film_duration = models.TimeField()
    
    class Meta:
        ordering = ['movie_session_start_date']
    
    def __str__(self):
        return self.title


class CinemaSession(models.Model):
    movie_season = models.ForeignKey(MovieSeason, on_delete=models.CASCADE, null=False)
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE, null=False)
    movie_show_starts = models.DateTimeField(db_index=True)
    movie_show_ends = models.DateTimeField()
    empty_seats = models.PositiveIntegerField()
    ticket_price = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    
    class Meta:
        ordering = ['movie_show_starts']
        unique_together = ["cinema_hall", 'movie_show_starts']
    
    def __str__(self):
        return f"title: {self.movie_season}; movie_season: {self.movie_season};cinema_hall: {self.cinema_hall} " \
               f"movie_show_starts: {self.movie_show_starts}"
    
    def save(self, **kwargs):
        if self.pk is None:
            self.empty_seats = self.cinema_hall.number_of_seats
            
            film_duration = self.movie_season.film_duration
            self.movie_show_ends = self.movie_show_starts + timedelta(hours=film_duration.hour,
                                                                      minutes=film_duration.minute,
                                                                      seconds=film_duration.second)
        super().save(**kwargs)


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='purchases')
    cinema_session = models.ForeignKey(CinemaSession, on_delete=models.CASCADE, null=False)
    # movie_season = models.ForeignKey(MovieSeason, on_delete=models.CASCADE, null=False)
    # cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE, null=False)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    summ = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"user: {self.user}; cinema_session: {self.cinema_session}; quantity:{self.quantity}"
