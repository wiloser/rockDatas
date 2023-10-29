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
from django.http import HttpResponse
from scipy.optimize import curve_fit
import numpy as np

def fit_func(w, k, a):
    Q, R = w
    return k * np.power(Q**(1/3) / R, a)


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

            # 尖山地下矿
            'JianShanUndergroundMine': 'jianshan_underground_mine.html',
            # 露天采矿
            'OpenPit': 'open_pit.html',
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

        if(rockData == '1'):
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
        elif(rockData == '2-1'):
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
        elif(rockData == '2-2'):
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
        elif(rockData == '2-3'):
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
        elif(rockData == '2-4'):
            file_path = os.path.join('path', 'to', 'shearStressShearDirectionPath', unique_filename)
            shearStressShearDirectionPath = default_storage.save(file_path+'1', shearStressShearDirection)
            rock5 = Rock5(key=rock,
                          shearingStrength=shearingStrength,
                          shearStressShearDirection=shearStressShearDirectionPath, )
            rock5.save()
            rockDatas = Rock5.objects.all()
            # Redirect to a success page or perform any additional operations
            return render(request, pageName['DirectShearExperimentInMechanicsLab'], {'rocks': rockDatas})
        elif(rockData == '2-5'):
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
        elif(rockData == '3-1'):
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
        elif(rockData == '3-2'):
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
        elif(rockData == '3-3'):
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
        else:
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


