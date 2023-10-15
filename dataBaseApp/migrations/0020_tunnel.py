# Generated by Django 4.2.5 on 2023-10-15 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataBaseApp', '0019_segmentation_alter_schema_velocity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tunnel',
            fields=[
                ('tunnel_name', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='巷道名称')),
                ('tunnel1_name', models.CharField(max_length=255, verbose_name='巷道1名称')),
                ('tunnel2_name', models.CharField(max_length=255, verbose_name='巷道2名称')),
                ('tunnel3_name', models.CharField(max_length=255, verbose_name='巷道3名称')),
                ('tunnel4_name', models.CharField(max_length=255, verbose_name='巷道4名称')),
                ('tunnel5_name', models.CharField(max_length=255, verbose_name='巷道5名称')),
                ('tunnel6_name', models.CharField(max_length=255, verbose_name='巷道6名称')),
                ('tunnel7_name', models.CharField(max_length=255, verbose_name='巷道7名称')),
                ('tunnel8_name', models.CharField(max_length=255, verbose_name='巷道8名称')),
                ('tunnel9_name', models.CharField(max_length=255, verbose_name='巷道9名称')),
                ('tunnel10_name', models.CharField(max_length=255, verbose_name='巷道10名称')),
            ],
            options={
                'verbose_name': '工程数据库中的地底下矿2',
                'verbose_name_plural': '工程数据库中的地底下矿2',
            },
        ),
    ]
