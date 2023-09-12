import re

from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model
from django.db.models import Q, Max, Min
from django.shortcuts import render, redirect
from dataBaseApp.models import *
from dataBaseApp.views import pageName

def contains_non_decimal_characters(input_str):
    # 使用正则表达式匹配小数形式的数字
    pattern = r'[^\d.]'
    return bool(re.search(pattern, input_str))

# pageName = {'homePage': 'rock_properties.html',
#
#             # 岩石物性库
#             'RockPropertiesDatabase': 'rock_properties.html',
#             'RockPropertiesDatabaseSearch': 'rock_properties_search.html',
#
#             # 力学实验库的单轴压缩实验
#             'UniaxialCompressionExperimentInMechanicsLabPage': 'uniaxial_compression_experiment.html',
#             # 力学实验库的三轴压缩实验
#             'TriaxialCompressionExperimentInMechanicsLab': 'triaxial_compression_experiment.html',
#             # 力学实验库的抗拉强度实验
#             'TensileStrengthExperimentInMechanicsLab': 'tensile_strength_experiment.html',
#             # 力学实验库的直接剪切实验
#             'DirectShearExperimentInMechanicsLab': 'direct_shear_experiment.html',
#             # 力学实验库的XRD衍射实验
#             'XRDDiffractionExperimentInMechanicsLab': 'xrd_diffraction_experiment.html',
#
#             # 工程数据库中的露天爆破
#             'OpenPitBlastingInEngineeringDatabase': 'open_pit_blasting.html',
#             # 工程数据库中的掘进爆破
#             'TunnelingBlastingInEngineeringDatabase': 'tunneling_blasting.html',
#             # 工程数据库中的回采爆破
#             'RetreatBlastingInEngineeringDatabase': 'retreat_blasting.html',
#
#             # 大数据计算平台
#             'Theoretical_Calculation': 'theoretical_Calculation.html',
#
#             # 大数据分析
#             'Big_Date': 'none.html',
#
#             # 矿山信息
#             'Mine_Date': 'none.html',
#             }


