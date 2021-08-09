from home.models import Todo
from home.serializers import TodoSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework .decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator

@api_view(['GET','POST'])
def todo_info(request):

    if request.method== 'GET':
        todo=Todo.objects.all()
        serializer=TodoSerializer(todo, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':

        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','DELETE'])
def todo_details(request,id):

    try:
        todo =Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    elif request.method == 'PATCH':
        serializer = TodoSerializer(todo, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TodoList(APIView):
    
    def get(self, request, format=None):
        data=request.data
        todo = Todo.objects.all()
        paginator = Paginator(todo,2)
        page_no = paginator.get_page(data.get("page_no"))
        serializer = TodoSerializer(page_no,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class TodoDetail(APIView):
    
    def get_object(self,id):
        try:
            return Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        todo = self.get_object(id)
        serializer =TodoSerializer(todo)
        return Response({'data' : serializer.data})


    def put(self, request, id, format=None):
        todo = self.get_object(id)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data})
        return Response({'errors':serializer.errors,'status':status.HTTP_400_BAD_REQUEST})

    def patch(self, request, id, format=None):
        todo = self.get_object(id)
        serializer = TodoSerializer(todo, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data})
        return Response({'errors':serializer.errors,
                          'status':status.HTTP_400_BAD_REQUEST,
                          })
        

    def delete(self, request, id, format=None):
        todo = self.get_object(id)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
