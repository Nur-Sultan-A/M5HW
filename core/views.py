from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from .models import Category, Type
from .serializers import CategorySerializer, TypeSerializer


class TodoViewSet(viewsets.ModelViewSet):

    queryset = Todo.objects.filter(is_deleted=False)
    serializer_class = TodoSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TypeViewSet(viewsets.ModelViewSet):

    queryset = Type.objects.all()
    serializer_class = TypeSerializer