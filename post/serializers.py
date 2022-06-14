from rest_framework import serializers

from post.models import (
    Post,
    Support
)
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
    company_name = serializers.SerializerMethodField(read_only=True)
    company_country = serializers.SerializerMethodField(read_only=True)
    company_region = serializers.SerializerMethodField(read_only=True)

    # 회사 이름
    def get_company_name(self, obj):
        return obj.company.company_name

    # 회사 거주 나라
    def get_company_country(self, obj):
        return obj.company.country

    # 회사 지역
    def get_company_region(self, obj):
        return obj.company.region

    class Meta:
        model = Post
        fields = [
            'id', 'company_name', 'company_country', 'company_region',
            'position', 'compensation', 'skill', 'created'
        ]


# 공고 상세 시리얼라이저
class PostDetailSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField(read_only=True)
    company_country = serializers.SerializerMethodField(read_only=True)
    company_region = serializers.SerializerMethodField(read_only=True)

    # 회사 이름
    def get_company_name(self, obj):
        return obj.company.company_name

    # 회사 거주 나라
    def get_company_country(self, obj):
        return obj.company.country

    # 회사 지역
    def get_company_region(self, obj):
        return obj.company.region

    class Meta:
        model = Post
        fields = [
            'id', 'company_name', 'company_country', 'company_region',
            'position', 'compensation', 'skill',
            'content', 'created', 'supported_user',
        ]


# 공고 생성, 수정 시리얼라이저
class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'company', 'position', 'compensation', 'skill', 'content'
        ]

        write_only_fields = [
            'company'
        ]


# 지원 시리얼라이저
class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        read_only_fields = [
            'post', 'user'
        ]
        fields = [
            'user', 'post'
        ]