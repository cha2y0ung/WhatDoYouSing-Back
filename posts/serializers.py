from rest_framework import serializers
from .models import *
from django.db.models import Q
from rest_framework.serializers import ReadOnlyField
from datetime import datetime, timedelta

class FunctionMixin:
    
    def get_author_nickname(self, obj):
        return obj.author.nickname
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_comment_count(self, obj):
        return obj.comment.count() 
    
    def get_recomments_count(self, obj):
        return obj.recomments.count()
    
    def get_com_count(self, obj):
        comment_count = obj.comment_count()
        recomment_count = obj.recomment_count()

        return comment_count + recomment_count
    
    def get_com_likes_count(self, obj):
        return obj.com_likes.count()
    
    def get_com_relikes_count(self, obj):
        return obj.com_relikes.count()
    
    
class PostSerializer(FunctionMixin, serializers.ModelSerializer):
    #comment_count = serializers.SerializerMethodField()
    author_nickname = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [ 
            "id",
            "author",
            "author_nickname",
            "lyrics",
            "content",
            "title",
            "singer",
            "link",
            "sings_emotion",
            "likes_count",
            "scrap",
            "created_at",
        ]

        read_only_fields = ["author"]

class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emotion
        fields=['emo_id','content','emo_post','emo_user']