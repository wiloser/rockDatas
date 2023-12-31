# Generated by Django 4.1.3 on 2023-07-15 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataBaseApp', '0011_alter_rock2_elasticmodulus_alter_rock2_poissonsratio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rock3',
            name='poissonsRatio',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='泊松比'),
        ),
        migrations.AlterField(
            model_name='rock3',
            name='rockCohesion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='内聚力'),
        ),
        migrations.AlterField(
            model_name='rock3',
            name='rockInternalFrictionAngle',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='内摩擦角'),
        ),
        migrations.AlterField(
            model_name='rock3',
            name='triaxialCompressiveStrength',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='三轴抗压强度'),
        ),
        migrations.AlterField(
            model_name='rock3',
            name='youngModulus',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='杨氏模量'),
        ),
        migrations.AlterField(
            model_name='rock4',
            name='tensileFailureLoad',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='破坏荷载'),
        ),
        migrations.AlterField(
            model_name='rock4',
            name='tensileStrength',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='抗拉强度'),
        ),
        migrations.AlterField(
            model_name='rock5',
            name='shearingStrength',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='抗剪强度'),
        ),
        migrations.AlterField(
            model_name='rock7',
            name='rockDynamicStrength',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='岩石动态强度'),
        ),
        migrations.AlterField(
            model_name='rock7',
            name='rockProctorsCoefficient',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='普氏系数'),
        ),
        migrations.AlterField(
            model_name='rock7',
            name='rockStaticStrength',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='岩石静态强度'),
        ),
        migrations.AlterField(
            model_name='rock7',
            name='surfaceArrayPitch',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='排距/抵抗线'),
        ),
        migrations.AlterField(
            model_name='rock7',
            name='surfaceBoreDiameter',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='孔径'),
        ),
        migrations.AlterField(
            model_name='rock7',
            name='surfaceDistance',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='孔距'),
        ),
        migrations.AlterField(
            model_name='rock7',
            name='surfaceHoleDepth',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='孔深'),
        ),
        migrations.AlterField(
            model_name='rock7',
            name='surfaceSpecificCharge',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='露天炸药单耗'),
        ),
        migrations.AlterField(
            model_name='rock7',
            name='surfaceSuperDeep',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='超深'),
        ),
        migrations.AlterField(
            model_name='rock8',
            name='excavationBoreholeDiameter',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='炮孔直径'),
        ),
        migrations.AlterField(
            model_name='rock8',
            name='excavationBoreholeNumber',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='炮孔数量'),
        ),
        migrations.AlterField(
            model_name='rock8',
            name='excavationCutCharge',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='掏槽单耗'),
        ),
        migrations.AlterField(
            model_name='rock8',
            name='excavationHollowholeDiameter',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='空孔直径'),
        ),
        migrations.AlterField(
            model_name='rock8',
            name='excavationSectionArea',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='断面面积'),
        ),
        migrations.AlterField(
            model_name='rock8',
            name='excavationSpecificCharge',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='掘进炸药单耗'),
        ),
        migrations.AlterField(
            model_name='rock9',
            name='stopeArrayPitch',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='排距/最小抵抗线'),
        ),
        migrations.AlterField(
            model_name='rock9',
            name='stopeBoreholeDiameter',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='炮孔直径'),
        ),
        migrations.AlterField(
            model_name='rock9',
            name='stopeCollapseStepDistance',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='崩矿步距'),
        ),
        migrations.AlterField(
            model_name='rock9',
            name='stopeDistance',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='孔距/孔底距'),
        ),
        migrations.AlterField(
            model_name='rock9',
            name='stopeDriftInterval',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='进路间距'),
        ),
        migrations.AlterField(
            model_name='rock9',
            name='stopeEdgeHoleAngle',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='边孔角'),
        ),
        migrations.AlterField(
            model_name='rock9',
            name='stopeSpecificCharge',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='回采炸药单耗'),
        ),
        migrations.AlterField(
            model_name='rock9',
            name='stopeSublevelHeight',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='分段高度'),
        ),
    ]
