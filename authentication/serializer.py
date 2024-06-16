from rest_framework import serializers
from authentication.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('created_at', 'updated_at', 'is_staff',
                   'is_active', 'date_joined', 'groups', 'user_permissions', 'is_superuser', 'last_login')


