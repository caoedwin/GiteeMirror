from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import datetime, os
from django.http import HttpResponse
import datetime, json, simplejson
from .models import ProjectPlan
from CQM.models import CQMProject
from app01.models import UserInfo, ProjectinfoinDCT, Role
from django.db import transaction
from django.forms.models import model_to_dict

# Create your views here.
headermodel_ProjectPlan = {
    'Year': 'Year', 'DataType': 'DataType', 'CG': 'CG',
    'Compal Model': 'Compal_Model', 'Customer Model': 'Customer_Model',
    """Marketing type
(Commercial / Consumer)""": 'Marketing_type',
    """Status:
Planning  =P
Executing=E""": 'Status', 'Customer': 'Customer',
    """Product Type
(NB/PAD/AIO/IPC)""": 'Product_Type', 'Jan': 'Jan', 'Feb': 'Feb', 'Mar': 'Mar', 'Apr': 'Apr', 'May': 'May', 'Jun': 'Jun', 'Jul': 'Jul', 'Aug': 'Aug', 'Sep': 'Sep',
'Oct': 'Oct', 'Nov': 'Nov',  'Dec': 'Dec',
}


@csrf_exempt
def ProjectComparison_Edit(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    Skin = request.COOKIES.get('Skin_raw')
    # print(Skin)
    if not Skin:
        Skin = "/static/src/blue.jpg"
    weizhi = "DDIS/ProjectComparison_edit"
    mock_data = [
        # {"id": 1, "Project": "FLMA0", "FFRT_Entry_unclose_issue": "67", "SIT_Exit_unclose_issue": "41",
        #  "first_FFRT": "2023-12-05~2023-12-18", "second_FFRT": "2023-12-19~2023-12-25",
        #  "third_FFRT": "2023-12-19~2023-12-25", "fourth_FFRT": "", "fifth_FFRT": "",
        #  "sixth_FFRT": "", "issue_def": "New found_Unidentified", "Remark": "Copilot PCR new feature issue",
        #  "FFRT": "FFRT1", "Defect_ID": "398743",
        #  "Title": "[S590-14&16IRU_SIT_UMA] Copilot PCR, Press Right Ctrl(Copilot Key) to launch Copilot window, then enter/resume MS/S4 or launch other windows, close Copilot window need press twice Right Ctrl (F/R: 2/2u, 4/4c)",
        #  "Create_date": "2023-12-20", "Update_date": "2023-12-25", "Status": "Postpone",
        #  "Severity": "3", "Category": "OS", "Component": "OS",
        #  "BIOS_KBC": "PFCN08WW", "Comments": "", "Author": "Vickie_Wang@compal.com",
        #  "Assign_to": "liulan4", "Description": "Test configuration: Image: V8"
        #                                         "OS: Win11 23H2 build 22631.2715"
        #                                         "Driver: V1.00"
        #                                         "BIOS/EC: PFCN08WW/PFEC08WW, 2023/12/14"
        #                                         "Edge: V120.0.2210.77"
        #                                         "Detect by:"
        #                                         "Ad-hoc"
        #                                         "Fail scope:"
        #                                         "Tested unit: 2units(14-I7U16WFS05#38, 16-I5U08WFS02#02)"
        #                                         "Failed unit: 2units(14-I7U16WFS05#38, 16-I5U08WFS02#02)"
        #                                         "F/R: 2/2u, 4/4c"
        #                                         "Observed symptom:"
        #                                         "Press Right Ctrl(Copilot Key) to launch Copilot window, then enter/resume MS/S4 or launch other windows, close Copilot window need press twice Right Ctrl"
        #                                         "Error code/ message:"
        #                                         "None"
        #                                         "Expected behavior:"
        #                                         "Press Right Ctrl(Copilot Key) to launch Copilot window, then enter/resume MS/S4 or launch other windows, close Copilot window need press once Right Ctrl."
        #                                         "How to recover:"
        #                                         "None.",
        #  "Reproduce_steps": "",
        #  "Age": "4",
        #
        #  },
        # {"id": 2, "Project": "FLMA0", "FFRT_Entry_unclose_issue": "67", "SIT_Exit_unclose_issue": "41",
        #  "first_FFRT": "2023-12-05~2023-12-18", "second_FFRT": "2023-12-19~2023-12-25",
        #  "third_FFRT": "2023-12-19~2023-12-25", "fourth_FFRT": "", "fifth_FFRT": "",
        #  "sixth_FFRT": "", "issue_def": "New found_Unidentified", "Remark": "Copilot PCR new feature issue",
        #  "FFRT": "FFRT1", "Defect_ID": "398744",
        #  "Title": "[S590-14&16IRU_SIT_UMA] Copilot PCR, Press Right Ctrl(Copilot Key) to launch Copilot window, then enter/resume MS/S4 or launch other windows, close Copilot window need press twice Right Ctrl (F/R: 2/2u, 4/4c)",
        #  "Create_date": "2023-12-20", "Update_date": "2023-12-25", "Status": "Postpone",
        #  "Severity": "3", "Category": "OS", "Component": "OS",
        #  "BIOS_KBC": "PFCN08WW", "Comments": "", "Author": "Vickie_Wang@compal.com",
        #  "Assign_to": "liulan4", "Description": "Test configuration: Image: V8"
        #                                         "OS: Win11 23H2 build 22631.2715"
        #                                         "Driver: V1.00"
        #                                         "BIOS/EC: PFCN08WW/PFEC08WW, 2023/12/14"
        #                                         "Edge: V120.0.2210.77"
        #                                         "Detect by:"
        #                                         "Ad-hoc"
        #                                         "Fail scope:"
        #                                         "Tested unit: 2units(14-I7U16WFS05#38, 16-I5U08WFS02#02)"
        #                                         "Failed unit: 2units(14-I7U16WFS05#38, 16-I5U08WFS02#02)"
        #                                         "F/R: 2/2u, 4/4c"
        #                                         "Observed symptom:"
        #                                         "Press Right Ctrl(Copilot Key) to launch Copilot window, then enter/resume MS/S4 or launch other windows, close Copilot window need press twice Right Ctrl"
        #                                         "Error code/ message:"
        #                                         "None"
        #                                         "Expected behavior:"
        #                                         "Press Right Ctrl(Copilot Key) to launch Copilot window, then enter/resume MS/S4 or launch other windows, close Copilot window need press once Right Ctrl."
        #                                         "How to recover:"
        #                                         "None.",
        #  "Reproduce_steps": "",
        #  "Age": "4",
        #
        #  },
        # {"id": 3, "Project": "FLMA0", "FFRT_Entry_unclose_issue": "67", "SIT_Exit_unclose_issue": "41",
        #  "first_FFRT": "2023-12-05~2023-12-18", "second_FFRT": "2023-12-19~2023-12-25",
        #  "third_FFRT": "2023-12-19~2023-12-25", "fourth_FFRT": "", "fifth_FFRT": "",
        #  "sixth_FFRT": "", "issue_def": "New found_Unidentified", "Remark": "Copilot PCR new feature issue",
        #  "FFRT": "FFRT1", "Defect_ID": "398745",
        #  "Title": "[S590-14&16IRU_SIT_UMA] Copilot PCR, Press Right Ctrl(Copilot Key) to launch Copilot window, then enter/resume MS/S4 or launch other windows, close Copilot window need press twice Right Ctrl (F/R: 2/2u, 4/4c)",
        #  "Create_date": "2023-12-20", "Update_date": "2023-12-25", "Status": "Postpone",
        #  "Severity": "3", "Category": "OS", "Component": "OS",
        #  "BIOS_KBC": "PFCN08WW", "Comments": "", "Author": "Vickie_Wang@compal.com",
        #  "Assign_to": "liulan4", "Description": "Test configuration: Image: V8"
        #                                         "OS: Win11 23H2 build 22631.2715"
        #                                         "Driver: V1.00"
        #                                         "BIOS/EC: PFCN08WW/PFEC08WW, 2023/12/14"
        #                                         "Edge: V120.0.2210.77"
        #                                         "Detect by:"
        #                                         "Ad-hoc"
        #                                         "Fail scope:"
        #                                         "Tested unit: 2units(14-I7U16WFS05#38, 16-I5U08WFS02#02)"
        #                                         "Failed unit: 2units(14-I7U16WFS05#38, 16-I5U08WFS02#02)"
        #                                         "F/R: 2/2u, 4/4c"
        #                                         "Observed symptom:"
        #                                         "Press Right Ctrl(Copilot Key) to launch Copilot window, then enter/resume MS/S4 or launch other windows, close Copilot window need press twice Right Ctrl"
        #                                         "Error code/ message:"
        #                                         "None"
        #                                         "Expected behavior:"
        #                                         "Press Right Ctrl(Copilot Key) to launch Copilot window, then enter/resume MS/S4 or launch other windows, close Copilot window need press once Right Ctrl."
        #                                         "How to recover:"
        #                                         "None.",
        #  "Reproduce_steps": "",
        #  "Age": "4",

        # },
    ]

    errMsg = ''

    deletepermission = 0  # 1:能删除

    err_msg = ''

    canEdit = 0  # 1:能编辑 0:不能编辑

    # roles = []
    # onlineuser = request.session.get('account')
    # # print(UserInfo.objects.get(account=onlineuser))
    # for i in UserInfo.objects.get(account=onlineuser).role.all():
    #     roles.append(i.name)
    # # print(roles)
    # editPpriority = 0
    # for i in roles:
    #     if 'DQA_SW' in i or 'admin' == i:
    #         editPpriority = 1
    #     elif 'LD' in i:
    #         if editPpriority != 1:
    #             editPpriority = 2
    #     elif 'RD' in i:
    #         if editPpriority != 1 and editPpriority != 2:
    #             editPpriority = 3

    print(request.POST)
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
                    pass

                if 'upload' in str(request.body):

                    responseData = json.loads(request.body)
                    # print(responseData['historyYear'],type(responseData['historyYear']))
                    YearSearch = responseData['Year']
                    DataTypeSearch = responseData['DataType']

                    xlsxlist = json.loads(responseData['ExcelData'])
                    # print(xlsxlist)
                    # 验证，先验证再上传,必须要先验证，如果边验证边上传，一旦报错，下次再传就无法通过同机种验证
                    # Check_dic_Project = {'Customer': CustomerSearch, 'Project': ProjectSearch, }
                    # # print(Check_dic_ProjectCQM)
                    # Projectinfo = CQMProject.objects.filter(**Check_dic_Project).first()
                    # print(Projectinfo)
                    # current_user = request.session.get('user_name')
                    current_account = request.session.get('account')
                    ProjectComparison_admin_user = "0301507" #Canny
                    # if Projectinfo:s
                    #                     #     for k in Projectinfo.Owner.all():
                    #                     #         # print(k.username,current_user)
                    #                     #         # print(type(k.username),type(current_user))
                    #                     #         if k.username == current_uer:
                    #             canEdit = 1
                    #             break
                    if current_account == ProjectComparison_admin_user:
                        canEdit = 1
                    # print(canEdit)
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
                                if key in headermodel_ProjectPlan.keys():
                                    # print(headermodel_ProjectPlan[key],value)
                                    modeldata[headermodel_ProjectPlan[key]] = value
                            # print(modeldata)

                            if 'Year' in modeldata.keys():
                                startupload = 1
                            else:
                                # canEdit = 0
                                startupload = 0
                                err_msg = """
                                        第"%s"條數據，Year不能爲空
                                                            """ % rownum
                                break
                            if 'DataType' in modeldata.keys():
                                startupload = 1
                            else:
                                # canEdit = 0
                                startupload = 0
                                err_msg = """
                                        第"%s"條數據，DataType不能爲空
                                                            """ % rownum
                                break
                            if 'CG' in modeldata.keys():
                                startupload = 1
                            else:
                                # canEdit = 0
                                startupload = 0
                                err_msg = """
                                        第"%s"條數據，CG不能爲空
                                                            """ % rownum
                                break
                            if 'Compal_Model' in modeldata.keys():
                                startupload = 1
                            else:
                                # canEdit = 0
                                startupload = 0
                                err_msg = """
                                        第"%s"條數據，Compal_Model不能爲空
                                                            """ % rownum
                                break
                            if 'Customer_Model' in modeldata.keys():
                                startupload = 1
                            else:
                                # canEdit = 0
                                startupload = 0
                                err_msg = """
                                        第"%s"條數據，Customer_Model不能爲空
                                                            """ % rownum
                                break
                            if 'Marketing_type' in modeldata.keys():
                                startupload = 1
                            else:
                                # canEdit = 0
                                startupload = 0
                                err_msg = """
                                        第"%s"條數據，Marketing_type不能爲空
                                                            """ % rownum
                                break
                            if 'Status' in modeldata.keys():
                                startupload = 1
                            else:
                                # canEdit = 0
                                startupload = 0
                                err_msg = """
                                        第"%s"條數據，Status不能爲空
                                                            """ % rownum
                                break
                            if 'Customer' in modeldata.keys():
                                startupload = 1
                            else:
                                # canEdit = 0
                                startupload = 0
                                err_msg = """
                                        第"%s"條數據，Customer不能爲空
                                                            """ % rownum
                                break
                            if 'Product_Type' in modeldata.keys():
                                startupload = 1
                            else:
                                # canEdit = 0
                                startupload = 0
                                err_msg = """
                                        第"%s"條數據，Product_Type不能爲空
                                                            """ % rownum
                                break

                            create_list.append(ProjectPlan(**modeldata))  # object(**dict)
                        # print(err_msg, startupload)
                        # print(create_list,)
                        if startupload:
                            try:
                                with transaction.atomic():
                                    ProjectPlan.objects.bulk_create(create_list)
                                    update_list = []
                            except Exception as e:
                                # alert = '此数据正被其他使用者编辑中...'
                                alert = str(e)
                                print(alert)

                    # print('IssuesBreakdown')
                    # mock_data
                    Check_dic_ProjectPlan = {"Year": YearSearch, "DataType": DataTypeSearch}
                    for i in ProjectPlan.objects.filter(**Check_dic_ProjectPlan):
                        # print(i)
                        mock_data.append(
                            {
                                "id": i.id, "Year": i.Year, "DataType": i.DataType,
                                "CG": i.CG,
                                "Compal_Model": i.Compal_Model,
                                "Customer_Model": i.Customer_Model,
                                "Marketing_type": i.Marketing_type,
                                "Status": i.Status,
                                "Customer": i.Customer,
                                "Product_Type": i.Product_Type,
                                "Jan": i.Jan,
                                "Feb": i.Feb,
                                "Mar": i.Mar,
                                "Apr": i.Apr,
                                "May": i.May,
                                "Jun": i.Jun,
                                "Jul": i.Jul,
                                "Aug": i.Aug,
                                "Sep": i.Sep,
                                "Oct": i.Oct,
                                "Nov": i.Nov,
                                "Dec": i.Dec,
                            }
                        )
        data = {
            "errMsg": err_msg,
            "content": mock_data,
            "permission": canEdit,

        }
        # print(data)
        return HttpResponse(json.dumps(data), content_type="application/json")
    return render(request, 'ProjectComparison/ProjectComparison_Edit.html', locals())


@csrf_exempt
def ProjectComparison_Summary(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    Skin = request.COOKIES.get('Skin_raw')
    # print(Skin)
    if not Skin:
        Skin = "/static/src/blue.jpg"
    weizhi = "DDIS/ProjectComparison_Summary"


    if request.method == "POST":
        if request.POST.get('isGetData') == 'first':
            pass
        if request.POST.get('isGetData') == 'SEARCH':
            pass
        data = {
        }
        # print(data)
        return HttpResponse(json.dumps(data), content_type="application/json")
    return render(request, 'ProjectComparison/ProjectComparison_Summary.html', locals())
