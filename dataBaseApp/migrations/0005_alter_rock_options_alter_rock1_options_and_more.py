# Generated by Django 4.2.2 on 2023-07-09 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("dataBaseApp", "0004_alter_rock1_rocktype"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="rock",
            options={"verbose_name": "岩石", "verbose_name_plural": "岩石"},
        ),
        migrations.AlterModelOptions(
            name="rock1",
            options={"verbose_name": "岩石物性库", "verbose_name_plural": "岩石物性库"},
        ),
        migrations.AlterModelOptions(
            name="rock2",
            options={
                "verbose_name": "力学实验库的单轴压缩实验",
                "verbose_name_plural": "力学实验库的单轴压缩实验",
            },
        ),
        migrations.AlterModelOptions(
            name="rock3",
            options={
                "verbose_name": "力学实验库的三轴压缩实验",
                "verbose_name_plural": "力学实验库的三轴压缩实验",
            },
        ),
        migrations.AlterModelOptions(
            name="rock4",
            options={
                "verbose_name": "力学实验库的抗拉强度实验",
                "verbose_name_plural": "力学实验库的抗拉强度实验",
            },
        ),
        migrations.AlterModelOptions(
            name="rock5",
            options={
                "verbose_name": "力学实验库的直接剪切实验",
                "verbose_name_plural": "力学实验库的直接剪切实验",
            },
        ),
        migrations.AlterModelOptions(
            name="rock6",
            options={
                "verbose_name": "力学实验库的XRD衍射实验",
                "verbose_name_plural": "力学实验库的XRD衍射实验",
            },
        ),
        migrations.AlterModelOptions(
            name="rock7",
            options={
                "verbose_name": "工程数据库中的露天爆破",
                "verbose_name_plural": "工程数据库中的露天爆破",
            },
        ),
        migrations.AlterModelOptions(
            name="rock8",
            options={
                "verbose_name": "工程数据库中的掘进爆破",
                "verbose_name_plural": "工程数据库中的掘进爆破",
            },
        ),
        migrations.AlterModelOptions(
            name="rock9",
            options={
                "verbose_name": "工程数据库中的回采爆破",
                "verbose_name_plural": "工程数据库中的回采爆破",
            },
        ),
        migrations.AlterField(
            model_name="rock",
            name="rock_id",
            field=models.CharField(
                max_length=255, primary_key=True, serialize=False, verbose_name="岩石ID"
            ),
        ),
        migrations.AlterField(
            model_name="rock",
            name="rock_name",
            field=models.CharField(max_length=255, verbose_name="岩石名称"),
        ),
        migrations.AlterField(
            model_name="rock1",
            name="key",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="dataBaseApp.rock",
                verbose_name="岩石",
            ),
        ),
        migrations.AlterField(
            model_name="rock1",
            name="rockDensity",
            field=models.CharField(max_length=255, verbose_name="岩石密度"),
        ),
        migrations.AlterField(
            model_name="rock1",
            name="rockLongitudinalWaveVelocity",
            field=models.CharField(max_length=255, verbose_name="岩石纵波速度"),
        ),
        migrations.AlterField(
            model_name="rock1",
            name="rockOrigin",
            field=models.CharField(max_length=255, verbose_name="岩石产地"),
        ),
        migrations.AlterField(
            model_name="rock1",
            name="rockPermeabilityCoefficient",
            field=models.CharField(max_length=255, verbose_name="岩石渗透系数"),
        ),
        migrations.AlterField(
            model_name="rock1",
            name="rockPorosity",
            field=models.CharField(max_length=255, verbose_name="岩石孔隙度"),
        ),
        migrations.AlterField(
            model_name="rock1",
            name="rockTransverseWaveVelocity",
            field=models.CharField(max_length=255, verbose_name="岩石横波速度"),
        ),
        migrations.AlterField(
            model_name="rock1",
            name="rockType",
            field=models.CharField(
                choices=[("沉积岩", "沉积岩"), ("岩浆岩", "岩浆岩"), ("变质岩", "变质岩")],
                max_length=255,
                verbose_name="岩石类型",
            ),
        ),
        migrations.AlterField(
            model_name="rock1",
            name="rockWaterAbsorption",
            field=models.CharField(max_length=255, verbose_name="岩石吸水率"),
        ),
        migrations.AlterField(
            model_name="rock1",
            name="rockWaveImpedance",
            field=models.FloatField(null=True, verbose_name="岩石波阻抗"),
        ),
        migrations.AlterField(
            model_name="rock2",
            name="elasticModulus",
            field=models.FloatField(null=True, verbose_name="弹性模量"),
        ),
        migrations.AlterField(
            model_name="rock2",
            name="key",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="dataBaseApp.rock",
                verbose_name="岩石",
            ),
        ),
        migrations.AlterField(
            model_name="rock2",
            name="poissonsRatio",
            field=models.FloatField(null=True, verbose_name="泊松比"),
        ),
        migrations.AlterField(
            model_name="rock2",
            name="uniaxialCompressiveStrength",
            field=models.FloatField(null=True, verbose_name="单轴抗压强度"),
        ),
        migrations.AlterField(
            model_name="rock2",
            name="uniaxialCrackMorphology",
            field=models.ImageField(upload_to="images/", verbose_name="单轴裂纹形态"),
        ),
        migrations.AlterField(
            model_name="rock2",
            name="uniaxialFailureMode",
            field=models.ImageField(upload_to="images/", verbose_name="单轴破坏模式"),
        ),
        migrations.AlterField(
            model_name="rock2",
            name="uniaxialStressStrainCurve",
            field=models.ImageField(upload_to="images/", verbose_name="单轴应力应变曲线"),
        ),
        migrations.AlterField(
            model_name="rock3",
            name="key",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="dataBaseApp.rock",
                verbose_name="岩石",
            ),
        ),
        migrations.AlterField(
            model_name="rock3",
            name="poissonsRatio",
            field=models.FloatField(null=True, verbose_name="泊松比"),
        ),
        migrations.AlterField(
            model_name="rock3",
            name="rockCohesion",
            field=models.FloatField(null=True, verbose_name="岩石内聚力"),
        ),
        migrations.AlterField(
            model_name="rock3",
            name="rockInternalFrictionAngle",
            field=models.FloatField(null=True, verbose_name="岩石内摩擦角"),
        ),
        migrations.AlterField(
            model_name="rock3",
            name="triaxialCompressiveStrength",
            field=models.FloatField(null=True, verbose_name="三轴抗压强度"),
        ),
        migrations.AlterField(
            model_name="rock3",
            name="triaxialFailureMode",
            field=models.ImageField(upload_to="images/", verbose_name="三轴破坏模式"),
        ),
        migrations.AlterField(
            model_name="rock3",
            name="triaxialMohrStrength",
            field=models.ImageField(upload_to="images/", verbose_name="三轴莫尔强度"),
        ),
        migrations.AlterField(
            model_name="rock3",
            name="triaxialStressStrainCurve",
            field=models.ImageField(upload_to="images/", verbose_name="三轴应力应变曲线"),
        ),
        migrations.AlterField(
            model_name="rock3",
            name="youngModulus",
            field=models.FloatField(null=True, verbose_name="杨氏模量"),
        ),
        migrations.AlterField(
            model_name="rock4",
            name="key",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="dataBaseApp.rock",
                verbose_name="岩石",
            ),
        ),
        migrations.AlterField(
            model_name="rock4",
            name="tensileAxialLoad",
            field=models.ImageField(upload_to="images/", verbose_name="抗拉轴向载荷"),
        ),
        migrations.AlterField(
            model_name="rock4",
            name="tensileFailureLoad",
            field=models.FloatField(null=True, verbose_name="抗拉破坏荷载"),
        ),
        migrations.AlterField(
            model_name="rock4",
            name="tensileFailureMode",
            field=models.ImageField(upload_to="images/", verbose_name="抗拉破坏模式"),
        ),
        migrations.AlterField(
            model_name="rock4",
            name="tensileStrength",
            field=models.FloatField(null=True, verbose_name="抗拉强度"),
        ),
        migrations.AlterField(
            model_name="rock5",
            name="key",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="dataBaseApp.rock",
                verbose_name="岩石",
            ),
        ),
        migrations.AlterField(
            model_name="rock5",
            name="shearStressShearDirection",
            field=models.ImageField(upload_to="images/", verbose_name="剪切应力剪切方向"),
        ),
        migrations.AlterField(
            model_name="rock5",
            name="shearingStrength",
            field=models.FloatField(null=True, verbose_name="剪切强度"),
        ),
        migrations.AlterField(
            model_name="rock6",
            name="key",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="dataBaseApp.rock",
                verbose_name="岩石",
            ),
        ),
        migrations.AlterField(
            model_name="rock6",
            name="xrdJade",
            field=models.ImageField(upload_to="images/", verbose_name="XRD玉石图谱"),
        ),
        migrations.AlterField(
            model_name="rock6",
            name="xrdMineralContent",
            field=models.CharField(max_length=255, verbose_name="XRD矿物含量"),
        ),
        migrations.AlterField(
            model_name="rock6",
            name="xrdPattern",
            field=models.ImageField(upload_to="images/", verbose_name="XRD衍射图谱"),
        ),
        migrations.AlterField(
            model_name="rock7",
            name="key",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="dataBaseApp.rock",
                verbose_name="岩石",
            ),
        ),
        migrations.AlterField(
            model_name="rock7",
            name="rockDynamicStrength",
            field=models.FloatField(null=True, verbose_name="岩石动态强度"),
        ),
        migrations.AlterField(
            model_name="rock7",
            name="rockProctorsCoefficient",
            field=models.FloatField(null=True, verbose_name="岩石普洛克特系数"),
        ),
        migrations.AlterField(
            model_name="rock7",
            name="rockStaticStrength",
            field=models.FloatField(null=True, verbose_name="岩石静态强度"),
        ),
        migrations.AlterField(
            model_name="rock7",
            name="surfaceArrayPitch",
            field=models.FloatField(null=True, verbose_name="表面阵列间距"),
        ),
        migrations.AlterField(
            model_name="rock7",
            name="surfaceBoreDiameter",
            field=models.FloatField(null=True, verbose_name="表面孔直径"),
        ),
        migrations.AlterField(
            model_name="rock7",
            name="surfaceDistance",
            field=models.FloatField(null=True, verbose_name="表面距离"),
        ),
        migrations.AlterField(
            model_name="rock7",
            name="surfaceExplosiveType",
            field=models.CharField(max_length=255, verbose_name="表面爆破药剂类型"),
        ),
        migrations.AlterField(
            model_name="rock7",
            name="surfaceHoleDepth",
            field=models.FloatField(null=True, verbose_name="表面孔深度"),
        ),
        migrations.AlterField(
            model_name="rock7",
            name="surfaceHoleLayout",
            field=models.CharField(max_length=255, verbose_name="表面孔布置"),
        ),
        migrations.AlterField(
            model_name="rock7",
            name="surfaceSpecificCharge",
            field=models.FloatField(null=True, verbose_name="表面药剂耗量"),
        ),
        migrations.AlterField(
            model_name="rock7",
            name="surfaceSuperDeep",
            field=models.FloatField(null=True, verbose_name="表面超深"),
        ),
        migrations.AlterField(
            model_name="rock8",
            name="excavationBoreholeDiameter",
            field=models.FloatField(null=True, verbose_name="开挖钻孔直径"),
        ),
        migrations.AlterField(
            model_name="rock8",
            name="excavationBoreholeNumber",
            field=models.FloatField(null=True, verbose_name="开挖钻孔数量"),
        ),
        migrations.AlterField(
            model_name="rock8",
            name="excavationCutCharge",
            field=models.FloatField(null=True, verbose_name="开挖切割药量"),
        ),
        migrations.AlterField(
            model_name="rock8",
            name="excavationCutForm",
            field=models.CharField(max_length=255, verbose_name="开挖切割形式"),
        ),
        migrations.AlterField(
            model_name="rock8",
            name="excavationExplosiveType",
            field=models.CharField(max_length=255, verbose_name="开挖爆破药剂类型"),
        ),
        migrations.AlterField(
            model_name="rock8",
            name="excavationHollowholeDiameter",
            field=models.FloatField(null=True, verbose_name="开挖空洞直径"),
        ),
        migrations.AlterField(
            model_name="rock8",
            name="excavationSectionArea",
            field=models.FloatField(null=True, verbose_name="开挖断面面积"),
        ),
        migrations.AlterField(
            model_name="rock8",
            name="excavationSectionShape",
            field=models.CharField(max_length=255, verbose_name="开挖断面形状"),
        ),
        migrations.AlterField(
            model_name="rock8",
            name="excavationSpecificCharge",
            field=models.FloatField(null=True, verbose_name="开挖药剂耗量"),
        ),
        migrations.AlterField(
            model_name="rock8",
            name="key",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="dataBaseApp.rock",
                verbose_name="岩石",
            ),
        ),
        migrations.AlterField(
            model_name="rock9",
            name="key",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="dataBaseApp.rock",
                verbose_name="岩石",
            ),
        ),
        migrations.AlterField(
            model_name="rock9",
            name="stopeArrayPitch",
            field=models.FloatField(null=True, verbose_name="阵列间距"),
        ),
        migrations.AlterField(
            model_name="rock9",
            name="stopeBoreholeDiameter",
            field=models.FloatField(null=True, verbose_name="钻孔直径"),
        ),
        migrations.AlterField(
            model_name="rock9",
            name="stopeCollapseStepDistance",
            field=models.FloatField(null=True, verbose_name="崩落步距"),
        ),
        migrations.AlterField(
            model_name="rock9",
            name="stopeDistance",
            field=models.FloatField(null=True, verbose_name="距离"),
        ),
        migrations.AlterField(
            model_name="rock9",
            name="stopeDriftInterval",
            field=models.FloatField(null=True, verbose_name="巷道间距"),
        ),
        migrations.AlterField(
            model_name="rock9",
            name="stopeEdgeHoleAngle",
            field=models.FloatField(null=True, verbose_name="边缘钻孔角度"),
        ),
        migrations.AlterField(
            model_name="rock9",
            name="stopeExplosiveType",
            field=models.CharField(max_length=255, verbose_name="爆破药剂类型"),
        ),
        migrations.AlterField(
            model_name="rock9",
            name="stopeHoleLayout",
            field=models.CharField(max_length=255, verbose_name="钻孔布置"),
        ),
        migrations.AlterField(
            model_name="rock9",
            name="stopeMethod",
            field=models.CharField(max_length=255, verbose_name="方法"),
        ),
        migrations.AlterField(
            model_name="rock9",
            name="stopeOreCaving",
            field=models.CharField(max_length=255, verbose_name="块状"),
        ),
        migrations.AlterField(
            model_name="rock9",
            name="stopeSpecificCharge",
            field=models.FloatField(null=True, verbose_name="药剂耗量"),
        ),
        migrations.AlterField(
            model_name="rock9",
            name="stopeSublevelHeight",
            field=models.FloatField(null=True, verbose_name="子级高度"),
        ),
    ]
