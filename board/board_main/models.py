from typing import Any
from django.db import models

# Create your models here.
# models.py의 클래스와 DB의 table과 sync를 맞춰 테이블(컬럼정보) 자동생성.

# 클래스명 = 테이블명, 변수=컬럼명
class Test(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=30)

class Author(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=30)
    # DB설정에 default timestamp가 걸리는 것이아닌, 장고가 현재시간을 db에 insert
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # DB에는 fk를 설정한 변수명에 _id 가 붙게 된다.
    # on_delete = models.CASCADE, 
    # db에 author_id는 파이썬에서는 author객체와 같은것.
    author = models.ForeignKey(Author, on_delete=models.SET_NULL ,null=True, related_name='posts')

    
