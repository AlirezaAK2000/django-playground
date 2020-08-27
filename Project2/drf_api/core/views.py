from django.shortcuts import render
from django.http import JsonResponse


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import mixins

from .serializer import PostSerializer
from .models import Post


class PostCreateView(generics.CreateAPIView,
        mixins.ListModelMixin
    ):   
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self , request , *args , **kwargs):
        return self.list(request , *args , **kwargs)


class PostView( mixins.ListModelMixin
    ,mixins.CreateModelMixin
    ,generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self , request , *args , **kwargs):
        return self.list(request , *args , **kwargs)


    def post(self , request , *args , **kwargs):
        return self.create(request , *args , **kwargs)



# class ModelListCreateView(mixins.ListCreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

class TestView(APIView):

    permission_class = (
        IsAuthenticated,
    )

    def get(self , request , *args , **kwargs):
        qs = Post.objects.all()
        serializer  = PostSerializer(qs, many=True)
        return Response(serializer.data)   
        
    def post(self , request , *args , **kwargs):

        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

