# Generated by Django 2.2 on 2021-12-08 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=10, verbose_name='类别')),
            ],
        ),
        migrations.CreateModel(
            name='collectible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='藏品名')),
                ('time', models.CharField(default='未知', max_length=10, verbose_name='年代')),
                ('location', models.CharField(max_length=16, verbose_name='藏品拜访地点')),
                ('content', models.TextField(verbose_name='介绍')),
                ('loves', models.IntegerField(verbose_name='喜爱数')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Collectibles.category')),
            ],
        ),
        migrations.CreateModel(
            name='monitorLimit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lowTemperature', models.FloatField(verbose_name='最低温度')),
                ('highTemperature', models.FloatField(verbose_name='最高温度')),
                ('lowHumidity', models.FloatField(verbose_name='最低湿度')),
                ('highHumidity', models.FloatField(verbose_name='最高湿度')),
                ('highSound', models.FloatField(verbose_name='最高声响')),
                ('highlight', models.FloatField(verbose_name='最高亮度')),
                ('collectible', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Collectibles.collectible', verbose_name='藏品')),
            ],
        ),
        migrations.CreateModel(
            name='love',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collectible', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Collectibles.collectible', verbose_name='藏品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='light',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lightID', models.CharField(max_length=16, verbose_name='灯光效果')),
                ('collectible', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Collectibles.collectible', verbose_name='藏品')),
            ],
        ),
        migrations.CreateModel(
            name='device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceId', models.CharField(max_length=64, verbose_name='监控设备号')),
                ('collectible', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Collectibles.collectible', verbose_name='藏品')),
            ],
        ),
    ]