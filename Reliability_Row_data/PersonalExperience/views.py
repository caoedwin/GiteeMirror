from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import datetime, json, simplejson, requests, time
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app01.models import UserInfo, ProjectinfoinDCT
from PersonalInfo.models import PersonalInfo
from django.db.models import Max, Min, Sum, Count, Q, F, Value, CharField
from django.db.models.functions import Substr
from operator import itemgetter, attrgetter
from collections import Counter
from .models import PerExperience, OSR_OSinfo
from django.db.models.functions import ExtractYear


@csrf_exempt
def NPI_upload(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    Skin = request.COOKIES.get('Skin_raw')
    # print(Skin)
    if not Skin:
        Skin = "/static/src/blue.jpg"
    weizhi = "PersonalExperience/NPI_upload"


    errMsgNumber = ''

    sectionProject = [
        # {"value": "GLMS1", "SS_Date": "2021/02/03"}, {"value": "HLS4I", "SS_Date": "2021/02/04"},
    ]

    for i in ProjectinfoinDCT.objects.all():
        datastr = i.SS.split(' ')[0].split('/')
        sectionProject.append({"value": i.ComPrjCode, "SS_Date": datastr[2] + "-" + datastr[0] + "-" + datastr[1]})
    # print(request.body)
    # print(request.POST)
    if request.method == "POST":
        if request.POST.get('action') == 'addSubmit':
            # print(request.POST.get('Project'))
            updata_dic = {}
            updata_dic['Proposer_Num'] = request.session.get('account')
            # updata_dic['Proposer_NameE'] = request.session.get('user_name')
            PersonalInfos = PersonalInfo.objects.filter(Q(GroupNum=updata_dic['Proposer_Num']) | Q(SAPNum=updata_dic['Proposer_Num'])).first()
            # print(PersonalInfos)
            updata_dic['Project'] = request.POST.get('Project')
            updata_dic['Role'] = request.POST.get('Role')
            updata_dic['Function'] = request.POST.get('Function')
            updata_dic['SubFunction_Com'] = request.POST.get('SubFunction')
            updata_dic['Phase'] = request.POST.get('Phase')
            if PerExperience.objects.filter(**updata_dic):
                errMsgNumber = "您已申请过：Project:%s-Phase:%s-Function:%s-SubFunction:%s-Role:%s" % (updata_dic['Project'], updata_dic['Phase'],
                                                                                         updata_dic['Function'], updata_dic['SubFunction_Com'],
                                                                                         updata_dic['Role'])
            else:
                updata_dic['Proposer_Name'] = PersonalInfos.CNName
                updata_dic['Dalei'] = "NPI"
                updata_dic['Department_Code'] = PersonalInfos.DepartmentCode
                updata_dic['Approved_Officer'] = ProjectinfoinDCT.objects.filter(ComPrjCode=request.POST.get('Project')).first().DQAPLNum
                # print(ProjectinfoinDCT.objects.filter(ComPrjCode=request.POST.get('Project')).first())
                # print(ProjectinfoinDCT.objects.filter(ComPrjCode=request.POST.get('Project')).first().DQAPLNum)
                updata_dic['SS_Date'] = request.POST.get('SS_Date')
                updata_dic['Comments'] = request.POST.get('Comments')
                updata_dic['EditTime'] = datetime.datetime.now().strftime("%Y-%m-%d")
                updata_dic['Status'] = "待簽核"
                if updata_dic['Approved_Officer']:
                    PerExperience.objects.create(**updata_dic)
                else:
                    errMsgNumber = "Project:%s DQAPL的工号缺失" % updata_dic['Project']


        data = {
            "sectionProject": sectionProject,
            "errMsgNumber": errMsgNumber,

        }
        return HttpResponse(json.dumps(data), content_type="application/json")

    return render(request, 'PersonalExperience/NPI_upload.html', locals())

@csrf_exempt
def INV_upload(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    Skin = request.COOKIES.get('Skin_raw')
    # print(Skin)
    if not Skin:
        Skin = "/static/src/blue.jpg"
    weizhi = "PersonalExperience/INV_upload"

    errMsgNumber = ''

    sectionProject = [
        # {"value": "GLMS1", "SS_Date": "2021/02/03"}, {"value": "HLS4I", "SS_Date": "2021/02/04"},
    ]
    for i in ProjectinfoinDCT.objects.all():
        datastr = i.SS.split(' ')[0].split('/')
        sectionProject.append({"value": i.ComPrjCode, "SS_Date": datastr[2] + "-" + datastr[0] + "-" + datastr[1]})

    if request.method == 'POST':
        if request.POST.get('action') == 'addSubmit':
            # print(request.POST.get('Project'))
            updata_dic = {}
            updata_dic['Proposer_Num'] = request.session.get('account')
            # updata_dic['Proposer_NameE'] = request.session.get('user_name')
            PersonalInfos = PersonalInfo.objects.filter(Q(GroupNum=updata_dic['Proposer_Num']) | Q(SAPNum=updata_dic['Proposer_Num'])).first()
            # print(PersonalInfos)
            updata_dic['Project'] = request.POST.get('Project')
            updata_dic['Role'] = request.POST.get('Role')
            updata_dic['Function'] = request.POST.get('Function')
            updata_dic['Time_Interval'] = request.POST.get('Month')
            updata_dic['Year'] = request.POST.get('Year')
            if PerExperience.objects.filter(**updata_dic):
                errMsgNumber = "您已申请过：Project:%s-Phase:%s-Function:%s-SubFunction:%s-Role:%s" % (updata_dic['Project'], updata_dic['Phase'],
                                                                                         updata_dic['Function'], updata_dic['SubFunction_Com'],
                                                                                         updata_dic['Role'])
            else:
                updata_dic['Proposer_Name'] = PersonalInfos.CNName
                updata_dic['Dalei'] = "INV"
                updata_dic['KeypartNum'] = request.POST.get('KeypartNum')
                updata_dic['Department_Code'] = PersonalInfos.DepartmentCode
                updata_dic['Approved_Officer'] = ProjectinfoinDCT.objects.filter(ComPrjCode=request.POST.get('Project')).first().DQAPLNum
                # print(ProjectinfoinDCT.objects.filter(ComPrjCode=request.POST.get('Project')).first())
                # print(ProjectinfoinDCT.objects.filter(ComPrjCode=request.POST.get('Project')).first().DQAPLNum)
                updata_dic['SS_Date'] = request.POST.get('SS_Date')
                updata_dic['Comments'] = request.POST.get('Comments')
                updata_dic['EditTime'] = datetime.datetime.now().strftime("%Y-%m-%d")
                updata_dic['Status'] = "待簽核"
                if updata_dic['Approved_Officer']:
                    PerExperience.objects.create(**updata_dic)
                else:
                    errMsgNumber = "Project:%s DQAPL的工号缺失" % updata_dic['Project']
        data = {
            "sectionProject": sectionProject,
            "errMsgNumber": errMsgNumber,
        }
        # print(data)
        return HttpResponse(json.dumps(data), content_type="application/json")

    return render(request, 'PersonalExperience/INV_upload.html', locals())

@csrf_exempt
def OSR_upload(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    Skin = request.COOKIES.get('Skin_raw')
    # print(Skin)
    if not Skin:
        Skin = "/static/src/blue.jpg"
    weizhi = "PersonalExperience/OSR_upload"

    errMsgNumber = ''

    sectionProject = [
        # {"value": "GLMS1", "SS_Date": "2021/02/03"}, {"value": "HLS4I", "SS_Date": "2021/02/04"},
    ]

    sectionPhase = [
        # "Win11", "win10", "XP"
                    ]
    for i in OSR_OSinfo.objects.all():
        sectionPhase.append(i.OSinfo)
    CanEdit = 1
    DQAPLNum = request.session.get('account')
    for i in ProjectinfoinDCT.objects.all():
        datastr = i.SS.split(' ')[0].split('/')
        sectionProject.append({"value": i.ComPrjCode, "SS_Date": datastr[2] + "-" + datastr[0] + "-" + datastr[1]})
        if DQAPLNum == i.DQAPLNum:
            CanEdit = 1
    if request.method == 'POST':
        if request.POST.get('action') == 'SubmitOSR':
            # print(request.POST.get('Project'))
            updataOS_dic = {}
            updataOS_dic['OSinfo'] = request.POST.get('OSR')
            if OSR_OSinfo.objects.filter(**updataOS_dic):
                errMsgNumber = "OS:%s 已经存在" % updataOS_dic['OSinfo']
            else:
                updataOS_dic['EditTime'] = datetime.datetime.now().strftime("%Y-%m-%d")
                updataOS_dic['Editer'] = request.session.get('account')
                OSR_OSinfo.objects.create(**updataOS_dic)
                sectionPhase = [
                    # "Win11", "win10", "XP"
                ]
                for i in OSR_OSinfo.objects.all():
                    sectionPhase.append(i.OSinfo)
        if request.POST.get('action') == 'addSubmit':
            # print(request.POST.get('Project'))
            updata_dic = {}
            updata_dic['Proposer_Num'] = request.session.get('account')
            # updata_dic['Proposer_NameE'] = request.session.get('user_name')
            PersonalInfos = PersonalInfo.objects.filter(Q(GroupNum=updata_dic['Proposer_Num']) | Q(SAPNum=updata_dic['Proposer_Num'])).first()
            # print(PersonalInfos)
            updata_dic['Project'] = request.POST.get('Project')
            updata_dic['Role'] = request.POST.get('Role')
            updata_dic['Function'] = request.POST.get('Function')
            updata_dic['SubFunction_Com'] = request.POST.get('SubFunction')
            updata_dic['Phase'] = request.POST.get('Phase')
            if PerExperience.objects.filter(**updata_dic):
                errMsgNumber = "您已申请过：Project:%s-Phase:%s-Function:%s-SubFunction:%s-Role:%s" % (updata_dic['Project'], updata_dic['Phase'],
                                                                                         updata_dic['Function'], updata_dic['SubFunction_Com'],
                                                                                         updata_dic['Role'])
            else:
                updata_dic['Proposer_Name'] = PersonalInfos.CNName
                updata_dic['Dalei'] = "OSR"
                updata_dic['Department_Code'] = PersonalInfos.DepartmentCode
                updata_dic['Approved_Officer'] = ProjectinfoinDCT.objects.filter(ComPrjCode=request.POST.get('Project')).first().DQAPLNum
                # print(ProjectinfoinDCT.objects.filter(ComPrjCode=request.POST.get('Project')).first())
                # print(ProjectinfoinDCT.objects.filter(ComPrjCode=request.POST.get('Project')).first().DQAPLNum)
                updata_dic['SS_Date'] = request.POST.get('SS_Date')
                updata_dic['Comments'] = request.POST.get('Comments')
                updata_dic['EditTime'] = datetime.datetime.now().strftime("%Y-%m-%d")
                updata_dic['Status'] = "待簽核"
                if updata_dic['Approved_Officer']:
                    PerExperience.objects.create(**updata_dic)
                else:
                    errMsgNumber = "Project:%s DQAPL的工号缺失" % updata_dic['Project']
        data = {
            "sectionProject": sectionProject,
            "sectionPhase": sectionPhase,
            "errMsgNumber": errMsgNumber,
            "CanEdit": CanEdit,

        }
        # print(data)
        return HttpResponse(json.dumps(data), content_type="application/json")

    return render(request, 'PersonalExperience/OSR_upload.html', locals())

@csrf_exempt
def My_application(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    Skin = request.COOKIES.get('Skin_raw')
    # print(Skin)
    if not Skin:
        Skin = "/static/src/blue.jpg"
    weizhi = "PersonalExperience/My_application"



    if request.method == 'POST':

        data = {
            "err_Msg": "",
        }
        # print(data)
        return HttpResponse(json.dumps(data), content_type="application/json")

    return render(request, 'PersonalExperience/My_application.html', locals())

@csrf_exempt
def My_approve(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    Skin = request.COOKIES.get('Skin_raw')
    # print(Skin)
    if not Skin:
        Skin = "/static/src/blue.jpg"
    weizhi = "PersonalExperience/My_approve"



    if request.method == 'POST':

        data = {
            "err_Msg": "",
        }
        # print(data)
        return HttpResponse(json.dumps(data), content_type="application/json")
    return render(request, 'PersonalExperience/My_approve.html', locals())

@csrf_exempt
def Summary(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    Skin = request.COOKIES.get('Skin_raw')
    # print(Skin)
    if not Skin:
        Skin = "/static/src/blue.jpg"
    weizhi = "PersonalExperience/Summary"
    err_Msg = ''


    if request.method == 'POST':

        data = {
            "err_Msg": err_Msg,
        }
        # print(data)
        return HttpResponse(json.dumps(data), content_type="application/json")

    return render(request, 'PersonalExperience/Summary.html', locals())

