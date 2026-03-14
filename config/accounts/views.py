from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SignupSerializer


@api_view(["POST"])
def signup(request):

    serializer = SignupSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def food_view(request):

    user = request.user

    if user.role == "admin":

        vegetables = ["carrot", "broccoli", "spinach"]

        return Response({
            "role": "admin",
            "data": vegetables
        })

    else:

        fruits = ["apple", "banana", "mango"]

        return Response({
            "role": "user",
            "data": fruits
        })