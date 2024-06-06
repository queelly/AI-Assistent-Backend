from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('is_staff', 'created_at', 'updated_at', 'is_staff',
                   'is_active')


