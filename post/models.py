from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.contenttypes.fields import (
    GenericRelation,
    GenericForeignKey
)
from django.contrib.contenttypes.models import ContentType

from company.models import Company
from user.models import User


# Create your models here.
# 공고 모델
class Post(TimeStampedModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE) # 회사 모델 외래키
    position = models.CharField('채용포지션', max_length=50)
    compensation = models.PositiveIntegerField('채용보상금')
    skill = models.CharField('사용기술', max_length=50)
    content = models.TextField('채용내용')

    supported_user = models.ManyToManyField(
        User,
        through='post.Support',
        related_name='supported_post'
    )

    def __str__(self):
        return self.content

    # 인덱스 생성
    class Meta:
        db_table = 'post'
        indexes = [
            models.Index(fields=('position',), name='position_idx'),
            models.Index(fields=('skill',), name='skill_idx'),
        ]


# # 회사 다른 공고 모델
# class PostToCompany(models.Model):
#     content_type = models.ForeignKey(ContentType, related_name='content_type_post', on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')


# 지원 모델
class Support(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
