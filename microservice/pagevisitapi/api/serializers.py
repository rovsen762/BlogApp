from rest_framework import serializers
from pagevisitapi.models import PageVisit

class PageVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageVisit
        fields = '__all__'