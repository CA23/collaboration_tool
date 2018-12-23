from rest_framework import serializers
from . import models




class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Member