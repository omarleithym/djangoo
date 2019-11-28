from rest_framework import serializers
from .models import posts

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = posts
        fields = ['id', 'comment', 'username', 'userid']