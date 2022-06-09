from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.
# 회사 모델
class Company(TimeStampedModel):
    company_name = models.CharField('회사명', max_length=50)
    country = models.CharField('국가', max_length=50)
    region = models.CharField('지역', max_length=50)

    def __str__(self):
        return self.company_name

    # 인덱스 생성
    class Meta:
        db_table = 'company'
        indexes = [
            models.Index(fields=('company_name',), name='company_name_idx'),
        ]
