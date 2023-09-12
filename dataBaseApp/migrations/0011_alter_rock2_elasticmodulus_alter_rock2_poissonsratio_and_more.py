# Generated by Django 4.1.3 on 2023-07-15 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataBaseApp', '0010_alter_rock2_uniaxialcrackmorphology_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rock2',
            name='elasticModulus',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='弹性模量'),
        ),
        migrations.AlterField(
            model_name='rock2',
            name='poissonsRatio',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='泊松比'),
        ),
        migrations.AlterField(
            model_name='rock2',
            name='uniaxialCompressiveStrength',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='单轴抗压强度'),
        ),
    ]