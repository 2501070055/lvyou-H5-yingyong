# Generated by Django 3.1.7 on 2021-04-06 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='名称')),
                ('desc', models.CharField(max_length=256, verbose_name='描述')),
                ('main_img', models.ImageField(max_length=256, upload_to='%Y%m/sight', verbose_name='主图')),
                ('banner_img', models.ImageField(max_length=256, upload_to='%Y%m/sight', verbose_name='详情主图')),
                ('content', models.TextField(verbose_name='详细')),
                ('score', models.FloatField(default=5, verbose_name='评分')),
                ('min_price', models.FloatField(default=0, verbose_name='最低价格')),
                ('province', models.CharField(max_length=32, verbose_name='省份')),
                ('city', models.CharField(max_length=32, verbose_name='市区')),
                ('area', models.CharField(max_length=32, null=True, verbose_name='区/县')),
                ('town', models.CharField(max_length=32, null=True, verbose_name='乡镇')),
                ('is_top', models.BooleanField(default=False, verbose_name='是否为精选')),
                ('is_hot', models.BooleanField(default=False, verbose_name='是否为热门')),
                ('is_valid', models.BooleanField(default=True, verbose_name='逻辑删除')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'db_table': 'sight',
                'ordering': ['-updated_at'],
            },
        ),
    ]