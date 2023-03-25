from rest_framework import serializers
from .models import humans

class dataSerializers(serializers.ModelSerializer):
       class Meta:
             model=humans
             fields="__all__"