def schema(request):
    if request.method == 'POST':
        type = request.GET['type']
        if(type == "1-1"):
            year = request.POST['year']
            month = request.POST['month']
            day = request.POST['day']
            area = request.POST['area']
            plat = request.POST['plat']
            well = request.POST['well']
            pdf_file = request.FILES.get('pdf', '')
            if not year or not month or not day or not area or not plat or not well or not pdf_file:
                pass
            else:
                name = year + ',' + month + ',' + day + ',' + area + ',' + plat + ',' + well
                schema = Schema(schema_name=name, pdf_file=pdf_file)
                try:
                    schema.save()
                    # return render(request, pageName['OpenPit'])
                except:
                    pass
        elif(type == "3-1"):
            year = request.POST['year']
            month = request.POST['month']
            day = request.POST['day']
            area = request.POST['area']
            plat = request.POST['plat']
            well = request.POST['well']
            pdf_file = request.FILES.get('pdf', '')
            if not year or not month or not day or not area or not plat or not well or not pdf_file:
                pass
            else:
                name = year + ',' + month + ',' + day + ',' + area + ',' + plat + ',' + well
                schema = Schema2(schema_name=name, pdf_file=pdf_file)
                try:
                    schema.save()
                except:
                    pass
        elif(type == "1-2"):
            schemaName = request.POST['schemaName']
            oldSchema = Schema.objects.get(schema_name=schemaName)
            if oldSchema:
                velocity = request.POST['velocity']
                img1 = request.FILES['img1-1']
                img2 = request.FILES['img2-1']
                img3 = request.FILES['img3-1']
                img4 = request.FILES['img4-1']
                oldSchema.image_file_vibration = img1
                oldSchema.velocity = velocity
                oldSchema.image_file_damage = img2
                oldSchema.image_file_blast_heap = img3
                oldSchema.image_file_wall_surface = img4
                try:
                    oldSchema.save()
                    # return render(request, pageName['OpenPit'])
                except:
                    pass
        elif(type == "3-2"):
            schemaName = request.POST['schemaName']
            oldSchema = Schema2.objects.get(schema_name=schemaName)
            if oldSchema:
                velocity = request.POST['velocity']
                img1 = request.FILES['img1-1']
                img2 = request.FILES['img2-1']
                img3 = request.FILES['img3-1']
                img4 = request.FILES['img4-1']
                oldSchema.image_file_vibration = img1
                oldSchema.velocity = velocity
                oldSchema.image_file_damage = img2
                oldSchema.image_file_blast_heap = img3
                oldSchema.image_file_wall_surface = img4
                try:
                    oldSchema.save()
                    # return render(request, pageName['OpenPit'])
                except:
                    pass
        elif(type == "1-3"):
            schemaName2 = request.POST['schemaName2']
            deleteSchema = Schema.objects.get(schema_name=schemaName2) or ''
            try:
                if deleteSchema:
                    deleteSchema.delete()
            except:
                pass
        elif(type == "1-4"):
            part = request.POST['part']
            match = request.POST['match']
            KValue2 = request.POST['KValue2']
            AValue2 = request.POST['AValue2']
            value = KA(k_a_value=part+'_'+KValue2+'_'+AValue2, is_match=match)
            
            try:
                value.save()
            except:
                pass
        elif(type == "3-4"):
            part = request.POST['part']
            KValue2 = request.POST['KValue2']
            AValue2 = request.POST['AValue2']
            oldValue = KA2(k_a_value=part+'_'+KValue2+'_'+AValue2)
            
            try:
                oldValue.save()
            except:
                pass
        elif(type == "1-5"):
            part = request.POST['part2']
            KValue3 = request.POST['KValue3']
            AValue3 = request.POST['AValue3']
            oldValue = KA.objects.get(k_a_value=part+'_'+KValue3+'_'+AValue3)
            try:
                oldValue.delete()
            except:
                pass
        elif(type == "3-5"):
            part = request.POST['part2']
            KValue3 = request.POST['KValue3']
            AValue3 = request.POST['AValue3']
            oldValue = KA2.objects.get(k_a_value=part+'_'+KValue3+'_'+AValue3)
            try:
                oldValue.delete()
            except:
                pass
        elif(type == "3-6"):
            segInput = request.POST['seg-input2']
            oldSeg = Segmentation.objects.get(seg_name=segInput)
            oldValue = Tunnel.objects.filter(tunnel_name__startswith=segInput)
            try:
                oldSeg.delete()
                oldValue.delete()
            except:
                pass
        elif(type == "3-3"):
            schemaName2 = request.POST['schemaName2']
            deleteSchema = Schema2.objects.get(schema_name=schemaName2) or ''
            try:
                if deleteSchema:
                    deleteSchema.delete()
            except:
                pass
        elif(type == "2-1"):
            segmentation = request.POST['segmentation']
            img12 = request.FILES['img1-2']
            if not segmentation or not img12:
                pass
            else:
                seg = Segmentation(seg_name=segmentation, image_img=img12)
                try:
                    seg.save()
                    # return render(request, pageName['OpenPit'])
                except:
                    pass

        elif(type == "2-2"):
            segInput = request.POST['seg-input']
            tunnel = request.POST['tunnel']
            tunnel1 = request.POST['tunnel1']
            tunnel2 = request.POST['tunnel2']
            tunnel3 = request.POST['tunnel3']
            tunnel4 = request.POST['tunnel4']
            tunnel5 = request.POST['tunnel5']
            tunnel6 = request.POST['tunnel6']
            tunnel7 = request.POST['tunnel7']
            tunnel8 = request.POST['tunnel8']
            tunnel9 = request.POST['tunnel9']
            tunnel10 = request.POST['tunnel10']
            if not segInput or not tunnel:
                pass
            else:
                tunnelData = Tunnel(
                    tunnel_name = segInput + ',' + tunnel, 
                    tunnel1_name = tunnel1,
                    tunnel2_name = tunnel2,
                    tunnel3_name = tunnel3,
                    tunnel4_name = tunnel4,
                    tunnel5_name = tunnel5,
                    tunnel6_name = tunnel6,
                    tunnel7_name = tunnel7,
                    tunnel8_name = tunnel8,
                    tunnel9_name = tunnel9,
                    tunnel10_name = tunnel10,
                )
                try:
                    tunnelData.save()
                    # return render(request, pageName['OpenPit'])
                except:
                    pass
        elif(type == "4-1"):
            # 拟合数据
            filed21 = request.POST['filed2']
            t311 = request.POST['t3-1-1']
            t312 = request.POST['t3-1-2']
            t313 = request.POST['t3-1-3']
            t321 = request.POST['t3-2-1']
            t322 = request.POST['t3-2-2']
            t323 = request.POST['t3-2-3']
            t331 = request.POST['t3-3-1']
            t332 = request.POST['t3-3-2']
            t333 = request.POST['t3-3-3']
            t341 = request.POST['t3-4-1']
            t342 = request.POST['t3-4-2']
            t343 = request.POST['t3-4-3']
            t351 = request.POST['t3-5-1']
            t352 = request.POST['t3-5-2']
            t353 = request.POST['t3-5-3']
            t361 = request.POST['t3-6-1']
            t362 = request.POST['t3-6-2']
            t363 = request.POST['t3-6-3']
            if t311 == '' or t321 == '' or t331 == '':
                pass
            elif t341 == '':
                Q = np.array([t311, t321, t331 ])
                R = np.array([t312, t322, t332 ])
                y = np.array([t313, t323, t333 ])
                params, cov = curve_fit(fit_func, (Q, R), y)
                k_fit, a_fit = params
                print(f"拟合的参数：k = {k_fit}, a = {a_fit}")
            elif t351 == '': 
                Q = np.array([t311, t321, t331, t341 ])
                R = np.array([t312, t322, t332, t342 ])
                y = np.array([t313, t323, t333, t343 ])
                params, cov = curve_fit(fit_func, (Q, R), y)
                k_fit, a_fit = params
                print(f"拟合的参数：k = {k_fit}, a = {a_fit}")
            elif t361 == '':
                Q = np.array([t311, t321, t331, t341, t351 ])
                R = np.array([t312, t322, t332, t342, t352 ])
                y = np.array([t313, t323, t333, t343, t353 ])
                params, cov = curve_fit(fit_func, (Q, R), y)
                k_fit, a_fit = params
                print(f"拟合的参数：k = {k_fit}, a = {a_fit}")
            else:
                Q = np.array([t311, t321, t331, t341 , t351 , t361 ])
                R = np.array([t312, t322, t332, t342 , t352 , t362 ])
                y = np.array([t313, t323, t333, t343 , t353 , t363 ])
                params, cov = curve_fit(fit_func, (Q, R), y)
                k_fit, a_fit = params
            result7 = {
                'filed2': filed21,
                't311': t311,
                't312': t312,
                't313': t313,
                't321': t321,
                't322': t322,
                't323': t323,
                't331': t331,
                't332': t332,
                't333': t333,
                't341': t341,
                't342': t342,
                't343': t343,
                't351': t351,
                't352': t352,
                't353': t353,
                't361': t361,
                't362': t362,
                't363': t363,
                'k_fit': k_fit,
                'a_fit': a_fit,
            }
        elif(type == "4-1-2"):
            # 拟合数据
            seg = request.POST['seg-select3']
            tunnel = request.POST['showTunnel200']
            t311 = request.POST['t3-1-1']
            t312 = request.POST['t3-1-2']
            t313 = request.POST['t3-1-3']
            t321 = request.POST['t3-2-1']
            t322 = request.POST['t3-2-2']
            t323 = request.POST['t3-2-3']
            t331 = request.POST['t3-3-1']
            t332 = request.POST['t3-3-2']
            t333 = request.POST['t3-3-3']
            t341 = request.POST['t3-4-1']
            t342 = request.POST['t3-4-2']
            t343 = request.POST['t3-4-3']
            t351 = request.POST['t3-5-1']
            t352 = request.POST['t3-5-2']
            t353 = request.POST['t3-5-3']
            t361 = request.POST['t3-6-1']
            t362 = request.POST['t3-6-2']
            t363 = request.POST['t3-6-3']
            if t311 == '' or t321 == '' or t331 == '':
                pass
            elif t341 == '':
                Q = np.array([t311, t321, t331 ])
                R = np.array([t312, t322, t332 ])
                y = np.array([t313, t323, t333 ])
                params, cov = curve_fit(fit_func, (Q, R), y)
                k_fit, a_fit = params
                print(f"拟合的参数：k = {k_fit}, a = {a_fit}")
            elif t351 == '': 
                Q = np.array([t311, t321, t331, t341 ])
                R = np.array([t312, t322, t332, t342 ])
                y = np.array([t313, t323, t333, t343 ])
                params, cov = curve_fit(fit_func, (Q, R), y)
                k_fit, a_fit = params
                print(f"拟合的参数：k = {k_fit}, a = {a_fit}")
            elif t361 == '':
                Q = np.array([t311, t321, t331, t341, t351 ])
                R = np.array([t312, t322, t332, t342, t352 ])
                y = np.array([t313, t323, t333, t343, t353 ])
                params, cov = curve_fit(fit_func, (Q, R), y)
                k_fit, a_fit = params
                print(f"拟合的参数：k = {k_fit}, a = {a_fit}")
            else:
                Q = np.array([t311, t321, t331, t341 , t351 , t361 ])
                R = np.array([t312, t322, t332, t342 , t352 , t362 ])
                y = np.array([t313, t323, t333, t343 , t353 , t363 ])
                params, cov = curve_fit(fit_func, (Q, R), y)
                k_fit, a_fit = params
            result8 = {
                'seg': seg,
                'tunnel': tunnel,
                't311': t311,
                't312': t312,
                't313': t313,
                't321': t321,
                't322': t322,
                't323': t323,
                't331': t331,
                't332': t332,
                't333': t333,
                't341': t341,
                't342': t342,
                't343': t343,
                't351': t351,
                't352': t352,
                't353': t353,
                't361': t361,
                't362': t362,
                't363': t363,
                'k_fit': k_fit,
                'a_fit': a_fit,
            }
        schemaList = Schema.objects.all()
        result = []
        for item in schemaList:
            result.append({
                'schema_name': item.schema_name,
                'velocity': item.velocity or '',
                'pdf': item.pdf_file.url,
                'img1': item.image_file_vibration.url,
                'img2': item.image_file_damage.url,
                'img3': item.image_file_blast_heap.url,
                'img4': item.image_file_wall_surface.url,
            })
        print(result)
        result2 = []
        for item in Segmentation.objects.all():
            result2.append({
                'seg_name': item.seg_name,
                'img_seg': item.image_img.url,
            })
        print(result2)
        result3 = []
        for item in Tunnel.objects.all():
            result3.append({
                'tunnel_name': item.tunnel_name,
                'tunnel_name1': item.tunnel1_name,
                'tunnel_name2': item.tunnel2_name,
                'tunnel_name3': item.tunnel3_name,
                'tunnel_name4': item.tunnel4_name,
                'tunnel_name5': item.tunnel5_name,
                'tunnel_name6': item.tunnel6_name,
                'tunnel_name7': item.tunnel7_name,
                'tunnel_name8': item.tunnel8_name,
                'tunnel_name9': item.tunnel9_name,
                'tunnel_name10': item.tunnel10_name,
            })
        print(result3)
        result4 = []
        schemaList4 = Schema2.objects.all()
        for item in schemaList4:
            result4.append({
                'schema_name': item.schema_name,
                'velocity': item.velocity or '',
                'pdf': item.pdf_file.url,
                'img1': item.image_file_vibration.url,
                'img2': item.image_file_damage.url,
                'img3': item.image_file_blast_heap.url,
                'img4': item.image_file_wall_surface.url,
            })
        result5 = []
        schemaList5 = KA.objects.all()
        for item in schemaList5:
            result5.append({
                'value': item.k_a_value,
                'match': item.is_match,
            })
        print(result5)
        result6 = []
        schemaList6 = KA2.objects.all()
        for item in schemaList6:
            result6.append({
                'value': item.k_a_value,
                'match': item.is_match,
            })
        print(result6)
        if(type == '4-1'):
            return render(request, pageName['OpenPit'], {'schemas': result, 'KA': result5, 'COM': result7})
        elif(type == '4-1-2'):
            return render(request, pageName['JianShanUndergroundMine'], {'schemas': result4, 'KA': result6, 'segmentations': result2, 'tunnels': result3, 'COM': result8})
        elif(type != "2-1" and type != '2-2' and type != '3-1' and type != '3-2' and type != '3-3' and type != '3-4' and type != '3-5' and type != '3-6'):
            return render(request, pageName['OpenPit'], {'schemas': result, 'KA': result5, 'COM': {}})
        else:
            return render(request, pageName['JianShanUndergroundMine'], {'schemas': result4, 'KA': result6, 'segmentations': result2, 'tunnels': result3, 'COM': {}})
    if request.method == 'GET':
        # Schema.objects.all().delete()
        # Schema2.objects.all().delete()
        # Segmentation.objects.all().delete()
        # Tunnel.objects.all().delete()
        schemaList = Schema.objects.all()
        pageParam = request.GET.get('param1', '')
        result = []
        for item in schemaList:
            result.append({
                'schema_name': item.schema_name,
                'velocity': item.velocity or '',
                'pdf': item.pdf_file.url,
                'img1': item.image_file_vibration.url,
                'img2': item.image_file_damage.url,
                'img3': item.image_file_blast_heap.url,
                'img4': item.image_file_wall_surface.url,
            })
        print(result)
        result5 = []
        schemaList5 = KA.objects.all()
        for item in schemaList5:
            result5.append({
                'value': item.k_a_value,
            })
        print(result5)
        result6 = []
        schemaList6 = KA2.objects.all()
        for item in schemaList6:
            result6.append({
                'value': item.k_a_value,
            })
        print(result6)
        if not pageParam:
            return render(request, pageName['OpenPit'], {'schemas': result, 'KA': result5, 'COM': {}})
        else:
            result4 = []
            schemaList4 = Schema2.objects.all()
            for item in schemaList4:
                result4.append({
                    'schema_name': item.schema_name,
                    'velocity': item.velocity or '',
                    'pdf': item.pdf_file.url,
                    'img1': item.image_file_vibration.url,
                    'img2': item.image_file_damage.url,
                    'img3': item.image_file_blast_heap.url,
                    'img4': item.image_file_wall_surface.url,
                })
            print(result4)
            result2 = []
            for item in Segmentation.objects.all():
                result2.append({
                    'seg_name': item.seg_name,
                    'img_seg': item.image_img.url,
                })
            print(result2)
            result3 = []
            for item in Tunnel.objects.all():
                result3.append({
                    'tunnel_name': item.tunnel_name,
                    'tunnel_name1': item.tunnel1_name,
                    'tunnel_name2': item.tunnel2_name,
                    'tunnel_name3': item.tunnel3_name,
                    'tunnel_name4': item.tunnel4_name,
                    'tunnel_name5': item.tunnel5_name,
                    'tunnel_name6': item.tunnel6_name,
                    'tunnel_name7': item.tunnel7_name,
                    'tunnel_name8': item.tunnel8_name,
                    'tunnel_name9': item.tunnel9_name,
                    'tunnel_name10': item.tunnel10_name,
                })
            return render(request, pageName['JianShanUndergroundMine'], {'schemas': result4, 'KA': result6, 'segmentations': result2, 'tunnels': result3, 'COM': {}})
