from django.db import models
from model_utils.models import TimeStampedModel

from company.models import Company


# Create your models here.
# 공고 모델
class Post(TimeStampedModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE) # 회사 모델 외래키
    position = models.CharField('채용포지션', max_length=50)
    compensation = models.PositiveIntegerField('채용보상금')
    skill = models.CharField('사용기술', max_length=50)
    content = models.TextField('채용내용')

    def __str__(self):
        return self.content

    # 인덱스 생성
    class Meta:
        db_table = 'post'
        indexes = [
            models.Index(fields=('position',), name='position_idx'),
            models.Index(fields=('skill',), name='skill_idx'),
        ]


