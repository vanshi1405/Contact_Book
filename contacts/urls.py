from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
router =DefaultRouter()
router.register('contac',viewset=ContactViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include("rest_framework.urls")),
]