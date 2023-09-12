import os
import uuid

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from dataBaseApp.models import *
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage, default_storage
from django.contrib import messages
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage

def get_default_image():
    # 读取默认图片文件
    with default_storage.open('path/to/default_image.jpg', 'rb') as file:
        file_content = file.read()

    # 创建InMemoryUploadedFile对象
    default_image = InMemoryUploadedFile(
        file=ContentFile(file_content),
        field_name=None,
        name='default_image.jpg',
        content_type='image/jpeg',
        size=len(file_content),
        charset=None
    )

    return default_image

default_image = get_default_image()


# Create your views here.

def login_view(request):
    return render(request, 'login.html')


def register_view(request):
    return render(request, 'register.html')


pageName = {'homePage': 'rock_properties.html',

            # 岩石物性库
            'RockPropertiesDatabase': 'rock_properties.html',
            'RockPropertiesDatabaseSearch': 'rock_properties_search.html',

            # 力学实验库的单轴压缩实验
            'UniaxialCompressionExperimentInMechanicsLabPage': 'uniaxial_compression_experiment.html',
            # 力学实验库的三轴压缩实验
            'TriaxialCompressionExperimentInMechanicsLab': 'triaxial_compression_experiment.html',
            # 力学实验库的抗拉强度实验
            'TensileStrengthExperimentInMechanicsLab': 'tensile_strength_experiment.html',
            # 力学实验库的直接剪切实验
            'DirectShearExperimentInMechanicsLab': 'direct_shear_experiment.html',
            # 力学实验库的XRD衍射实验
            'XRDDiffractionExperimentInMechanicsLab': 'xrd_diffraction_experiment.html',

            # 工程数据库中的露天爆破
            'OpenPitBlastingInEngineeringDatabase': 'open_pit_blasting.html',
            # 工程数据库中的掘进爆破
            'TunnelingBlastingInEngineeringDatabase': 'tunneling_blasting.html',
            # 工程数据库中的回采爆破
            'RetreatBlastingInEngineeringDatabase': 'retreat_blasting.html',

            # 大数据计算平台
            'Theoretical_Calculation': 'theoretical_Calculation.html',

            # 大数据分析
            'Big_Date': 'none.html',

            # 矿山信息
            'Mine_Date': 'none.html',
            }


def page_view(request):
    try:
        if (request.GET.get('param1')):
            param1 = request.GET.get('param1')
        else:
            param1 = 'homePage'
    except:
        param1 = 'homePage'
    try:
        if (request.GET.get('param2')):
            param2 = request.GET.get('param2')
        else:
            param2 = '1'
    except:
        param2 = '1'

    if param2 == "2-1":
        # 单轴压缩实验
        rockDatas = Rock2.objects.all()
    elif param2 == "2-2":
        # 三轴压缩实验
        rockDatas = Rock3.objects.all()
    elif param2 == "2-3":
        # 抗拉强度实验
        rockDatas = Rock4.objects.all()
    elif param2 == "2-4":
        # 直接剪切实验
        rockDatas = Rock5.objects.all()
    elif param2 == "2-5":
        # XRD衍射实验
        rockDatas = Rock6.objects.all()
    elif param2 == "3-1":
        # 露天爆破
        rockDatas = Rock7.objects.all()
    elif param2 == "3-2":
        # 掘进爆破
        rockDatas = Rock8.objects.all()
    elif param2 == "3-3":
        # 回采爆破
        rockDatas = Rock9.objects.all()
    elif param2 == "4-1":
        # 理论计算
        rockDatas = Rock1.objects.all()
    elif param2 == "4-2":
        # 大数据分析
        rockDatas = Rock1.objects.all()
    elif param2 == "5":
        # 矿山信息库
        rockDatas = Rock1.objects.all()
    else:
        # 岩石物性库
        rockDatas = Rock1.objects.all()

    pagePath = pageName[param1]
    # rocks = Rock
    return render(request, pagePath, {'rocks': rockDatas})


