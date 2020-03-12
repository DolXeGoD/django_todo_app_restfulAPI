from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import TbTodoList
from .serializers import TodoSerializer, TodoDetailSerializer
# Create your views here.
from rest_framework import viewsets

# class TodoBoard_restapi_main(viewsets.ModelViewSet):
#     queryset = TbTodoList.objects.all()
#     serializer_class = TodoSerializer

class TodoBoard_restapi_main(ListAPIView):
    queryset = TbTodoList.objects.all()
    serializer_class = TodoSerializer

class TodoBoard_restapi_detail(RetrieveAPIView):
    lookup_field = 'no'
    queryset = TbTodoList.objects.all()
    serializer_class = TodoDetailSerializer