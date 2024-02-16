from rest_framework.serializers import ModelSerializer
from .models import Gift

class GiftSerializer(ModelSerializer):
    class Meta:
        model = Gift
        fields = '__all__'
