from rest_framework import viewsets
from .models import posts
from .serializers import PostSerializer
from rest_framework.authentication import TokenAuthentication
from . import permissions
from rest_framework import filters

class PostViewSet(viewsets.ModelViewSet):
    queryset = posts.objects.all().order_by('-id')
    serializer_class = PostSerializer
    authentication_classes= (TokenAuthentication,)  
    permission_classes = (permissions.update,)
    filter_backends = [filters.SearchFilter,]
    filter_fields= []
    search_fields = ['userid',] 

