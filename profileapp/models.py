from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # user 와 1대1로 연결 / on_del : 이게 지워질경우 어떻게 할것인가, 삭제 정책 담당 (CASCADE = 종속)

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=30, unique=True, null=True) #Charfiled 의 필수값 : max_length
    message = models.CharField(max_length=200, null=True)