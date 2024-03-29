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
    "Marketing type\r\n(Commercial / Consumer)": 'Marketing_type',
    """Status:\r\nPlanning  =P\r\nExecuting=E""": 'Status', 'Customer': 'Customer',
    """Product Type\r\n(NB/PAD/AIO/IPC)""": 'Product_Type', 'Jan': 'Jan', 'Feb': 'Feb', 'Mar': 'Mar', 'Apr': 'Apr',
    'May': 'May', 'Jun': 'Jun', 'Jul': 'Jul', 'Aug': 'Aug', 'Sep': 'Sep',
    'Oct': 'Oct', 'Nov': 'Nov', 'Dec': 'Dec',
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
    weizhi = "PersonalInfo/PersonalInfo_edit"

    yearOptions = [
        # "2020", "2021", "2023"
    ]
    for i in ProjectPlan.objects.all().values("Year").distinct().order_by("Year"):
        yearOptions.append(i["Year"])

    datatypeOption = [
        # "Acutal", "w/o OOC", "with OOC"
    ]
    for i in ProjectPlan.objects.all().values("DataType").distinct().order_by("DataType"):
        datatypeOption.append(i["DataType"])

    mock_data = [
        # {"id": "1", "Year": "2024", "DataType": "Acutal", "CG": "CG13", "Compal_Model": "ILVR4",
        #  "Customer_Model": "S590 14Intel MTL H28(Plastic/Metal)",
        #  "Marketing_type": "SMB/Commercial", "Status": "E", "Customer": "C38", "Product_Type": "NB", "Jan": "OOC",
        #  "Feb": "SIT",
        #  "Mar": "", "Apr": "", "May": "", "Jun": "", "July": "", "Aug": "", "Sep": "", "Oct": "", "Nov": "", "Dec": ""},
        # {"id": "2", "Year": "2024", "DataType": "Acutal", "CG": "CG13", "Compal_Model": "ILVR4",
        #  "Customer_Model": "S590 14Intel MTL H28(Plastic/Metal)",
        #  "Marketing_type": "SMB/Commercial", "Status": "E", "Customer": "C38", "Product_Type": "NB", "Jan": "OOC",
        #  "Feb": "SIT",
        #  "Mar": "", "Apr": "", "May": "", "Jun": "", "July": "", "Aug": "", "Sep": "", "Oct": "", "Nov": "", "Dec": ""},
        # {"id": "3", "Year": "2024", "DataType": "Acutal", "CG": "CG13", "Compal_Model": "ILVR4",
        #  "Customer_Model": "S590 14Intel MTL H28(Plastic/Metal)",
        #  "Marketing_type": "SMB/Commercial", "Status": "E", "Customer": "C38", "Product_Type": "NB", "Jan": "OOC",
        #  "Feb": "SIT",
        #  "Mar": "", "Apr": "", "May": "", "Jun": "", "July": "", "Aug": "", "Sep": "", "Oct": "", "Nov": "", "Dec": ""}
    ]

    errMsg = ''

    permission = 0  # 1:有權限
    roles = []
    onlineuser = request.session.get('account')
    # onlineuser = '0502413'
    onlineuserDepartment = ''
    # print(onlineuser,UserInfo.objects.get(account=onlineuser))
    if UserInfo.objects.filter(account=onlineuser).first():
        for i in UserInfo.objects.filter(account=onlineuser).first().role.all():
            roles.append(i.name)
    for i in roles:
        if 'admin' in i or 'DQA_LNV_ProjectCom_admin' in i:
            permission = 1
    # print(request.POST)
    # print(request.body)
    if request.method == "POST":
        if request.POST.get('isGetData') == 'first':
            pass

        if request.POST.get('isGetData') == 'SEARCH':
            # mock_data
            Check_dic_ProjectPlan = {}
            YearSearch = request.POST.get('Year')
            DataTypeSearch = request.POST.get('DataType')
            if YearSearch:
                Check_dic_ProjectPlan["Year"] = YearSearch
            if DataTypeSearch:
                Check_dic_ProjectPlan["DataType"] = DataTypeSearch
            # print(Check_dic_ProjectPlan)
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
                        "Jan": i.Jan if i.Jan != None else '',
                        "Feb": i.Feb if i.Feb != None else '',
                        "Mar": i.Mar if i.Mar != None else '',
                        "Apr": i.Apr if i.Apr != None else '',
                        "May": i.May if i.May != None else '',
                        "Jun": i.Jun if i.Jun != None else '',
                        "July": i.Jul if i.Jul != None else '',
                        "Aug": i.Aug if i.Aug != None else '',
                        "Sep": i.Sep if i.Sep != None else '',
                        "Oct": i.Oct if i.Oct != None else '',
                        "Nov": i.Nov if i.Nov != None else '',
                        "Dec": i.Dec if i.Dec != None else '',
                    }
                )
        elif request.POST.get('action') == 'onSubmit':
            ID = request.POST.get('ID')
            Year = request.POST.get('Year')
            DataType = request.POST.get('DataType')
            CG = request.POST.get('CG')
            Compal_Model = request.POST.get('Compal_Model')
            Customer_Model = request.POST.get('Customer_Model')
            Marketing_type = request.POST.get('Marketing_type')
            Status = request.POST.get('Status')
            Customer = request.POST.get('Customer')
            Product_Type = request.POST.get('Product_Type')
            Jan = request.POST.get('Jan')
            Feb = request.POST.get('Feb')
            Mar = request.POST.get('Mar')
            Apr = request.POST.get('Apr')
            May = request.POST.get('May')
            Jun = request.POST.get('Jun')
            Jul = request.POST.get('July')
            Aug = request.POST.get('Aug')
            Sep = request.POST.get('Sep')
            Oct = request.POST.get('Oct')
            Nov = request.POST.get('Nov')
            Dec = request.POST.get('Dec')
            update_dic = {
                "Year": Year, "DataType": DataType,
                "CG": CG,
                "Compal_Model": Compal_Model,
                "Customer_Model": Customer_Model,
                "Marketing_type": Marketing_type,
                "Status": Status,
                "Customer": Customer,
                "Product_Type": Product_Type,
                "Jan": Jan,
                "Feb": Feb,
                "Mar": Mar,
                "Apr": Apr,
                "May": May,
                "Jun": Jun,
                "Jul": Jul,
                "Aug": Aug,
                "Sep": Sep,
                "Oct": Oct,
                "Nov": Nov,
                "Dec": Dec,
            }
            try:
                with transaction.atomic():
                    ProjectPlan.objects.filter(id=ID).update(**update_dic)
            except Exception as e:
                # alert = '此数据正被其他使用者编辑中...'
                alert = str(e)
                print(alert)

            # mock_data
            Check_dic_ProjectPlan = {}
            YearSearch = request.POST.get('searchYear')
            DataTypeSearch = request.POST.get('searchDataType')
            if YearSearch:
                Check_dic_ProjectPlan["Year"] = YearSearch
            if DataTypeSearch:
                Check_dic_ProjectPlan["DataType"] = DataTypeSearch
            # print(Check_dic_ProjectPlan)
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
                        "Jan": i.Jan if i.Jan != None else '',
                        "Feb": i.Feb if i.Feb != None else '',
                        "Mar": i.Mar if i.Mar != None else '',
                        "Apr": i.Apr if i.Apr != None else '',
                        "May": i.May if i.May != None else '',
                        "Jun": i.Jun if i.Jun != None else '',
                        "July": i.Jul if i.Jul != None else '',
                        "Aug": i.Aug if i.Aug != None else '',
                        "Sep": i.Sep if i.Sep != None else '',
                        "Oct": i.Oct if i.Oct != None else '',
                        "Nov": i.Nov if i.Nov != None else '',
                        "Dec": i.Dec if i.Dec != None else '',
                    }
                )
        else:
            try:
                request.body
            except:
                pass
            else:
                if 'MUTIDELETE' in str(request.body):
                    responseData = json.loads(request.body)
                    # for i in responseData['params']:
                    #     ProjectPlan.objects.get(id=i).delete()
                    try:
                        with transaction.atomic():
                            ProjectPlan.objects.filter(id__in=responseData['params']).delete()
                    except Exception as e:
                        # alert = '此数据正被其他使用者编辑中...'
                        alert = str(e)
                        print(alert)
                    # mock_data
                    yearOptions = [
                        # "2020", "2021", "2023"
                    ]
                    for i in ProjectPlan.objects.all().values("Year").distinct().order_by("Year"):
                        yearOptions.append(i["Year"])

                    datatypeOption = [
                        # "Acutal", "w/o OOC", "with OOC"
                    ]
                    for i in ProjectPlan.objects.all().values("DataType").distinct().order_by("DataType"):
                        datatypeOption.append(i["DataType"])
                    Check_dic_ProjectPlan = {}
                    YearSearch = request.POST.get('Year')
                    DataTypeSearch = request.POST.get('DataType')
                    if YearSearch:
                        Check_dic_ProjectPlan["Year"] = YearSearch
                    if DataTypeSearch:
                        Check_dic_ProjectPlan["DataType"] = DataTypeSearch
                    # print(Check_dic_ProjectPlan)
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
                                "Jan": i.Jan if i.Jan != None else '',
                                "Feb": i.Feb if i.Feb != None else '',
                                "Mar": i.Mar if i.Mar != None else '',
                                "Apr": i.Apr if i.Apr != None else '',
                                "May": i.May if i.May != None else '',
                                "Jun": i.Jun if i.Jun != None else '',
                                "July": i.Jul if i.Jul != None else '',
                                "Aug": i.Aug if i.Aug != None else '',
                                "Sep": i.Sep if i.Sep != None else '',
                                "Oct": i.Oct if i.Oct != None else '',
                                "Nov": i.Nov if i.Nov != None else '',
                                "Dec": i.Dec if i.Dec != None else '',
                            }
                        )

                elif 'upload' in str(request.body):

                    responseData = json.loads(request.body)
                    # print(responseData['historyYear'],type(responseData['historyYear']))
                    YearSearch = responseData['Year']
                    YearSearch_backup = ''
                    DataTypeSearch = responseData['DataType']

                    xlsxlist = json.loads(responseData['ExcelData'])
                    # print(xlsxlist)
                    # 验证，先验证再上传,必须要先验证，如果边验证边上传，一旦报错，下次再传就无法通过同机种验证
                    # Check_dic_Project = {'Customer': CustomerSearch, 'Project': ProjectSearch, }
                    # # print(Check_dic_ProjectCQM)
                    # Projectinfo = CQMProject.objects.filter(**Check_dic_Project).first()
                    # print(Projectinfo)
                    # current_user = request.session.get('user_name')
                    # current_account = request.session.get('account')
                    # ProjectComparison_admin_user = "0301507" #Canny
                    # # if Projectinfo:s
                    # #                     #     for k in Projectinfo.Owner.all():
                    # #                     #         # print(k.username,current_user)
                    # #                     #         # print(type(k.username),type(current_user))
                    # #                     #         if k.username == current_uer:
                    # #             canEdit = 1
                    # #             break
                    # if current_account == ProjectComparison_admin_user:
                    #     canEdit = 1
                    # print(canEdit)
                    # try:
                    if permission:
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
                            if rownum == 1:
                                YearSearch_backup = modeldata['Year']
                                # print(modeldata['Year'])
                        # print(err_msg, startupload)
                        # print(create_list,)
                        # print(startupload)
                        # print(rownum, type(rownum))
                        if startupload:
                            try:
                                with transaction.atomic():
                                    ProjectPlan.objects.bulk_create(create_list)
                            except Exception as e:
                                # alert = '此数据正被其他使用者编辑中...'
                                alert = str(e)
                                print(alert)

                    # print('IssuesBreakdown')
                    # mock_data
                    yearOptions = [
                        # "2020", "2021", "2023"
                    ]
                    for i in ProjectPlan.objects.all().values("Year").distinct().order_by("Year"):
                        yearOptions.append(i["Year"])

                    datatypeOption = [
                        # "Acutal", "w/o OOC", "with OOC"
                    ]
                    for i in ProjectPlan.objects.all().values("DataType").distinct().order_by("DataType"):
                        datatypeOption.append(i["DataType"])
                    Check_dic_ProjectPlan = {}
                    if YearSearch:
                        Check_dic_ProjectPlan["Year"] = YearSearch
                    elif YearSearch_backup:
                        Check_dic_ProjectPlan["Year"] = YearSearch_backup
                    if DataTypeSearch:
                        Check_dic_ProjectPlan["DataType"] = DataTypeSearch
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
                                "Jan": i.Jan if i.Jan != None else '',
                                "Feb": i.Feb if i.Feb != None else '',
                                "Mar": i.Mar if i.Mar != None else '',
                                "Apr": i.Apr if i.Apr != None else '',
                                "May": i.May if i.May != None else '',
                                "Jun": i.Jun if i.Jun != None else '',
                                "July": i.Jul if i.Jul != None else '',
                                "Aug": i.Aug if i.Aug != None else '',
                                "Sep": i.Sep if i.Sep != None else '',
                                "Oct": i.Oct if i.Oct != None else '',
                                "Nov": i.Nov if i.Nov != None else '',
                                "Dec": i.Dec if i.Dec != None else '',
                            }
                        )
                    # except Exception as e:
                    #     err_msg = str(e)

        data = {
            "errMsg": errMsg,
            "yearOptions": yearOptions,
            "datatypeOption": datatypeOption,
            "content": mock_data,
            "permission": permission,

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
