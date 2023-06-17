from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from menu.models import Equipo
from .serializers import EquipoSerializers
from menu.models import Tecnico
from .serializers import TecnicoSerializers

@csrf_exempt
@api_view(['GET','POST'])

def lista_Equipo(request):

    if request.method == 'GET':
        equipos = Equipo.objects.all()
        serializer = EquipoSerializers(equipos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EquipoSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])

def lista_Tecnico(request):
    if request.method == 'GET':
        tecnicos = Tecnico.objects.all()
        serializer = TecnicoSerializers(tecnicos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TecnicoSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)