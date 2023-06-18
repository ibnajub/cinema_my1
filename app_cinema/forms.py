from django.contrib.auth.forms import UserCreationForm

from app_cinema.models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'money']
    
    # def __init__(self, *args, **kwargs):
    #     super(UserCreateForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['money'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['password1'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['password2'].widget.attrs.update({'class': 'form-control'})
