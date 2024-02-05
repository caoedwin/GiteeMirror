from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
import datetime,os
from django.http import HttpResponse
import datetime,json,simplejson
from .models import IssuesBreakdown
from CQM.models import CQMProject
from app01.models import UserInfo, ProjectinfoinDCT, Role
from django.db import transaction
from django.forms.models import model_to_dict
# Create your views here.
headermodel_IssuesBreakdown = {
    'Customer': 'Customer', 'Project': 'Project', 'FFRT Entry unclose issue': 'FFRT_Entry_unclose_issue', 'SIT Exit unclose issue': 'SIT_Exit_unclose_issue', '1st FFRT': 'first_FFRT',
    '2nd FFRT': 'second_FFRT', '3rd FFRT': 'third_FFRT', '4th FFRT': 'fourth_FFRT',
    '5th FFRT': 'fifth_FFRT', '6th FFRT': 'sixth_FFRT', '分類': 'issue_def', 'Remark': 'Remark', 'FFRT': 'FFRT',
    'Defect ID': 'Defect_ID', 'Title': 'Title', 'Create date': 'Create_date', 'Update date': 'Update_date', 'Status': 'Status',
    'Severity': 'Severity',
    'Category': 'Category', 'Component': 'Component', 'BIOS/KBC': 'BIOS_KBC', 'Comments': 'Comments',
    'Author': 'Author', 'Assign to': 'Assign_to', 'Description': 'Description', 'Reproduce steps': 'Reproduce_steps',
    'Age': 'Age',
}
@csrf_exempt
def IssuesBreakdown_edit(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    Skin = request.COOKIES.get('Skin_raw')
    # print(Skin)
    if not Skin:
        Skin = "/static/src/blue.jpg"
    weizhi = "DDIS/IssuesBreakdown_edit"
    ProjectCodeOption = {
        # "C38(NB)": [{"Projectcode": "ILYE3"},
        #             {"Projectcode": "JLV31"},
        #             {"Projectcode": "FLV34"},
        #             {"Projectcode": "GLSM1"}],
        # "C38(AIO)": [{"Projectcode": "ILYE3"},
        #              {"Projectcode": "JLV31"},
        #              {"Projectcode": "FLV34"},
        #              {"Projectcode": "GLSM1"}],
        # "C85": [{"Projectcode": "ILYE3"},
        #         {"Projectcode": "JLV31"},
        #         {"Projectcode": "FLV34"},
        #         {"Projectcode": "GLSM1"}],
        # "T88(AIO)": [{"Projectcode": "ILYE3"},
        #              {"Projectcode": "JLV31"},
        #              {"Projectcode": "FLV34"},
        #              {"Projectcode": "GLSM1"}],
    }


    mock_data = [
        # {"id": 1, "Customer": "C38(NB)", "ProjectcodeCompal": "ILYE3", "ProjectcodeCustomer": "Y580S-16IRH",
        #  "Lowlight_item": "Thermal and power setting frozen too late", "Root_cause": "For EOY10 SDV phase test",
        #  "LD": "Jazz_Lin", "Owner": "", "Mitigation_plan": "",
        #  },
        # {"id": 2, "Customer": "C38(NB)", "ProjectcodeCompal": "ILYE3", "ProjectcodeCustomer": "Y580S-16IRH",
        #  "Lowlight_item": "Thermal and power setting frozen too late", "Root_cause": "For EOY10 SDV phase test",
        #  "LD": "Jazz_Lin", "Owner": "", "Mitigation_plan": "",
        #  },
    ]

    errMsg = ''

    uploadpermission = 0  # 1:能编辑 0:不能编辑


    roles = []
    onlineuser = request.session.get('account')
    # print(UserInfo.objects.get(account=onlineuser))
    for i in UserInfo.objects.get(account=onlineuser).role.all():
        roles.append(i.name)
    # print(roles)
    editPpriority = 0
    for i in roles:
        if 'DQA_SW' in i or 'admin' == i:
            editPpriority = 1
        elif 'LD' in i:
            if editPpriority != 1:
                editPpriority = 2
        elif 'RD' in i:
            if editPpriority != 1 and editPpriority != 2:
                editPpriority = 3


    # print(request.POST)
    # print(request.body)
    if request.method == "POST":
        canEdit = 0
        if request.POST.get('isGetData') == 'first':
            pass

        if request.POST.get('isGetData') == 'SEARCH':
            pass
        else:
            try:
                request.body
            except:
                pass
            else:
                if 'MUTIDELETE' in str(request.body):
                    responseData = json.loads(request.body)
                    CustomerSearch = responseData['Customer']
                    ProjectSearch = responseData['Project']


                    del_dic_IssueBreakdown = {'Customer': CustomerSearch, 'Project': ProjectSearch}
                    # print(dic_Project)

                    if IssuesBreakdown.objects.filter(**del_dic_IssueBreakdown):
                        # print(1)
                        IssuesBreakdown.objects.filter(**del_dic_IssueBreakdown).delete()

                if 'ExcelData' in str(request.body):

                    responseData = json.loads(request.body)
                    # print(responseData['historyYear'],type(responseData['historyYear']))
                    CustomerSearch = responseData['Customer']
                    ProjectSearch = responseData['Project']

                    xlsxlist = json.loads(responseData['ExcelData'])
                    # 验证，先验证再上传,必须要先验证，如果边验证边上传，一旦报错，下次再传就无法通过同机种验证
                    Check_dic_Project = {'Customer': CustomerSearch, 'Project': ProjectSearch, }
                    # print(Check_dic_ProjectCQM)
                    Projectinfo = CQMProject.objects.filter(**Check_dic_Project).first()
                    # print(Projectinfo)
                    current_user = request.session.get('user_name')
                    if Projectinfo:
                        for k in Projectinfo.Owner.all():
                            # print(k.username,current_user)
                            # print(type(k.username),type(current_user))
                            if k.username == current_user:
                                canEdit = 1
                                break
                    if canEdit:
                        rownum = 0
                        startupload = 0
                        # print(xlsxlist)
                        create_list = []
                        for i in xlsxlist:
                            # print(type(i),i)
                            rownum += 1
                            modeldata = {}
                            for key, value in i.items():
                                if key in headermodel_IssuesBreakdown.keys():
                                    modeldata[headermodel_IssuesBreakdown[key]] = value
                            # print(modeldata)
                            if 'Project' in modeldata.keys():
                                startupload = 1
                            else:
                                # canEdit = 0
                                startupload = 0
                                err_ok = 2
                                err_msg = """
                                        第"%s"條數據，Project不能爲空
                                                            """ % rownum
                                break
                            if 'FFRT_Entry_unclose_issue' in modeldata.keys():
                                startupload = 1
                            else:
                                # canEdit = 0
                                startupload = 0
                                err_ok = 2
                                err_msg = """
                                        第"%s"條數據，FFRT_Entry_unclose_issue不能爲空
                                                            """ % rownum
                                break
                            if 'SIT_Exit_unclose_issue' in modeldata.keys():
                                startupload = 1
                            else:
                                # canEdit = 0
                                startupload = 0
                                err_ok = 2
                                err_msg = """
                                        第"%s"條數據，SIT_Exit_unclose_issue不能爲空
                                                            """ % rownum
                                break
                            if 'issue_def' in modeldata.keys():
                                startupload = 1
                            else:
                                # canEdit = 0
                                startupload = 0
                                err_ok = 2
                                err_msg = """
                                        第"%s"條數據，分類不能爲空
                                                            """ % rownum
                                break
                            if 'FFRT' in modeldata.keys():
                                startupload = 1
                            else:
                                # canEdit = 0
                                startupload = 0
                                err_ok = 2
                                err_msg = """
                                        第"%s"條數據，FFRT不能爲空
                                                            """ % rownum
                                break
                            if 'Create_date' in modeldata.keys() or 'Update_date' in modeldata.keys():
                                try:
                                    # 将字符串转换为日期对象
                                    date = datetime.datetime.strptime(modeldata['Create_date'], '%Y-%m-%d')
                                    # return True
                                    startupload = 1
                                except ValueError:
                                    # return False
                                    startupload = 0
                                    err_ok = 2
                                    err_msg = """
                                                                                                        第"%s"條數據，Create_date日期格式不对（YYYY-MM-DD）
                                                                                                                            """ % rownum
                                    break
                            else:
                                # canEdit = 0
                                startupload = 0
                                err_ok = 2
                                err_msg = """
                                        第"%s"條數據，Create_date不能爲空
                                                            """ % rownum
                                break
                            if 'Update_date' in modeldata.keys():
                                try:
                                    # 将字符串转换为日期对象
                                    date = datetime.datetime.strptime(modeldata['Update_date'], '%Y-%m-%d')
                                    # return True
                                    startupload = 1
                                except ValueError:
                                    # return False
                                    startupload = 0
                                    err_ok = 2
                                    err_msg = """
                                                                        第"%s"條數據，Update_date日期格式不对（YYYY-MM-DD）
                                                                                            """ % rownum
                                    break
                            create_list.append(modeldata)

                        if startupload:
                            try:
                                with transaction.atomic():
                                    IssuesBreakdown.objects.bulk_create(create_list)
                                    update_list = []
                            except Exception as e:
                                # alert = '此数据正被其他使用者编辑中...'
                                alert = str(e)


                    #mock_data
                    for i in IssuesBreakdown.objects.filter(**Check_dic_Project):
                        mock_data.append(
                            {
                                "id": i.id, "Customer": i.Customer, "Project": i.Project,
                             "FFRT_Entry_unclose_issue": i.FFRT_Entry_unclose_issue,
                             "SIT_Exit_unclose_issue": i.SIT_Exit_unclose_issue,
                             "first_FFRT": i.first_FFRT,
                             "second_FFRT": i.second_FFRT,
                             "third_FFRT": i.third_FFRT,
                             "fourth_FFRT": i.fourth_FFRT,
                             "fifth_FFRT": i.fifth_FFRT,
                             "sixth_FFRT": i.sixth_FFRT,
                             "issue_def": i.issue_def,
                             "Remark": i.Remark,
                             "FFRT": i.FFRT,
                             "Defect_ID": i.Defect_ID,
                             "Title": i.Title,
                             "Create_date": str(i.Create_date) if i.Create_date else '',
                             "Update_date": str(i.Update_date) if i.Update_date else '',
                             "Status": i.Status, "Severity": i.Severity,
                             "Category": i.Category,
                             "Component": i.Component,
                             "BIOS_KBC": i.BIOS_KBC,
                             "Comments": i.Comments,
                             "Author": i.Author, "Assign_to": i.Assign_to, "Description": i.Description,
                             "Reproduce_steps": i.Reproduce_steps,
                             "Age": i.Age
                             }
                        )
        editpermission = editPpriority
        data = {
            "errMsg": errMsg,
            "ProjectCodeOption": ProjectCodeOption,
            "content": mock_data,
            "uploadpermission": uploadpermission,
            "editpermission": editpermission,
        }
        # print(data)
        return HttpResponse(json.dumps(data), content_type="application/json")
    return render(request, 'IssuesBreakdown/IssuesBreakdown_Edit.html', locals())

def IssuesBreakdown_Summary(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    Skin = request.COOKIES.get('Skin_raw')
    # print(Skin)
    if not Skin:
        Skin = "/static/src/blue.jpg"
    weizhi = "DDIS/IssuesBreakdown_edit"
    ProjectCodeOption = {
        # "C38(NB)": [{"Projectcode": "ILYE3"},
        #             {"Projectcode": "JLV31"},
        #             {"Projectcode": "FLV34"},
        #             {"Projectcode": "GLSM1"}],
        # "C38(AIO)": [{"Projectcode": "ILYE3"},
        #              {"Projectcode": "JLV31"},
        #              {"Projectcode": "FLV34"},
        #              {"Projectcode": "GLSM1"}],
        # "C85": [{"Projectcode": "ILYE3"},
        #         {"Projectcode": "JLV31"},
        #         {"Projectcode": "FLV34"},
        #         {"Projectcode": "GLSM1"}],
        # "T88(AIO)": [{"Projectcode": "ILYE3"},
        #              {"Projectcode": "JLV31"},
        #              {"Projectcode": "FLV34"},
        #              {"Projectcode": "GLSM1"}],
    }


    mock_data = [
        # {"id": 1, "Customer": "C38(NB)", "ProjectcodeCompal": "ILYE3", "ProjectcodeCustomer": "Y580S-16IRH",
        #  "Lowlight_item": "Thermal and power setting frozen too late", "Root_cause": "For EOY10 SDV phase test",
        #  "LD": "Jazz_Lin", "Owner": "", "Mitigation_plan": "",
        #  },
        # {"id": 2, "Customer": "C38(NB)", "ProjectcodeCompal": "ILYE3", "ProjectcodeCustomer": "Y580S-16IRH",
        #  "Lowlight_item": "Thermal and power setting frozen too late", "Root_cause": "For EOY10 SDV phase test",
        #  "LD": "Jazz_Lin", "Owner": "", "Mitigation_plan": "",
        #  },
    ]

    errMsg = ''

    uploadpermission = 0  # 1:能编辑 0:不能编辑


    roles = []
    onlineuser = request.session.get('account')
    # print(UserInfo.objects.get(account=onlineuser))
    for i in UserInfo.objects.get(account=onlineuser).role.all():
        roles.append(i.name)
    # print(roles)
    editPpriority = 0
    for i in roles:
        if 'DQA_SW' in i or 'admin' == i:
            editPpriority = 1
        elif 'LD' in i:
            if editPpriority != 1:
                editPpriority = 2
        elif 'RD' in i:
            if editPpriority != 1 and editPpriority != 2:
                editPpriority = 3


    # print(request.POST)
    # print(request.body)
    if request.method == "POST":
        if request.POST.get('isGetData') == 'first':
            pass

        if request.POST.get('isGetData') == 'SEARCH':
            pass
        if request.POST.get('action') == 'onSubmit':
            pass
        editpermission = editPpriority
        data = {
            "errMsg": errMsg,
            "ProjectCodeOption": ProjectCodeOption,
            "content": mock_data,
            "uploadpermission": uploadpermission,
            "editpermission": editpermission,
        }
        # print(data)
        return HttpResponse(json.dumps(data), content_type="application/json")
    return render(request, 'IssuesBreakdown/IssuesBreakdown_Summary.html', locals())