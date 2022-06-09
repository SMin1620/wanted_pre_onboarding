from django.conf import settings

from user.models import User


# 유저 더미 데이터
def gen_master(apps, schema_editor):
    # 슈퍼 유저 생성
    User.objects.create_superuser(
        username='admin',
        password='admin',
        name='관리자',
        email='admin@email.com',
        gender=User.GenderChoices.MALE
    )

    # 일반 유저 생성
    for id in range(2, 6):
        username = f"user{id}"
        password = f"user{id}"
        user = f"user{id}"
        email = f"user{id}@email.com"
        gender = User.GenderChoices.MALE

        # 일반 유저 생성
        User.objects.create_user(
            username=username,
            password=password,
            name=user,
            email=email,
            gender=gender
        )

