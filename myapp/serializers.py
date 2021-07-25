from rest_framework import serializers
from myapp.models import MyUser


class EmailSignUpSerailzier(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'first_name', 'last_name', 'password', 'mobile_number', 'username']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = MyUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
