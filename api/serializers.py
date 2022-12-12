from django.db import models
from django.db.models import fields
from pyexpat import model
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from django.contrib.auth.models import User
from .models import Person
from .models import Batch
from .models import BatchesInfo
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  =  User
        fields = "__all__"
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model  =  Person
        fields = "__all__"
class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model  =  Batch
        fields = "__all__"
class BatchesInfoSerializer(serializers.ModelSerializer):
    batch = BatchSerializer(many=False)
    class Meta:
        model  =  BatchesInfo
        fields = "__all__"