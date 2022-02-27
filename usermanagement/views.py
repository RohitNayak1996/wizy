
from rest_framework.authentication import TokenAuthentication

from rest_framework.viewsets import ModelViewSet
# Create your views here.
from usermanagement.models import Movies, CustomUser
from usermanagement.serializers import MoviesSerializer, CustomUserSerializer


class MoviesView(ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    authentication_classes = (TokenAuthentication,)

class CustomUserView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = (TokenAuthentication,)