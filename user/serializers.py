from rest_framework import serializers
from rest_framework.validators import UniqueValidator
# from .models import User

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ('is_staff', 'is_active', 'date_joined',
                            'is_superuser', 'groups', 'user_permissions',
                            'last_login')
        fields = ('id', 'username', 'email')


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    def validate(self, data):
        username = data.get('email')
        password = data.get('password')
        if not username:
            raise serializers.ValidationError({"email": ["Enter a valid email address."]})
        if not password:
            raise serializers.ValidationError({"password": ["Enter password"]})

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return data
        raise serializers.ValidationError({"email": [u'%s is already in use.' % username]})
