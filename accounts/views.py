from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serilaizers import RegistrationSerializer


class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        response_data = {
            'user': serializer.data,
            'token': {
                'access': access_token,
                'refresh': refresh_token,
            },
        }

        response = Response(response_data, status=status.HTTP_200_OK)
        response.set_cookie('access', access_token, httponly=True)
        response.set_cookie('refresh', refresh_token, httponly=True)

        return response
