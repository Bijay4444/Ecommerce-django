from django.shortcuts import render
# from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from . import serializers
from rest_framework.authentication import get_user_model
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class UserRegistrationView(CreateAPIView):
    serializer_class = serializers.UserSerializer
    