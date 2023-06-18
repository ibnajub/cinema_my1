from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from app_cinema.views import UserLoginView, UserRegisterView, UserLogoutView, CinemaSessionListView, \
    MovieSeasonCreateView

urlpatterns = [
    path('', CinemaSessionListView.as_view(), name='index'),
    path('session_period/<str:period_param>/', CinemaSessionListView.as_view(), name='session_period'),
    
    path('add_movie', MovieSeasonCreateView.as_view(), name='add_movie'),
    
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    
    path('api/', include('app_cinema.api.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