def addRock(request):
    unique_filename = f'{uuid.uuid4()}'
    if request.method == 'POST':
        rockData = request.GET.get('rockData')
        print(rockData)
        # Retrieve the form data
        rock_id = request.POST.get('rock_id')
        rock_type = request.POST.get('rock_type')
        rock_name = request.POST.get('rock_name')

        # ------- 岩石物性库
        rock_density = request.POST.get('rock_density')
        rockPorosity = request.POST.get('rockPorosity')
        rockWaterAbsorption = request.POST.get('rockWaterAbsorption')
        rockPermeabilityCoefficient = request.POST.get('rockPermeabilityCoefficient')
        rockLongitudinalWaveVelocity = request.POST.get('rockLongitudinalWaveVelocity')
        rockTransverseWaveVelocity = request.POST.get('rockTransverseWaveVelocity')
        rockWaveImpedance = request.POST.get('rockWaveImpedance')
        rockOrigin = request.POST.get('rockOrigin')

        '''static_strength = request.POST.get('static_strength')
        dynamic_strength = request.POST.get('dynamic_strength')
        rock_density = request.POST.get('rock_density')
        longitudinal_velocity = request.POST.get('longitudinal_velocity')
        poisson_ratio = request.POST.get('poisson_ratio')
        puissone_ratio = request.POST.get('puissone_ratio')
        explosive_consumption = request.POST.get('explosive_consumption')'''

        # ------- 力学实验库的单轴压缩实验
        uniaxialCompressiveStrength = request.POST.get('uniaxialCompressiveStrength')
        elasticModulus = request.POST.get('elasticModulus')
        poissonsRatio = request.POST.get('poissonsRatio')
        # 图片
        uniaxialFailureMode = request.FILES.get('uniaxialFailureMode')
        if uniaxialFailureMode is None:
            uniaxialFailureMode = default_image
        # 图片
        uniaxialStressStrainCurve = request.FILES.get('uniaxialStressStrainCurve')
        if uniaxialStressStrainCurve is None:
            uniaxialStressStrainCurve = default_image
        # 图片
        uniaxialCrackMorphology = request.FILES.get('uniaxialCrackMorphology')
        if uniaxialCrackMorphology is None:
            uniaxialCrackMorphology = default_image
        
        # ------- 力学实验库的三轴压缩实验
        triaxialCompressiveStrength = request.POST.get('triaxialCompressiveStrength')
        rockCohesion = request.POST.get('rockCohesion')
        rockInternalFrictionAngle = request.POST.get('rockInternalFrictionAngle')
        youngModulus = request.POST.get('youngModulus')
        poissonsRatio = request.POST.get('poissonsRatio')
        # 图片
        triaxialFailureMode = request.FILES.get('triaxialFailureMode')
        if triaxialFailureMode is None:
            triaxialFailureMode = default_image
        # 图片
        triaxialStressStrainCurve = request.FILES.get('triaxialStressStrainCurve')
        if triaxialStressStrainCurve is None:
            triaxialStressStrainCurve = default_image
        # 图片
        triaxialMohrStrength = request.FILES.get('triaxialMohrStrength')
        if triaxialMohrStrength is None:
            triaxialMohrStrength = default_image
        
        # ------ 力学实验库的抗拉强度实验
        tensileStrength = request.POST.get('tensileStrength')
        tensileFailureLoad = request.POST.get('tensileFailureLoad')
        # 图片
        tensileFailureMode = request.FILES.get('tensileFailureMode')
        if tensileFailureMode is None:
            tensileFailureMode = default_image
        # 图片
        tensileAxialLoad = request.FILES.get('tensileAxialLoad')
        if tensileAxialLoad is None:
            tensileAxialLoad = default_image
        
        # ------ 力学实验库的直接剪切实验
        shearingStrength = request.POST.get('shearingStrength')
        # 图片
        shearStressShearDirection = request.FILES.get('shearStressShearDirection')
        if shearStressShearDirection is None:
            shearStressShearDirection = default_image
        
        # ------ 力学实验库的XRD衍射实验
        xrdMineralContent = request.POST.get('xrdMineralContent')
        # 图片
        xrdPattern = request.FILES.get('xrdPattern')
        if xrdPattern is None:
            xrdPattern = default_image
        # 图片
        xrdJade = request.FILES.get('xrdJade')
        if xrdJade is None:
            xrdJade = default_image
        
        # ------ 工程数据库中的露天爆破
        rockStaticStrength = request.POST.get('rockStaticStrength')
        rockProctorsCoefficient = request.POST.get('rockProctorsCoefficient')
        rockDynamicStrength = request.POST.get('rockDynamicStrength')
        surfaceHoleLayout = request.POST.get('surfaceHoleLayout')
        surfaceBoreDiameter = request.POST.get('surfaceBoreDiameter')
        surfaceHoleDepth = request.POST.get('surfaceHoleDepth')
        surfaceDistance = request.POST.get('surfaceDistance')
        surfaceArrayPitch = request.POST.get('surfaceArrayPitch')
        surfaceSuperDeep = request.POST.get('surfaceSuperDeep')
        surfaceExplosiveType = request.POST.get('surfaceExplosiveType')
        surfaceSpecificCharge = request.POST.get('surfaceSpecificCharge')

        # ------ 工程数据库中的掘进爆破
        excavationSectionShape = request.POST.get('excavationSectionShape')
        excavationSectionArea = request.POST.get('excavationSectionArea')
        excavationCutForm = request.POST.get('excavationCutForm')
        excavationHollowholeDiameter = request.POST.get('excavationHollowholeDiameter')
        excavationBoreholeDiameter = request.POST.get('excavationBoreholeDiameter')
        excavationBoreholeNumber = request.POST.get('excavationBoreholeNumber')
        excavationCutCharge = request.POST.get('excavationCutCharge')
        excavationExplosiveType = request.POST.get('excavationExplosiveType')
        excavationSpecificCharge = request.POST.get('excavationSpecificCharge')

        # ------ 工程数据库中的回采爆破
        stopeMethod = request.POST.get('stopeMethod')
        stopeOreCaving = request.POST.get('stopeOreCaving')
        stopeHoleLayout = request.POST.get('stopeHoleLayout')
        stopeBoreholeDiameter = request.POST.get('stopeBoreholeDiameter')
        stopeDistance = request.POST.get('stopeDistance')
        stopeArrayPitch = request.POST.get('stopeArrayPitch')
        stopeExplosiveType = request.POST.get('stopeExplosiveType')
        stopeSpecificCharge = request.POST.get('stopeSpecificCharge')
        stopeSublevelHeight = request.POST.get('stopeSublevelHeight')
        stopeDriftInterval = request.POST.get('stopeDriftInterval')
        stopeCollapseStepDistance = request.POST.get('stopeCollapseStepDistance')
        stopeEdgeHoleAngle = request.POST.get('stopeEdgeHoleAngle')

        # Create a new Rock object
        rock = Rock(rock_id=rock_id, rock_name=rock_name)
        try:
            rock.save()
        except:
            pass

        match rockData:
            case '1':
                # Create a new Rock1 object and associate it with the Rock object
                rock1 = Rock1(key=rock,
                              rockType=rock_type,
                              rockDensity=rock_density,
                              rockPorosity=rockPorosity,
                              rockWaterAbsorption=rockWaterAbsorption,
                              rockPermeabilityCoefficient=rockPermeabilityCoefficient,
                              rockLongitudinalWaveVelocity=rockLongitudinalWaveVelocity,
                              rockTransverseWaveVelocity=rockTransverseWaveVelocity,
                              rockWaveImpedance=rockWaveImpedance,
                              rockOrigin=rockOrigin, )
                rock1.save()
                rockDatas = Rock1.objects.all()
                # Redirect to a success page or perform any additional operations
                return render(request, pageName['RockPropertiesDatabaseSearch'], {'rocks': rockDatas})
            case '2-1':
                file_path = os.path.join('path', 'to', 'uniaxial', unique_filename)
                print('cslog_uniaxialFailureMode:',type(uniaxialFailureMode))
                uniaxialFailureModePath = default_storage.save(file_path+'1', uniaxialFailureMode)
                uniaxialStressStrainCurvePath = default_storage.save(file_path+'2', uniaxialStressStrainCurve)
                uniaxialCrackMorphologyPath = default_storage.save(file_path+'3', uniaxialCrackMorphology)
                rock2 = Rock2(key=rock,
                              uniaxialCompressiveStrength=uniaxialCompressiveStrength,
                              elasticModulus=elasticModulus,
                              poissonsRatio=poissonsRatio,
                              uniaxialFailureMode=uniaxialFailureModePath,
                              uniaxialStressStrainCurve=uniaxialStressStrainCurvePath,
                              uniaxialCrackMorphology=uniaxialCrackMorphologyPath, )
                rock2.save()
                rockDatas = Rock2.objects.all()
                # Redirect to a success page or perform any additional operations
                return render(request, pageName['UniaxialCompressionExperimentInMechanicsLabPage'],
                              {'rocks': rockDatas})
            case '2-2':
                file_path = os.path.join('path', 'to', 'triaxial', unique_filename)
                triaxialFailureModePath = default_storage.save(file_path+'1', triaxialFailureMode)
                triaxialStressStrainCurvePath = default_storage.save(file_path+'2', triaxialStressStrainCurve)
                triaxialMohrStrengthPath = default_storage.save(file_path+'3', triaxialMohrStrength)
                rock3 = Rock3(key=rock,
                              triaxialCompressiveStrength=triaxialCompressiveStrength,
                              rockCohesion=rockCohesion,
                              rockInternalFrictionAngle=rockInternalFrictionAngle,
                              youngModulus=youngModulus,
                              poissonsRatio=poissonsRatio,
                              triaxialFailureMode=triaxialFailureModePath,
                              triaxialStressStrainCurve=triaxialStressStrainCurvePath,
                              triaxialMohrStrength=triaxialMohrStrengthPath, )
                rock3.save()
                rockDatas = Rock3.objects.all()
                # Redirect to a success page or perform any additional operations
                return render(request, pageName['TriaxialCompressionExperimentInMechanicsLab'], {'rocks': rockDatas})
            case '2-3':
                file_path = os.path.join('path', 'to', 'tensile', unique_filename)
                tensileFailureModePath = default_storage.save(file_path+'1', tensileFailureMode)
                tensileAxialLoadPath = default_storage.save(file_path+'2', tensileAxialLoad)

                rock4 = Rock4(key=rock,
                              tensileStrength=tensileStrength,
                              tensileFailureLoad=tensileFailureLoad,
                              tensileFailureMode=tensileFailureModePath,
                              tensileAxialLoad=tensileAxialLoadPath,
                              )
                rock4.save()
                rockDatas = Rock4.objects.all()
                # Redirect to a success page or perform any additional operations
                return render(request, pageName['TensileStrengthExperimentInMechanicsLab'], {'rocks': rockDatas})
            case '2-4':
                file_path = os.path.join('path', 'to', 'shearStressShearDirectionPath', unique_filename)
                shearStressShearDirectionPath = default_storage.save(file_path+'1', shearStressShearDirection)
                rock5 = Rock5(key=rock,
                              shearingStrength=shearingStrength,
                              shearStressShearDirection=shearStressShearDirectionPath, )
                rock5.save()
                rockDatas = Rock5.objects.all()
                # Redirect to a success page or perform any additional operations
                return render(request, pageName['DirectShearExperimentInMechanicsLab'], {'rocks': rockDatas})
            case '2-5':
                file_path = os.path.join('path', 'to', ' xrd', unique_filename)
                xrdPatternPath = default_storage.save(file_path+'1', xrdPattern)
                xrdJadePath = default_storage.save(file_path+'2', xrdJade)
                rock6 = Rock6(key=rock,
                              xrdMineralContent=xrdMineralContent,
                              xrdPattern=xrdPatternPath,
                              xrdJade=xrdJadePath, )
                rock6.save()
                rockDatas = Rock6.objects.all()
                # Redirect to a success page or perform any additional operations
                return render(request, pageName['XRDDiffractionExperimentInMechanicsLab'], {'rocks': rockDatas})
            case '3-1':
                rock7 = Rock7(key=rock,
                              rockStaticStrength=rockStaticStrength,
                              rockProctorsCoefficient=rockProctorsCoefficient,
                              rockDynamicStrength=rockDynamicStrength,
                              surfaceHoleLayout=surfaceHoleLayout,
                              surfaceBoreDiameter=surfaceBoreDiameter,
                              surfaceHoleDepth=surfaceHoleDepth,
                              surfaceDistance=surfaceDistance,
                              surfaceArrayPitch=surfaceArrayPitch,
                              surfaceSuperDeep=surfaceSuperDeep,
                              surfaceExplosiveType=surfaceExplosiveType,
                              surfaceSpecificCharge=surfaceSpecificCharge, )
                rock7.save()
                rockDatas = Rock7.objects.all()
                # Redirect to a success page or perform any additional operations
                return render(request, pageName['OpenPitBlastingInEngineeringDatabase'], {'rocks': rockDatas})
            case '3-2':
                rock8 = Rock8(key=rock,
                              excavationSectionShape=excavationSectionShape,
                              excavationSectionArea=excavationSectionArea,
                              excavationCutForm=excavationCutForm,
                              excavationHollowholeDiameter=excavationHollowholeDiameter,
                              excavationBoreholeDiameter=excavationBoreholeDiameter,
                              excavationBoreholeNumber=excavationBoreholeNumber,
                              excavationCutCharge=excavationCutCharge,
                              excavationExplosiveType=excavationExplosiveType,
                              excavationSpecificCharge=excavationSpecificCharge,
                              )
                rock8.save()
                rockDatas = Rock8.objects.all()
                # Redirect to a success page or perform any additional operations
                return render(request, pageName['TunnelingBlastingInEngineeringDatabase'], {'rocks': rockDatas})
            case '3-3':
                rock9 = Rock9(key=rock,
                              stopeMethod=stopeMethod,
                              stopeOreCaving=stopeOreCaving,
                              stopeHoleLayout=stopeHoleLayout,
                              stopeBoreholeDiameter=stopeBoreholeDiameter,
                              stopeDistance=stopeDistance,
                              stopeArrayPitch=stopeArrayPitch,
                              stopeExplosiveType=stopeExplosiveType,
                              stopeSpecificCharge=stopeSpecificCharge,
                              stopeSublevelHeight=stopeSublevelHeight,
                              stopeDriftInterval=stopeDriftInterval,
                              stopeCollapseStepDistance=stopeCollapseStepDistance,
                              stopeEdgeHoleAngle=stopeEdgeHoleAngle,
                              )
                rock9.save()
                rockDatas = Rock9.objects.all()
                # Redirect to a success page or perform any additional operations
                return render(request, pageName['RetreatBlastingInEngineeringDatabase'], {'rocks': rockDatas})
            case _:
                return page_view(request)
    else:
        # Handle GET request
        return page_view(request)


