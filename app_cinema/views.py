from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView

from app_cinema.forms import UserCreateForm
from app_cinema.models import CinemaSession, MovieSeason, Purchase, CinemaHall


# 1 главная список сеансов
# 2 конкретный сеанс + описание фильма с фото кнопокой купить
# 4 список покупок
# 5 список фильмы редактировать/добавить/удалить

# проверки
# 1 хватает денег
# 2 хватает мест
# 3 есть такой сеанс, зал, прьемьера
# 5 дата начала саенса больше чем сейчас
# 6 разрешать редактирование сеанса если еще нет продаж менять зал, цену,
# 7 создавать сеанс можно по периоду указаному в премьере фильма
#  время конца сеанса считаем из длительности фильма, число свободных мест из зала7


class CinemaSessionListView(ListView):
    login_url = 'login/'
    paginate_by = 10
    model = CinemaSession
    template_name = 'index.html'
    context_object_name = 'page_obj'
    
    # context_object_name = 'sessions_tomorrow'
    
    def get_queryset(self):
        # Получаем список сеансов на сегодня
        period_param = self.kwargs.get('period_param')
        if period_param == 'today':
            now = timezone.now()
            start_of_day = timezone.datetime.combine(now, timezone.datetime.min.time())
            end_of_day = timezone.datetime.combine(now, timezone.datetime.max.time())
            return CinemaSession.objects.filter(movie_show_starts__range=[start_of_day, end_of_day])
        elif period_param == 'tomorrow':
            tomorrow = timezone.now().date() + timezone.timedelta(days=1)
            start_of_day = timezone.datetime.combine(tomorrow, timezone.datetime.min.time())
            end_of_day = timezone.datetime.combine(tomorrow, timezone.datetime.max.time())
            return CinemaSession.objects.filter(movie_show_starts__range=[start_of_day, end_of_day])
        else:
            return CinemaSession.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем GET-параметр 'query_search' в контекст шаблона для отображения что искали по кнопке поиска
        query_search = self.request.GET.get('query_search')
        if query_search:
            context['query_search'] = query_search
        return context


class CinemaHallCreateView(LoginRequiredMixin, CreateView):
    model = CinemaHall
    login_url = 'login/'
    # success_url = reverse_lazy('returnconfirmationlist')
    success_url = reverse_lazy('index')
    # form_class = ReturnConfirmationForm
    fields = []


class MovieSeasonCreateView(LoginRequiredMixin, CreateView):
    model = MovieSeason
    login_url = 'login/'
    # fields = ['quantity', 'product', ]
    success_url = reverse_lazy('index')
    # form_class = PurchaseForm
    fields = []


class CinemaSessionCreateView(LoginRequiredMixin, CreateView):
    model = CinemaSession
    login_url = 'login/'
    # success_url = reverse_lazy('returnconfirmationlist')
    success_url = reverse_lazy('index')
    # form_class = ReturnConfirmationForm
    fields = []


class PurchaseListView(LoginRequiredMixin, ListView):
    login_url = 'login/'
    paginate_by = 5
    model = Purchase
    template_name = 'index.html'


class PurchaseCreateView(LoginRequiredMixin, CreateView):
    model = Purchase
    login_url = 'login/'
    # success_url = reverse_lazy('returnconfirmationlist')
    success_url = reverse_lazy('index')
    # form_class = ReturnConfirmationForm
    fields = []


class UserRegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreateForm
    success_url = '/'


class UserLoginView(LoginView):
    # https://ccbv.co.uk/projects/Django/4.1/django.contrib.auth.views/LoginView/
    success_url = '/'
    template_name = 'login.html'
    
    # def get_success_url(self):
    #     return self.success_url


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'