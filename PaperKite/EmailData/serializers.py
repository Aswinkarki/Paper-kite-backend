from rest_framework import serializers
from .models import EmailData

class EmailDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailData
        fields = '__all__'
