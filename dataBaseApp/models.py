from django.db import models
from django.db.models import CharField

# 岩石
ROCK_TYPE_CHOICES = [
    ('沉积岩', '沉积岩'),
    ('岩浆岩', '岩浆岩'),
    ('变质岩', '变质岩'),
]
# # 岩石物性库
# 'RockPropertiesDatabase': 'rock_properties.html',
# 'RockPropertiesDatabaseSearch': 'rock_properties_search.html',

class Rock(models.Model):
    rock_id = models.CharField(primary_key=True, max_length=255, verbose_name='岩石ID')
    rock_name = models.CharField(max_length=255, verbose_name='岩石名称')
    class Meta:
        app_label = 'dataBaseApp'
        verbose_name = '岩石'
        verbose_name_plural = '岩石'

class Rock1(models.Model):
    key = models.ForeignKey(Rock, on_delete=models.CASCADE, primary_key=True, verbose_name='岩石')
    rockType = models.CharField(max_length=255, choices=ROCK_TYPE_CHOICES, verbose_name='岩石类型')
    rockDensity = models.CharField(blank=True,null=True, max_length=255, verbose_name='密度')
    rockPorosity = models.CharField(blank=True,null=True, max_length=255, verbose_name='孔隙度')
    rockWaterAbsorption = models.CharField(blank=True,null=True, max_length=255, verbose_name='吸水率')
    rockPermeabilityCoefficient = models.CharField(blank=True,null=True, max_length=255, verbose_name='渗透系数')
    rockLongitudinalWaveVelocity = models.CharField(blank=True,null=True, max_length=255, verbose_name='纵波速度')
    rockTransverseWaveVelocity = models.CharField(blank=True,null=True, max_length=255, verbose_name='横波速度')
    rockWaveImpedance = models.CharField(blank=True,null=True, max_length=255, verbose_name='波阻抗')
    rockOrigin = models.CharField(blank=True,null=True, max_length=255, verbose_name='岩石产地')

    class Meta:
        app_label = 'dataBaseApp'
        verbose_name = '岩石物性库'
        verbose_name_plural = '岩石物性库'

class Rock2(models.Model):
    key = models.ForeignKey(Rock, on_delete=models.CASCADE, primary_key=True, verbose_name='岩石')
    uniaxialCompressiveStrength = models.CharField(blank=True,null=True, verbose_name='单轴抗压强度', max_length=255,)
    elasticModulus = models.CharField(blank=True,null=True, verbose_name='弹性模量', max_length=255,)
    poissonsRatio = models.CharField(blank=True,null=True, verbose_name='泊松比', max_length=255,)
    uniaxialFailureMode = models.ImageField(blank=True,null=True, upload_to='images/', verbose_name='单轴破坏模式（图）', default='path/to/default_image.jpg')
    uniaxialStressStrainCurve = models.ImageField(blank=True,null=True, upload_to='images/', verbose_name='单轴应力-应变曲线（图）', default='path/to/default_image.jpg')
    uniaxialCrackMorphology = models.ImageField(blank=True,null=True, upload_to='images/', verbose_name='单轴裂纹形态（图）', default='path/to/default_image.jpg')

    class Meta:
        app_label = 'dataBaseApp'
        verbose_name = '力学实验库的单轴压缩实验'
        verbose_name_plural = '力学实验库的单轴压缩实验'

# 继续补全其他模型类的 verbose_name 中文信息...

