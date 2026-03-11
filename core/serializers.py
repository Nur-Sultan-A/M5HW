from rest_framework import serializers
from .models import Todo
from .models import Category, Type


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = "__all__"