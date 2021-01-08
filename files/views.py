from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import *


# class FileView(APIView):
#     def get(self, request):
#         files = File.objects.all()
#         serializer = FileSerializer(files, many=True)
#         return Response(serializer.data)
#
#
# class FileCreateView(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#     def post(self, request):
#         file = FileSerializer(data = request.data)
#
#         if file.is_valid(raise_exception=True):
#             file.save()
#         return Response(file.data)

#
# class FileDetailView(APIView):
#     def get(self, request, id):
#         file = File.objects.get(id = id)
#         serializer = FileSerializer(file, many=False)
#         return Response({'file':serializer.data})

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

