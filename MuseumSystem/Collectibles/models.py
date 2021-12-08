from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class category(models.Model):
    categoryName = models.CharField(max_length=10, verbose_name="类别")


class collectible(models.Model):
    name = models.CharField(max_length=20, verbose_name="藏品名")
    # pic
    time = models.CharField(max_length=10, verbose_name="年代", default="未知")
    category = models.ForeignKey(category, on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=16, verbose_name="藏品拜访地点")
    content = models.TextField(verbose_name="介绍")  # 后面改为富文本
    loves = models.IntegerField(verbose_name="喜爱数")


class love(models.Model):
    collectible = models.ForeignKey(collectible, on_delete=models.DO_NOTHING, verbose_name="藏品")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="用户")


class device(models.Model):
    collectible = models.ForeignKey(collectible, on_delete=models.DO_NOTHING, verbose_name="藏品")
    deviceId = models.CharField(max_length=64, verbose_name="监控设备号")


class light(models.Model):
    collectible = models.ForeignKey(collectible, on_delete=models.DO_NOTHING, verbose_name="藏品")
    lightID = models.CharField(max_length=16, verbose_name="灯光效果")


class monitorLimit(models.Model):
    collectible = models.ForeignKey(collectible, on_delete=models.DO_NOTHING, verbose_name="藏品")
    lowTemperature = models.FloatField(verbose_name="最低温度")
    highTemperature = models.FloatField(verbose_name="最高温度")
    lowHumidity = models.FloatField(verbose_name="最低湿度")
    highHumidity = models.FloatField(verbose_name="最高湿度")
    highSound = models.FloatField(verbose_name="最高声响")
    highlight = models.FloatField(verbose_name="最高亮度")
