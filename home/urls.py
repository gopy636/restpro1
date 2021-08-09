
from django.urls import path
from home .views import *

urlpatterns = [
    path('info/',todo_info),
    path('detail/<int:id>',todo_details),
    path('get_info/',TodoList.as_view()),
    path('todo/<int:id>/',TodoDetail.as_view()),
]
