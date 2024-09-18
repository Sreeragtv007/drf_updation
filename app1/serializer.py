from rest_framework import serializers

from .models import *

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
        
        
    def validate(self, attrs):
        if attrs['age' > 10]:
            raise serializers.ValidationError('age greater than 10')