# # 力学实验库的三轴压缩实验
# 'TriaxialCompressionExperimentInMechanicsLab': 'triaxial_compression_experiment.html',
class Rock3(models.Model):
    key = models.ForeignKey(Rock, on_delete=models.CASCADE, primary_key=True, verbose_name='岩石')
    triaxialCompressiveStrength = models.CharField(blank=True,null=True, max_length=255, verbose_name='三轴抗压强度')
    rockCohesion = models.CharField(blank=True,null=True,max_length=255,  verbose_name='内聚力')
    rockInternalFrictionAngle = models.CharField(blank=True,null=True,max_length=255,  verbose_name='内摩擦角')
    youngModulus = models.CharField(blank=True,null=True, max_length=255, verbose_name='杨氏模量')
    poissonsRatio = models.CharField(blank=True,null=True, max_length=255, verbose_name='泊松比')
    triaxialFailureMode = models.ImageField(blank=True,null=True, upload_to='images/', verbose_name='三轴破坏模式（图）', default='path/to/default_image.jpg')
    triaxialStressStrainCurve = models.ImageField(blank=True,null=True, upload_to='images/', verbose_name='三轴应力-应变曲线（图）', default='path/to/default_image.jpg')
    triaxialMohrStrength = models.ImageField(blank=True,null=True, upload_to='images/', verbose_name='三轴莫尔强度包络图（图）', default='path/to/default_image.jpg')

    class Meta:
        app_label = 'dataBaseApp'
        verbose_name = '力学实验库的三轴压缩实验'
        verbose_name_plural = '力学实验库的三轴压缩实验'


class Rock4(models.Model):
    key = models.ForeignKey(Rock, on_delete=models.CASCADE, primary_key=True, verbose_name='岩石')
    tensileStrength = models.CharField(blank=True,null=True, max_length=255, verbose_name='抗拉强度')
    tensileFailureLoad = models.CharField(blank=True,null=True, max_length=255, verbose_name='破坏荷载')
    tensileFailureMode = models.ImageField(blank=True,null=True, upload_to='images/', verbose_name='抗拉强度破坏模式（图）', default='path/to/default_image.jpg')
    tensileAxialLoad = models.ImageField(blank=True,null=True, upload_to='images/', verbose_name='抗拉强度轴向-荷载位移图（图）', default='path/to/default_image.jpg')

    class Meta:
        app_label = 'dataBaseApp'
        verbose_name = '力学实验库的抗拉强度实验'
        verbose_name_plural = '力学实验库的抗拉强度实验'

# # 力学实验库的直接剪切实验
# 'DirectShearExperimentInMechanicsLab': 'direct_shear_experiment.html',
class Rock5(models.Model):
    key = models.ForeignKey(Rock, on_delete=models.CASCADE, primary_key=True, verbose_name='岩石')
    shearingStrength = models.CharField(blank=True,null=True, max_length=255, verbose_name='抗剪强度')
    shearStressShearDirection = models.ImageField(blank=True,null=True, upload_to='images/', verbose_name='剪切应力-剪切方向位移（图）', default='path/to/default_image.jpg')

    class Meta:
        app_label = 'dataBaseApp'
        verbose_name = '力学实验库的直接剪切实验'
        verbose_name_plural = '力学实验库的直接剪切实验'


class Rock6(models.Model):
    key = models.ForeignKey(Rock, on_delete=models.CASCADE, primary_key=True, verbose_name='岩石')
    xrdMineralContent = models.CharField(blank=True,null=True, max_length=255, verbose_name='主要矿物含量')
    xrdPattern = models.ImageField(blank=True,null=True, upload_to='images/', verbose_name='XRD衍射图谱', default='path/to/default_image.jpg')
    xrdJade = models.ImageField(blank=True,null=True, upload_to='images/', verbose_name='Jade定量分析', default='path/to/default_image.jpg')

    class Meta:
        app_label = 'dataBaseApp'
        verbose_name = '力学实验库的XRD衍射实验'
        verbose_name_plural = '力学实验库的XRD衍射实验'


