from django.shortcuts import render
from rest_framework import generics #, permissions
# Create your views here.
from .permissions import IsAuthorOrReadOnly #
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
