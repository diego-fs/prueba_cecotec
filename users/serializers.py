#Third party imports
from rest_framework import serializers

#Local application imports
from .models import User
from django.core.validators import EmailValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')