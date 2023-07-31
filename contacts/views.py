import random
import string

from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound

from .serializers import *
from .models import *
from rest_framework import viewsets, status, request
from rest_framework.filters import SearchFilter
from rest_framework.filters import SearchFilter


class CustomPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 10
    page_size_query_param = 'page_size'


class ContactViewset(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['name', 'mobile_number']
    pagination_class = CustomPagination

    """
    this api is used for filter data according to name where name is unique=True in model field so we use get here 
    it handle 2 method get and delete if method is get it simply return data if delete then it delete record   
    """
    @action(detail=False,methods=['Get','Delete'],url_path='contact-name')
    def filter_contact_using_name(self,request):
        name = self.request.query_params['name']

        try:
            obj =Contact.objects.get(name=name)
            serializer =ContactSerializer(obj)
            if request.method == "DELETE":
                obj.delete()
                return Response({"message": f"Contact '{name}' deleted successfully."},
                                status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(serializer.data, status=status.HTTP_200_OK)
        except NotFound:
            return Response( status=status.HTTP_400_BAD_REQUEST)



# def generate_random_data():
#     email = "gmail.com"
#     for i in range(101):
#         name = "".join(random.choices(string.ascii_lowercase, k=5))
#         emaill = "".join(random.choices(string.ascii_lowercase, k=7))
#         emaill+=email
#         m = random.randint(10**9, 10**10 - 1)
#         c=Contact.objects.create(name=name,email=emaill,mobile_number=int(m))
#         c.save()

