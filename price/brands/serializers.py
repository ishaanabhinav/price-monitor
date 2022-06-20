from django.contrib.auth.models import User, Group
import brands.models as brand_model
from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class BrandSerializer(CountryFieldMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = brand_model.Brand
        fields = '__all__'

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = brand_model.Product
        fields = '__all__'