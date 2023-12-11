from rest_framework import serializers
from . import models

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id','s_name','s_age','s_gender']