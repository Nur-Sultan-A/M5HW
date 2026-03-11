from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet
from .views import CategoryViewSet, TypeViewSet


router = DefaultRouter()
router.register('todos', TodoViewSet)
router.register("categories", CategoryViewSet)
router.register("types", TypeViewSet)


urlpatterns = [
    path('', include(router.urls))
]