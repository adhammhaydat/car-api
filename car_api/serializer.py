from rest_framework import serializers
from .models import Car

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model=Car
        fields=("id","title", "author", "body","created_at","updated_at")