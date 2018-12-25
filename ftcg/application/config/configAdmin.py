# -*- coding: utf-8 -*-
import logging
import django.utils.log
import logging.handlers
import json
import time
import sys
sys.path.append('...')
from ftcg.models import street
from ftcg.models import community
from ftcg.models import village


from ..user import signAdmin
import django.utils.log


# 验证token
def verificationToken(request):
    token = request.GET['token'];
    if len(token) == 32:
        logger = logging.getLogger("django")
        logger.info('token->')
        return signAdmin.verificationToken(token)
    return False



# 验证为空的Parm信息
def verificationNullParm(request,parm):
    try:
        parms = request.GET[parm]
        if len(parms) == 0:
            return None
        return parms
    except BaseException as e:
        return None


# 创建街道的数据
def baseConfigStreet(request):
    name_parm = request.GET['name'];
    callBackDict = {}
    # 验证token
    if verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    if len(name_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '街道名称为空'
        return callBackDict
    number_parm = verificationNullParm(request,'number')
    address_parm = verificationNullParm(request, 'address')
    personCharge_parm = verificationNullParm(request, 'personCharge')
    phone_parm = verificationNullParm(request, 'phone')
    remarks_parm = verificationNullParm(request, 'remarks')
    managementSubsetNum_parm = verificationNullParm(request, 'managementSubsetNum')
    try:
        obj = street.objects.create(name=name_parm,number=number_parm,address=address_parm,personCharge=personCharge_parm,phone=phone_parm,remarks=remarks_parm,managementSubsetNum=managementSubsetNum_parm)
        obj.save()
        callBackDict['code'] = '1'
        callBackDict['data'] = obj.id
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict


# 创建社区
def baseConfigCommunity(request):
    name_parm = request.GET['name'];
    streetId_parm = request.GET['streetId'];
    callBackDict = {}
    if len(name_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '社区的名称为空'
        return callBackDict
    if len(streetId_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '街道的id为空'
        return callBackDict
    # 验证token
    if verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    # 获取其它参数
    number_parm = verificationNullParm(request, 'number')
    address_parm = verificationNullParm(request, 'address')
    personCharge_parm = verificationNullParm(request, 'personCharge')
    phone_parm = verificationNullParm(request, 'phone')
    remarks_parm = verificationNullParm(request, 'remarks')
    managementSubsetNum_parm = verificationNullParm(request, 'managementSubsetNum')
    try:
        obj = community.objects.create(streetId=streetId_parm, name=name_parm, number=number_parm, address=address_parm,
                                    personCharge=personCharge_parm, phone=phone_parm, remarks=remarks_parm,
                                    managementSubsetNum=managementSubsetNum_parm)
        obj.save()
        callBackDict['code'] = '1'
        callBackDict['data'] = obj.id
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict


# 创建小区的数据
# 0是普通小区，1是学校，2是政府机关，3是收储运公司
def baseConfigVillage(request):
    streetId_parm = request.GET['streetId'];
    communityId_parm = request.GET['communityId'];
    name_parm = request.GET['name'];
    type_parm = request.GET['type'];
    callBackDict = {}
    # 验证token
    if verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    if len(streetId_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '所属街道ID为空'
        return callBackDict
    if len(communityId_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '所属社区ID为空'
        return callBackDict
    if len(name_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '小区名称为空'
        return callBackDict
    if len(type_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '请选择小区的类型'
        return callBackDict
    # 获取其它参数
    number_parm = verificationNullParm(request, 'number')
    address_parm = verificationNullParm(request, 'address')
    personCharge_parm = verificationNullParm(request, 'personCharge')
    phone_parm = verificationNullParm(request, 'phone')
    remarks_parm = verificationNullParm(request, 'remarks')
    managementSubsetNum_parm = verificationNullParm(request, 'managementSubsetNum')
    try:
        obj = village.objects.create(communityId=communityId_parm,streetId=streetId_parm, name=name_parm, number=number_parm, address=address_parm,
                                       personCharge=personCharge_parm, phone=phone_parm, remarks=remarks_parm,
                                       managementSubsetNum=managementSubsetNum_parm)
        obj.save()
        callBackDict['code'] = '1'
        callBackDict['data'] = obj.id
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 获取所有街道的数据
def getStreets(request):
    callBackDict = {}
    try:
        streetList = street.objects.all()
        list = []
        for oneStreet in streetList:
            list.append({'id':oneStreet.id,'name':oneStreet.name,'number': oneStreet.number,
                                        'address': oneStreet.address, 'personCharge': oneStreet.personCharge,
                                        'phone': oneStreet.phone, 'remarks': oneStreet.remarks,
                                        'managementSubsetNum': oneStreet.managementSubsetNum})
        callBackDict['code'] = '1'
        callBackDict['data'] = list
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 获取指定街道的社区数据
def getCommunitys(request):
    callBackDict = {}
    streetId_parm = request.GET['streetId']
    if len(streetId_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '所属街道ID为空'
        return callBackDict
    try:
        communityList = community.objects.filter(streetId=streetId_parm)
        list = []
        for oneCommunity in communityList:
            list.append({'id': oneCommunity.id, 'name': oneCommunity.name, 'number': oneCommunity.number,
                         'address': oneCommunity.address, 'personCharge': oneCommunity.personCharge,
                         'phone': oneCommunity.phone, 'remarks': oneCommunity.remarks,
                         'managementSubsetNum': oneCommunity.managementSubsetNum})
        callBackDict['code'] = '1'
        callBackDict['data'] = list
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict




# 获取指定街道的小区数据
def getVillages(request):
    callBackDict = {}
    streetId_parm = request.GET['streetId']
    if len(streetId_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '所属街道ID为空'
        return callBackDict
    communityId_parm = verificationNullParm(request,'communityId')
    try:
        if communityId_parm == None:
            villageList = village.objects.filter(streetId=streetId_parm, isOpen=0)
        else:
            villageList = village.objects.filter(streetId=streetId_parm, communityId=communityId_parm,isOpen=0)
        list = []
        for oneVillage in villageList:
             list.append({'id': oneVillage.id, 'name': oneVillage.name,'type': oneVillage.type,'number': oneVillage.number,
                                        'address': oneVillage.address, 'personCharge': oneVillage.personCharge,
                                        'phone': oneVillage.phone, 'remarks': oneVillage.remarks,
                                        'managementSubsetNum': oneVillage.managementSubsetNum})
        callBackDict['code'] = '1'
        callBackDict['data'] = list
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict


# 开启小区
def openVillage(request):
    villageId_parm = request.GET['villageId']
    callBackDict = {}
    if len(villageId_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '小区的ID为空'
        return callBackDict
    # 验证token
    if verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        # 更新密码
        villageObj = village.objects.get(id=villageId_parm)
        villageObj.isOpen = 0
        villageObj.save()
        callBackDict['code'] = '1'
        callBackDict['msg'] = '开启成功'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '密码错误'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 关闭小区
def closeVillage(request):
    villageId_parm = request.GET['villageId']
    callBackDict = {}
    if len(villageId_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '小区的ID为空'
        return callBackDict
    # 验证token
    if verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        # 更新密码
        villageObj = village.objects.get(id=villageId_parm)
        villageObj.isOpen = 1
        villageObj.save()
        callBackDict['code'] = '1'
        callBackDict['msg'] = '关闭成功'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '密码错误'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 删除街道
def deleteStreet(request):
    callBackDict = {}
    streetId = request.GET['streetId']
    if len(streetId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '所属街道ID为空'
        return callBackDict
    # 验证token
    if verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        # 执行删除数据及关系
        street.objects.filter(id=streetId).delete()
        village.objects.filter(streetId=streetId).delete()
        callBackDict['code'] = '1'
        callBackDict['msg'] = '删除成功，同时删除了该街道下的所有小区'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict


# 删除社区
def deleteCommunity(request):
    callBackDict = {}
    communityId = request.GET['communityId']
    if len(communityId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '删除社区ID为空'
        return callBackDict
    # 验证token
    if verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        # 执行删除数据及关系
        community.objects.filter(id=communityId).delete()
        village.objects.filter(communityId=communityId).delete()
        callBackDict['code'] = '1'
        callBackDict['msg'] = '删除成功，同时删除了该社区下的所有小区'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 删除小区
def deleteVillage(request):
    callBackDict = {}
    villageId = request.GET['villageId']
    if len(villageId) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '删除的小区ID为空'
        return callBackDict
    # 验证token
    if verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    try:
        # 执行删除数据及关系
        village.objects.filter(id=villageId).delete()
        callBackDict['code'] = '1'
        callBackDict['msg'] = '删除成功'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        return callBackDict
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict



# 编辑小区的数据
# 0是普通小区，1是学校，2是政府机关，3是收储运公司
def editBaseConfigVillage(request):
    villageId_parm = request.GET['villageId'];
    callBackDict = {}
    # 验证token
    if verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    if len(villageId_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '小区的ID为空'
        return callBackDict
    # 获取其它参数
    name_parm = verificationNullParm(request, 'name')
    number_parm = verificationNullParm(request, 'number')
    address_parm = verificationNullParm(request, 'address')
    personCharge_parm = verificationNullParm(request, 'personCharge')
    phone_parm = verificationNullParm(request, 'phone')
    remarks_parm = verificationNullParm(request, 'remarks')
    managementSubsetNum_parm = verificationNullParm(request, 'managementSubsetNum')
    try:
        obj = village.objects.get(id=villageId_parm)
        if name_parm :
            obj.name = name_parm
        if number_parm :
            obj.number = number_parm
        if address_parm :
            obj.address = address_parm
        if personCharge_parm :
            obj.personCharge = personCharge_parm
        if phone_parm :
            obj.phone = phone_parm
        if remarks_parm :
            obj.remarks = remarks_parm
        if managementSubsetNum_parm :
            obj.managementSubsetNum = managementSubsetNum_parm
        obj.save()
        callBackDict['code'] = '1'
        callBackDict['msg'] = '编辑成功'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict


# 编辑社区的数据
def editBaseConfigCommunity(request):
    communityId_parm = request.GET['communityId'];
    callBackDict = {}
    # 验证token
    if verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    if len(communityId_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '社区的ID为空'
        return callBackDict
    # 获取其它参数
    name_parm = verificationNullParm(request, 'name')
    number_parm = verificationNullParm(request, 'number')
    address_parm = verificationNullParm(request, 'address')
    personCharge_parm = verificationNullParm(request, 'personCharge')
    phone_parm = verificationNullParm(request, 'phone')
    remarks_parm = verificationNullParm(request, 'remarks')
    managementSubsetNum_parm = verificationNullParm(request, 'managementSubsetNum')
    try:
        obj = community.objects.get(id=communityId_parm)
        if name_parm:
            obj.name = name_parm
        if number_parm:
            obj.number = number_parm
        if address_parm:
            obj.address = address_parm
        if personCharge_parm:
            obj.personCharge = personCharge_parm
        if phone_parm:
            obj.phone = phone_parm
        if remarks_parm:
            obj.remarks = remarks_parm
        if managementSubsetNum_parm:
            obj.managementSubsetNum = managementSubsetNum_parm
        obj.save()
        callBackDict['code'] = '1'
        callBackDict['msg'] = '编辑成功'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict




# 编辑街道的数据
def editBaseConfigStreet(request):
    streetId_parm = request.GET['streetId'];
    callBackDict = {}
    # 验证token
    if verificationToken(request) == False:
        callBackDict['code'] = '0'
        callBackDict['msg'] = 'token异常'
        return callBackDict
    if len(streetId_parm) == 0:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '街道的ID为空'
        return callBackDict
    # 获取其它参数
    name_parm = verificationNullParm(request, 'name')
    number_parm = verificationNullParm(request, 'number')
    address_parm = verificationNullParm(request, 'address')
    personCharge_parm = verificationNullParm(request, 'personCharge')
    phone_parm = verificationNullParm(request, 'phone')
    remarks_parm = verificationNullParm(request, 'remarks')
    managementSubsetNum_parm = verificationNullParm(request, 'managementSubsetNum')
    try:
        obj = street.objects.get(id=streetId_parm)
        if name_parm:
            obj.name = name_parm
        if number_parm:
            obj.number = number_parm
        if address_parm:
            obj.address = address_parm
        if personCharge_parm:
            obj.personCharge = personCharge_parm
        if phone_parm:
            obj.phone = phone_parm
        if remarks_parm:
            obj.remarks = remarks_parm
        if managementSubsetNum_parm:
            obj.managementSubsetNum = managementSubsetNum_parm
        obj.save()
        callBackDict['code'] = '1'
        callBackDict['msg'] = '编辑成功'
    except BaseException as e:
        callBackDict['code'] = '0'
        callBackDict['msg'] = '系统异常'
        logger = logging.getLogger("django")
        logger.info(str(e))
    return callBackDict
