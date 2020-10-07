from rest_framework import serializers
from cars.models import Car


class CarDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = '__all__'  # виводить все поля
        #fields = ['vin', 'color', 'brand', 'user', 'car_type']


class CarsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'vin', 'user']