class Rock7(models.Model):
    key = models.ForeignKey(Rock, on_delete=models.CASCADE, primary_key=True, verbose_name='岩石')
    rockStaticStrength = models.CharField(blank=True,null=True, max_length=255, verbose_name='岩石静态强度')
    rockProctorsCoefficient = models.CharField(blank=True,null=True, max_length=255, verbose_name='普氏系数')
    rockDynamicStrength = models.CharField(blank=True,null=True, max_length=255, verbose_name='岩石动态强度')
    surfaceHoleLayout = models.CharField(blank=True,null=True, max_length=255, verbose_name='露天炮孔布置')
    surfaceBoreDiameter = models.CharField(blank=True,null=True,max_length=255,  verbose_name='露天孔径')
    surfaceHoleDepth = models.CharField(blank=True,null=True, max_length=255, verbose_name='露天孔深')
    surfaceDistance = models.CharField(blank=True,null=True, max_length=255, verbose_name='露天孔距')
    surfaceArrayPitch = models.CharField(blank=True,null=True,max_length=255,  verbose_name='露天排距/抵抗线')
    surfaceSuperDeep = models.CharField(blank=True,null=True, max_length=255, verbose_name='露天超深')
    surfaceExplosiveType = models.CharField(blank=True,null=True, max_length=255, verbose_name='露天炸药类型')
    surfaceSpecificCharge = models.CharField(blank=True,null=True, max_length=255, verbose_name='露天炸药单耗')

    class Meta:
        app_label = 'dataBaseApp'
        verbose_name = '工程数据库中的露天爆破'
        verbose_name_plural = '工程数据库中的露天爆破'


# # 工程数据库中的掘进爆破
# 'TunnelingBlastingInEngineeringDatabase': 'tunneling_blasting.html',
class Rock8(models.Model):
    key = models.ForeignKey(Rock, on_delete=models.CASCADE, primary_key=True, verbose_name='岩石')
    excavationSectionShape = models.CharField(blank=True,null=True, max_length=255, verbose_name='断面形状')
    excavationSectionArea = models.CharField(blank=True,null=True,max_length=255,  verbose_name='断面面积')
    excavationCutForm = models.CharField(blank=True,null=True, max_length=255, verbose_name='掏槽形式')
    excavationHollowholeDiameter = models.CharField(blank=True,null=True, max_length=255, verbose_name='空孔直径')
    excavationBoreholeDiameter = models.CharField(blank=True,null=True, max_length=255, verbose_name='炮孔直径')
    excavationBoreholeNumber = models.CharField(blank=True,null=True, max_length=255, verbose_name='炮孔数量')
    excavationCutCharge = models.CharField(blank=True,null=True, max_length=255, verbose_name='掏槽单耗')
    excavationExplosiveType = models.CharField(blank=True,null=True, max_length=255, verbose_name='炸药类型')
    excavationSpecificCharge = models.CharField(blank=True,null=True, max_length=255, verbose_name='炸药单耗')

    class Meta:
        app_label = 'dataBaseApp'
        verbose_name = '工程数据库中的掘进爆破'
        verbose_name_plural = '工程数据库中的掘进爆破'


class Rock9(models.Model):
    key = models.ForeignKey(Rock, on_delete=models.CASCADE, primary_key=True, verbose_name='岩石')
    stopeMethod = models.CharField(blank=True,null=True, max_length=255, verbose_name='采矿方法')
    stopeOreCaving = models.CharField(blank=True,null=True, max_length=255, verbose_name='落矿方式')
    stopeHoleLayout = models.CharField(blank=True,null=True, max_length=255, verbose_name='炮孔布置形式')
    stopeBoreholeDiameter = models.CharField(blank=True,null=True, max_length=255, verbose_name='炮孔直径')
    stopeDistance = models.CharField(blank=True,null=True, max_length=255, verbose_name='孔距/孔底距')
    stopeArrayPitch = models.CharField(blank=True,null=True, max_length=255, verbose_name='排距/最小抵抗线')
    stopeExplosiveType = models.CharField(max_length=255, verbose_name='炸药类型')
    stopeSpecificCharge = models.CharField(blank=True,null=True, max_length=255, verbose_name='回采炸药单耗')
    stopeSublevelHeight = models.CharField(blank=True,null=True, max_length=255, verbose_name='分段高度')
    stopeDriftInterval = models.CharField(blank=True,null=True,max_length=255,  verbose_name='进路间距')
    stopeCollapseStepDistance = models.CharField(blank=True,null=True, max_length=255, verbose_name='崩矿步距')
    stopeEdgeHoleAngle = models.CharField(blank=True,null=True, max_length=255, verbose_name='边孔角')

    class Meta:
        app_label = 'dataBaseApp'
        verbose_name = '工程数据库中的回采爆破'
        verbose_name_plural = '工程数据库中的回采爆破'
