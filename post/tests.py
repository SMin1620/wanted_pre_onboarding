import json
from rest_framework.test import APITestCase, APIClient

from user.models import User
from post.models import Post, Support
from company.models import Company


# Create your tests here.
class PostTest(APITestCase):
  client = APIClient()

  def setUp(self):
    # 슈퍼 유저 생성
    user = User.objects.create_superuser('admin1', 'admin1@email.com', 'admin1')
    self.user = user

    # 회사 생성
    company = Company.objects.create(
      company_name='원티드',
      country='한국',
      region='서울'
    )
    company.save()
    self.company = company
    self.assertIsInstance(company, Company)

    # 공고 생성
    post = Post.objects.create(
      company=self.company,
      position='포지션',
      compensation=1000000,
      skill='사용기술',
      content='채용내용'
    )
    post.save()
    self.post = post
    self.assertIsInstance(post, Post)

  ## === GET TEST ===
  # post list
  def test_post_list(self):
    response = self.client.get(
      f'/api/post/',
      content_type='application/json'
    )
    self.assertEqual(response.status_code, 200)

  # post detail
  def test_post_detail(self):
    response = self.client.get(
      f'/api/post/{self.post.id}/',
      content_type='application/json'
    )
    self.assertEqual(response.status_code, 200)

  ## === POST, SUPPORT TEST ===
  # post create
  def test_create_post(self):
    context = {
      'company': self.company.id,
      'position': '테스트 포지션',
      'compensation': 1000000,
      'skill': '테스트 기술',
      'content': '테스트 내용'
    }
    response = self.client.post(
      f'/api/post/',
      json.dumps(context),
      content_type='application/json'
    )
    self.assertEqual(response.status_code, 201)

  # post support
  def test_support_post(self):
    self.client.login(username='admin1', password='admin1')

    context = {
      'user': self.user.id,
      'post': self.post.id
    }
    self.client.login()
    response = self.client.post(
      f'/api/post/{self.post.id}/support/',
      json.dumps(context),
      content_type='application/json'
    )
    self.assertEqual(response.status_code, 200)

  ## === PATCH, DELETE TEST ===
  # post update
  def test_update_post(self):
    context = {
      'content': '수정된 내용'
    }
    response = self.client.patch(
      f'/api/post/{self.post.id}/',
      json.dumps(context),
      content_type='application/json'
    )
    self.assertEqual(response.status_code, 200)

  # post delete
  def test_delete_post(self):
    response = self.client.delete(
      f'/api/post/{self.post.id}/',
      content_type='application/json'
    )
    self.assertEqual(response.status_code, 204)







