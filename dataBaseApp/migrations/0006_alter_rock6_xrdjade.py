# Generated by Django 4.1.3 on 2023-07-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataBaseApp', '0005_alter_rock_options_alter_rock1_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rock6',
            name='xrdJade',
            field=models.ImageField(upload_to='images/', verbose_name='Jade定量分析'),
        ),
    ]