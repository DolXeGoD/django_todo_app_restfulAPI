from .models import TbTodoList
from rest_framework import serializers

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TbTodoList
        fields = ('no', 'title', 'content', 'is_complete', 'end_date', 'priority')

class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbTodoList
        fields = ('no', 'title', 'content', 'is_complete', 'end_date', 'priority')

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbTodoList
        fields = ('title', 'content', 'end_date')