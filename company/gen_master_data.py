from django.conf import settings

from company.models import Company


# 회사 더미 데이터
def gen_master(apps, schema_editor):
    Company.objects.create(
        company_name='네이버',
        country='한국',
        region='서울'
    )
    Company.objects.create(
        company_name='카카오',
        country='한국',
        region='서울'
    )
    Company.objects.create(
        company_name='NCSOFT',
        country='한국',
        region='서울'
    )