@csrf_exempt
def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:

            login(request, user)
            # 执行登录成功后的操作，如重定向到首页或其他页面
            return page_view(request)
        else:
            # 用户名或密码验证失败
            messages.error(request, '登录验证失败，请重新登录。')
            return render(request, 'login.html', {'messages': messages.get_messages(request)})
    else:
        return render(request, 'login.html')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        # 处理注册表单提交
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        confirm_password = request.POST['confirm_password']

        # 检查密码是否匹配
        if password != confirm_password:
            # 密码不匹配，返回注册页面并显示错误消息
            return render(request, 'register.html', {'error': '密码不匹配'})

        # 创建用户
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
        except:
            return render(request, 'register.html', {'error': '账户已经注册'})

        # 注册成功后重定向到主页
        return redirect('login')

    # GET 请求，显示注册页面
    return render(request, 'register.html')

def delete_record(request):
    rock_id = request.GET['rock_id']
    rockType = request.GET.get('rockType')
    print('rockType:' + str(rockType))
    if rockType == "1":
        # 岩石物性库
        record = Rock1.objects.filter(key_id=rock_id).first()
        record.delete()
        page = 'homePage'
        rockDatas = Rock1.objects.all()
    elif rockType == "1-1":
        # 岩石物性库
        record = Rock1.objects.filter(key_id=rock_id).first()
        record.delete()
        page = 'RockPropertiesDatabaseSearch'
        rockDatas = Rock1.objects.all()
    elif rockType == "2-1":
        # 力学实验库的单轴压缩实验
        record = Rock2.objects.filter(key_id=rock_id).first()
        record.delete()
        page = 'UniaxialCompressionExperimentInMechanicsLabPage'
        rockDatas = Rock2.objects.all()
    elif rockType == "2-2":
        # 力学实验库的三轴压缩实验
        record = Rock3.objects.filter(key_id=rock_id).first()
        record.delete()
        page = 'TriaxialCompressionExperimentInMechanicsLab'
        rockDatas = Rock3.objects.all()
    elif rockType == "2-3":
        # 力学实验库的抗拉强度实验
        record = Rock4.objects.filter(key_id=rock_id).first()
        record.delete()
        page = 'TensileStrengthExperimentInMechanicsLab'
        rockDatas = Rock4.objects.all()
    elif rockType == "2-4":
        # 力学实验库的直接剪切实验
        record = Rock5.objects.filter(key_id=rock_id).first()
        record.delete()
        page = 'DirectShearExperimentInMechanicsLab'
        rockDatas = Rock5.objects.all()
    elif rockType == "2-5":
        # 力学实验库的XRD衍射实验
        record = Rock6.objects.filter(key_id=rock_id).first()
        record.delete()
        page = 'XRDDiffractionExperimentInMechanicsLab'
        rockDatas = Rock6.objects.all()
    elif rockType == "3-1":
        # 工程数据库中的露天爆破
        record = Rock7.objects.filter(key_id=rock_id).first()
        record.delete()
        page = 'OpenPitBlastingInEngineeringDatabase'
        rockDatas = Rock7.objects.all()
    elif rockType == "3-2":
        # 工程数据库中的掘进爆破
        record = Rock8.objects.filter(key_id=rock_id).first()
        record.delete()
        page = 'TunnelingBlastingInEngineeringDatabase'
        rockDatas = Rock8.objects.all()
    elif rockType == "3-3":
        # 工程数据库中的回采爆破
        record = Rock9.objects.filter(key_id=rock_id).first()
        record.delete()
        page = 'RetreatBlastingInEngineeringDatabase'
        rockDatas = Rock9.objects.all()
    else:
        page = 'RockPropertiesDatabase'
        rockDatas = Rock1.objects.all()

    return render(request, pageName[page], {'rocks': rockDatas})


def delete_singer(request):
    rock_id = request.GET['rock_id']
    record = Rock2.objects.filter(key_id=rock_id).first()
    record.delete()
    rockDatas = Rock2.objects.all()
    return render(request, pageName['UniaxialCompressionExperimentInMechanicsLabPage'], {'rocks': rockDatas})