class CustomUserManager(BaseUserManager):
    def create_user(self, name, username, password=None, **extra_fields):
        if not username:
            raise ValueError('必须提供用户名')

        user = self.model(name=name, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    class Meta:
        # 添加这一行来修改关系名称
        db_table = 'auth_user'
        # 指定不同的关系名称，避免与内置User模型的关系名称冲突
        related_name = 'custom_user_manager'

    def create_superuser(self, name, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(name, username, password, **extra_fields)


# 验证密码函数
def custom_authenticate(request, username=None, password=None):
    User = get_user_model()
    try:
        user = User.objects.get(username=username)
        print(user.password)
        if user.password == password:
            return user
    except User.DoesNotExist:
        return None


def search_rocks(request):
    if request.method == 'GET':
        rock_density_isNone = False
        rock_name = request.GET.get('rock_name')
        rock_type = request.GET.get('rock_type')
        selectIndex = [False, False, False]



        match rock_type:
            case "沉积岩":
                selectIndex[0] = True
            case "岩浆岩":
                selectIndex[1] = True
            case "变质岩":
                selectIndex[2] = True
            case _:
                pass
        static_strength = request.GET.get('static_strength')
        dynamic_strength = request.GET.get('dynamic_strength')

        rock_density = request.GET.get('rock_density')
        if rock_density == '' or contains_non_decimal_characters(rock_density):
            rock_density = 0
        else:
            rock_density = float(rock_density)

        longitudinal_velocity = request.GET.get('longitudinal_velocity')
        if longitudinal_velocity == '':
            longitudinal_velocity = 0
        else:
            longitudinal_velocity = float(longitudinal_velocity)

        print(rock_density)

        # 获取最大和最小密度值
        max_density = Rock1.objects.aggregate(Max('rockDensity'))['rockDensity__max']
        min_density = Rock1.objects.aggregate(Min('rockDensity'))['rockDensity__min']

        density_increment = 0.3  # 密度增量
        if rock_density == 0:
            print("走0了")
            rock_density_isNone = True
            if rock_type:
                query = Q(rockType=rock_type)
            if rock_name:
                query &= Q(key__rock_name=rock_name)
            print(query)
            rocks = Rock1.objects.filter(query)
        else:
            while True:
            # 构建查询条件，如果只输入岩石类型无密度，则执行if，如果有岩石类型且有密度，则执行else
                query = Q(rockDensity__gte=float(rock_density) - density_increment) & Q(
                rockDensity__lte=float(rock_density) + density_increment)
                if rock_name:
                    query &= Q(key__rock_name=rock_name)
                if rock_type:
                    query &= Q(rockType=rock_type)

            # if static_strength:
            #     query &= Q(static_strength=static_strength)
            # if dynamic_strength:
            #     query &= Q(dynamic_strength=dynamic_strength)
            # if longitudinal_velocity:
            #     query &= Q(rockLongitudinalWaveVelocity=longitudinal_velocity)

                rocks = Rock1.objects.filter(query)
                print(rocks)
                if rocks.exists() or (density_increment > 2):
                    break
                print(rock_density + density_increment)
            # 扩大精度范围
                density_increment += 0.5
        # return render(request, 'rock_properties_search.html', {'rocks': rocks})
        if rock_density_isNone:
            return render(request, 'rock_properties_search.html',
                              {'rocks': rocks, 'rock_type': rock_type,
                               'selectIndex': selectIndex, 'rock_name': rock_name})
        else:
            return render(request, 'rock_properties_search.html', {'rocks': rocks, 'rock_density': rock_density, 'rock_type': rock_type, 'selectIndex': selectIndex, 'rock_name': rock_name})

def search_rock(request):
    rockData = request.GET.get('rockData')
    rockId = request.GET.get('rockId')
    sorted_objects = []
    match rockData:
        case '2-1':
            try:
                rocks = Rock2.objects.all()
                for rock in rocks:
                    if rock.key.rock_id == rockId:
                        sorted_objects.append(rock)
                if sorted_objects == []:
                    for rock in rocks:
                        if rock.key.rock_id[0] == rockId[0]:
                            if len(rockId) == 1:
                                sorted_objects.append(rock)
                            elif rock.key.rock_id[1] == rockId[1]:
                                sorted_objects.append(rock)
            except:
                sorted_objects = None
            print(sorted_objects)
            page = 'UniaxialCompressionExperimentInMechanicsLabPage'
            return render(request, pageName[page], {'rocks': sorted_objects, 'rockId': rockId})
        case '2-2':
            try:
                rocks = Rock3.objects.all()
                for rock in rocks:
                    if rock.key.rock_id == rockId:
                        sorted_objects.append(rock)
                if sorted_objects == []:
                    for rock in rocks:
                        if rock.key.rock_id[0] == rockId[0]:
                            if len(rockId) == 1:
                                sorted_objects.append(rock)
                            elif rock.key.rock_id[1] == rockId[1]:
                                sorted_objects.append(rock)
            except:
                sorted_objects = None
            page = 'TriaxialCompressionExperimentInMechanicsLab'
            return render(request, pageName[page], {'rocks': sorted_objects, 'rockId': rockId})
        case '2-3':
            try:
                rocks = Rock4.objects.all()
                for rock in rocks:
                    if rock.key.rock_id == rockId:
                        sorted_objects.append(rock)
                if sorted_objects == []:
                    for rock in rocks:
                        if rock.key.rock_id[0] == rockId[0]:
                            if len(rockId) == 1:
                                sorted_objects.append(rock)
                            elif rock.key.rock_id[1] == rockId[1]:
                                sorted_objects.append(rock)
            except:
                sorted_objects = None
            page = 'TensileStrengthExperimentInMechanicsLab'
            return render(request, pageName[page], {'rocks': sorted_objects, 'rockId': rockId})
        case '2-4':
            try:
                rocks = Rock5.objects.all()
                for rock in rocks:
                    if rock.key.rock_id == rockId:
                        sorted_objects.append(rock)
                if sorted_objects == []:
                    for rock in rocks:
                        if rock.key.rock_id[0] == rockId[0]:
                            if len(rockId) == 1:
                                sorted_objects.append(rock)
                            elif rock.key.rock_id[1] == rockId[1]:
                                sorted_objects.append(rock)
            except:
                sorted_objects = None
            page = 'DirectShearExperimentInMechanicsLab'
            return render(request, pageName[page], {'rocks': sorted_objects, 'rockId': rockId})
        case '2-5':
            try:
                rocks = Rock6.objects.all()
                for rock in rocks:
                    if rock.key.rock_id == rockId:
                        sorted_objects.append(rock)
                if sorted_objects == []:
                    for rock in rocks:
                        if rock.key.rock_id[0] == rockId[0]:
                            if len(rockId) == 1:
                                sorted_objects.append(rock)
                            elif rock.key.rock_id[1] == rockId[1]:
                                sorted_objects.append(rock)
            except:
                sorted_objects = None
            page = 'XRDDiffractionExperimentInMechanicsLab'
            return render(request, pageName[page], {'rocks': sorted_objects, 'rockId': rockId})
        case '3-1':
            try:
                rocks = Rock7.objects.all()
                for rock in rocks:
                    if rock.key.rock_id == rockId:
                        sorted_objects.append(rock)
                if sorted_objects == []:
                    for rock in rocks:
                        if rock.key.rock_id[0] == rockId[0]:
                            if len(rockId) == 1:
                                sorted_objects.append(rock)
                            elif rock.key.rock_id[1] == rockId[1]:
                                sorted_objects.append(rock)
            except:
                sorted_objects = None
            page = 'OpenPitBlastingInEngineeringDatabase'
            return render(request, pageName[page], {'rocks': sorted_objects, 'rockId': rockId})
        case '3-2':
            try:
                rocks = Rock8.objects.all()
                for rock in rocks:
                    if rock.key.rock_id == rockId:
                        sorted_objects.append(rock)
                if sorted_objects == []:
                    for rock in rocks:
                        if rock.key.rock_id[0] == rockId[0]:
                            if len(rockId) == 1:
                                sorted_objects.append(rock)
                            elif rock.key.rock_id[1] == rockId[1]:
                                sorted_objects.append(rock)
            except:
                sorted_objects = None
            page = 'TunnelingBlastingInEngineeringDatabase'
            return render(request, pageName[page], {'rocks': sorted_objects, 'rockId': rockId})
        case '3-3':
            try:
                rocks = Rock9.objects.all()
                for rock in rocks:
                    if rock.key.rock_id == rockId:
                        sorted_objects.append(rock)
                if sorted_objects == []:
                    for rock in rocks:
                        if rock.key.rock_id[0] == rockId[0]:
                            if len(rockId) == 1:
                                sorted_objects.append(rock)
                            elif rock.key.rock_id[1] == rockId[1]:
                                sorted_objects.append(rock)
            except:
                sorted_objects = None
            page = 'RetreatBlastingInEngineeringDatabase'
            return render(request, pageName[page], {'rocks': sorted_objects, 'rockId': rockId})
        case _:
            sorted_objects = None
            page = 'RockPropertiesDatabase'
            return render(request, pageName[page], {'rocks': sorted_objects})