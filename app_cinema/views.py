from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView

from app_cinema.forms import UserCreateForm
from app_cinema.models import CinemaSession


# 1 главная список премьер
# 2 конкретный сеанс + описание фильма с фото
# 3 редактирование премьер/создание вместе с ними сеансов циклом по датам
# 4 покупки

# проверки
# 1 хватает денег
# 2 хватает мест
# 3 есть такой сеанс, зал, прьемьера
# 5 дата начала саенса больше чем сейчас
# 6 разрешать редактирование сеанса если еще нет продаж менять зал, цену,


class CinemaSessionListView(ListView):
    login_url = 'login/'
    paginate_by = 10
    model = CinemaSession
    template_name = 'index.html'
    
    # context_object_name = 'sessions_today'
    # context_object_name = 'sessions_tomorrow'
    
    def get_queryset(self):
        # Получаем список сеансов на сегодня
        now = timezone.now()
        # Получаем список сеансов на завтра
        tomorrow = timezone.now().date() + timezone.timedelta(days=1)
        return CinemaSession.objects.filter(start_date=now)


class UserRegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreateForm
    success_url = '/'


class UserLoginView(LoginView):
    # https://ccbv.co.uk/projects/Django/4.1/django.contrib.auth.views/LoginView/
    success_url = reverse_lazy('index')
    template_name = 'login.html'
    
    def get_success_url(self):
        return self.success_url


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'