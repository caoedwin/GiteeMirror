from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
import datetime,os
from django.http import HttpResponse
import datetime,json,simplejson
from .models import LowLightList
from CQM.models import CQMProject
from app01.models import UserInfo, ProjectinfoinDCT, Role
from django.db import transaction
from django.forms.models import model_to_dict
# Create your views here.
@csrf_exempt
def LowLightList_edit(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    Skin = request.COOKIES.get('Skin_raw')
    # print(Skin)
    if not Skin:
        Skin = "/static/src/blue.jpg"
    weizhi = "Reliability Test Data/CQM_edit"
    mock_data = [

    ]
    selectItem = [
        # "C38(NB)","C38(AIO)","A39","Other"
    ]
    searchalert = [
    ]

    canEdit = 0#编辑机种的权限
    aa = {"flag": 0}#弹窗1为此提案数据被编辑
    cc = {"statu": 4}#角色权限
    for i in CQMProject.objects.all().values('Customer').distinct().order_by('Customer'):
        # # print(i)
        # Project = []
        # for j in CQMProject.objects.filter(Customer=i['Customer']).values('Project').distinct().order_by('Project'):
        #     Project.append({"Project": j['Project']})
        selectItem.append(i['Customer'])
    roles = []
    onlineuser = request.session.get('account')
    # print(UserInfo.objects.get(account=onlineuser))
    for i in UserInfo.objects.get(account=onlineuser).role.all():
        roles.append(i.name)
    # print(roles)
    editPpriority = 0
    for i in roles:
        if 'DQA_SW' in i:
            editPpriority = 1
        elif 'LD' in i:
            if editPpriority != 1:
                editPpriority = 2
        elif 'RD' in i:
            if editPpriority != 1 and editPpriority != 2:
                editPpriority = 3

    cc = {"statu": editPpriority}
    # print(editPpriority)
    alert=0
    # print(request.POST)
    # print(request.body)
    if request.method == "POST":
        if request.POST.get('isGetData') == 'SEARCH':
            Customer = request.POST.get('Customer')
            ProjectCompal = request.POST.get('ProjectCompal')
            if editPpriority == 1:
                check_Owner_dic = {"Customer": Customer, "Project": ProjectCompal}
                Projectinfo = CQMProject.objects.filter(**check_Owner_dic).first()
                current_user = request.session.get('user_name')
                if Projectinfo:
                    for k in Projectinfo.Owner.all():
                        # print(i.username,current_user)
                        # print(type(i.username),type(current_user))
                        if k.username == current_user:
                            canEdit = 1
                            break


        aa = {"flag": alert}
        data = {
            "err_ok": "0",
            "content": mock_data,
            "select": selectItem,
            "canEdit": canEdit,
            "orr": cc,
            "orn": aa,
            "sear": searchalert
        }
        return HttpResponse(json.dumps(data), content_type="application/json")
    return render(request, 'LowLightList/LowLightList_edit.html', locals())