import retail.models as retail_models
from django.contrib.auth.models import User, Group

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = retail_models.Store
        fields = '__all__'

class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = retail_models.Inventory
        fields = '__all__'

class PromotionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = retail_models.Promotion
        fields = '__all__'

class AlertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = retail_models.Alert
        fields = '__all__'