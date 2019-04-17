from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.

class UserProfile(AbstractUser):
    # 定义头像，用户名，生日，性别，地址，联系电话，添加时间
    image = models.ImageField(upload_to='user/',verbose_name='用户头像',null=True,blank=True)
    nick_name = models.CharField(max_length=20,verbose_name='用户名',null=True,blank=True)
    birthday = models.DateTimeField(verbose_name='用户生日',null=True,blank=True)
    gender = models.CharField(choices=(('girl','女'),('boy','男')),verbose_name='用户性别',max_length=20,default='girl')
    address = models.CharField(max_length=100,verbose_name='用户地址',null=True,blank=True)
    phone = models.CharField(max_length=11,verbose_name='用户手机')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name