from rest_framework .serializers import ModelSerializer
from .models import *

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ['task_name','task_descriptions','task_status' ]
        read_only_fields = ('created_at', 'update_at')


        