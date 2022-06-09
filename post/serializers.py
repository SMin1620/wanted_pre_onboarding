from rest_framework import serializers

from post.models import Post
from company.models import Company


# 회사 시리얼라이저
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'company_name', 'country', 'region'
        ]


# 공고 목록 시리얼라이저
class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'company', 'position', 'compensation', 'skill'
        ]


# 공고 생성, 수정 시리얼라이저
class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'position', 'compensation',
            'skill', 'content'
        ]