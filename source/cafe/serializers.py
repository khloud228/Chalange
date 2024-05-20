from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Product, RuTag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    retry_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'retry_password')
        extra_kwargs = {'password': {'write_only': True}, 'email': {'required': False}}

    def validate_email(self, value):
        if value:
            return value[0].lower() + value[1:]
    
    def validate(self, data):
        if data['password'] != data['retry_password']:
            raise serializers.ValidationError({'password':'Пароли не совпадают'})
        return data
    
    def create(self, validated_data):
        user = User(
                username=validated_data['username']
            )
        
        if 'email' in validated_data:
            user.email = validated_data['email']
        user.set_password(validated_data['password'])
        user.save()
        return user


class RuTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuTag
        fields = '__all__' # ('id', 'name',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' # ('id', 'name', 'description')
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'}
        # }
