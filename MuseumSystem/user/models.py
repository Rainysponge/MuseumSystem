from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Sex(models.Model):
    sex = models.CharField(max_length=1)

    def __str__(self):
        return self.sex


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # portrait = models.ImageField('头像', upload_to=user_directory_path, blank=True, null=True)
    real_name = models.CharField(max_length=10, null=True, verbose_name="真实姓名")
    # loves = models.
    jurisdiction = models.IntegerField(default=1, verbose_name="权限")  # 0 管理员 1 游客

    # photo_resize = ImageSpecField(  # 注意：ImageSpecField 不会生成数据库表的字段
    #     source='portrait',
    #     processors=[ResizeToFill(148, 207)],  # 处理成一寸照片的大小
    #     format='JPEG',  # 处理后的图片格式
    #     options={'quality': 95}  # 处理后的图片质量
    # )

    # def photo_resize_url(self):
    #     if self.photo_resize and hasattr(self.photo_resize, 'url'):
    #         return self.photo_resize.url
    #     else:
    #         return '\\media\\upload\\default\\user.jpg'
    #
    # def __str__(self):
    #     return '<Profile: %s for %s>' % (self.nickname, self.user.username)
    #
    # def photo_url(self):
    #     if self.portrait and hasattr(self.portrait, 'url'):
    #         return self.portrait.url
    #     else:
    #         return '\\media\\upload\\default\\user.jpg'
