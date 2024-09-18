from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *

# Create your views here.
@api_view(['GET','POST'])
def test(request):
    if request.method == 'GET':
        obj=Students.objects.all()
        serializers=studentserializer(obj,many=True)
        return Response(serializers.data)
    elif request.method =='POST':
        data=request.data
        serializers=studentserializer(data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    elif request.method == 'PUT':
        data=request.data
        serializers=studentserializer(data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        