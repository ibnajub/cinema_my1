from django.urls import path, include

from app_cinema.views import UserLoginView, UserRegisterView, UserLogoutView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    
    path('api/', include('app_cinema.api.urls')),
   
   

]