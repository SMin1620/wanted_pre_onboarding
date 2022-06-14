from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# 사용자 모델
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'M', '남성'
        FEMALE = 'F', '여성'

    first_name = None
    last_name = None
    date_joined = None

    name = models.CharField('이름', max_length=100)
    gender = models.CharField('성별', max_length=4, blank=True, choices=GenderChoices.choices)

    created_at = models.DateTimeField('생성 날짜', auto_now_add=True)
    modified_at = models.DateTimeField('수정 날짜', auto_now=True)

    class Meta:
        db_table = 'user'
