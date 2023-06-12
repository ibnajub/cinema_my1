from django.utils import timezone
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication


class TokenExpiredAuthentication(TokenAuthentication):
    # урок 39, 47 минута
    def authenticate(self, request):
        user, token = super.authenticate(request=request)
        if (timezone.now() - token.created).seconds > 10:
            raise exceptions.AuthenticationFailed('More than 10 second ')
        return user, token
