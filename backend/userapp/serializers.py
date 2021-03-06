from rest_framework.serializers import ModelSerializer

from userapp.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
