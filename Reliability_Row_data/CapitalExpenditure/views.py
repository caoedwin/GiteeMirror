from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import datetime, os
from django.http import HttpResponse
import datetime, json, simplejson, pprint
from .models import CapitalExpenditure
from CQM.models import CQMProject
from app01.models import UserInfo, ProjectinfoinDCT, Role
from django.db import transaction
from django.forms.models import model_to_dict

# Create your views here.
headermodel_CapitalExpenditure = {'PlanYear': 'PlanYear',
  '客戶別': 'Customer',
  '預算編號': 'BudgetCode',
  '投資性質': 'Investment_Nature',
  '屬性代碼': 'Attribute_Code',
  '申請部門': 'Application_Department',
  '設備或工程名稱': 'Device_Name',
  '用途說明': 'Usage_Description',
  '廠牌規格': 'Specifications',
  '驗收月份': 'Acceptance_Month',
  '預算數量': 'Budget_Quantity',
  '預估總價': 'Estimated_Original_Currency',
  '__EMPTY': 'Estimated_Original_Price',
  '折合人民幣': 'Equivalent_To_RMB',
  '付款條件': 'Payment_Terms',
  '折舊月數': 'Depreciation_Months',
  '會計科目': 'Accounting_Subjects',
  '是否自動化': 'Automated_Or_Not',
  'Project Code': 'Project_Code',
  '現狀說明': 'Current_Situation',
  '適用範圍': 'Applicable_Scope',
  '投資動機與目的': 'Investment_Purpose',
  '投資動機與目的其他說明': 'Investment_Purpose_Des',
  '潛在問題': 'Potential_Issues',
  '潛在問題的其他說明': 'Potential_Issues_Des',
  '年節省支出': 'Tighten_Expenses',
  '年增加收益': 'Annual_Increase_PerYear',
  '年投資效益': 'Investment_Benefits_PerYear',
  '年淨現金流入': 'Cash_Inflows_PerYear',
  '回收年限(月數)': 'Payback_Period',
  '申購狀況': 'Subscription_Status',
  '申購數量': 'Subscription_Quantity',
  '申購金額\r\n(CNY)': 'Subscription_Amount',
  '入賬金額\r\n(CNY)': 'Entry_Amount',
},



@csrf_exempt
def CapitalExpenditure_Summary(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    Skin = request.COOKIES.get('Skin_raw')
    # print(Skin)
    if not Skin:
        Skin = "/static/src/blue.jpg"
    weizhi = "DDIS/CapitalExpenditure_Summary"

    mock_data = [

    ]
    # 表格數據
    mock_data1 = [
        # {"id": 1, "Phase": "FVT", "Jan": 0, "Feb": 0, "Mar": 1, "Apr": 2, "May": 3, "Jun": 4,
        #  "July": 5, "Aug": 6, "Sep": 7, "Oct": 8, "Nov": 9, "Dec": 0},
        # {"id": 2, "Phase": "FVT", "Jan": 0, "Feb": 0, "Mar": 1, "Apr": 2, "May": 3, "Jun": 4,
        #  "July": 5, "Aug": 6, "Sep": 7, "Oct": 8, "Nov": 9, "Dec": 0},
        # {"id": 3, "Phase": "FVT", "Jan": 0, "Feb": 0, "Mar": 1, "Apr": 2, "May": 3, "Jun": 4,
        #  "July": 5, "Aug": 6, "Sep": 7, "Oct": 8, "Nov": 9, "Dec": 0},

    ]
    mock_data2 = [
        # {"id": 1, "Phase": "FVT", "Jan": 0, "Feb": 0, "Mar": 1, "Apr": 2, "May": 3, "Jun": 4,
        #  "July": 5, "Aug": 6, "Sep": 7, "Oct": 8, "Nov": 9, "Dec": 0},
        # {"id": 2, "Phase": "FVT", "Jan": 0, "Feb": 0, "Mar": 1, "Apr": 2, "May": 3, "Jun": 4,
        #  "July": 5, "Aug": 6, "Sep": 7, "Oct": 8, "Nov": 9, "Dec": 0},
        # {"id": 3, "Phase": "FVT", "Jan": 0, "Feb": 0, "Mar": 1, "Apr": 2, "May": 3, "Jun": 4,
        #  "July": 5, "Aug": 6, "Sep": 7, "Oct": 8, "Nov": 9, "Dec": 0},

    ]
    mock_data3 = [
        # {"id": 1, "Phase": "FVT", "Jan": 0, "Feb": 0, "Mar": 1, "Apr": 2, "May": 3, "Jun": 4,
        #  "July": 5, "Aug": 6, "Sep": 7, "Oct": 8, "Nov": 9, "Dec": 0},
        # {"id": 2, "Phase": "FVT", "Jan": 0, "Feb": 0, "Mar": 1, "Apr": 2, "May": 3, "Jun": 4,
        #  "July": 5, "Aug": 6, "Sep": 7, "Oct": 8, "Nov": 9, "Dec": 0},
        # {"id": 3, "Phase": "FVT", "Jan": 0, "Feb": 0, "Mar": 1, "Apr": 2, "May": 3, "Jun": 4,
        #  "July": 5, "Aug": 6, "Sep": 7, "Oct": 8, "Nov": 9, "Dec": 0},

    ]
    mock_data4 = [
        # {"id": 1, "Phase": "FVT", "Jan": 0, "Feb": 0, "Mar": 1, "Apr": 2, "May": 3, "Jun": 4,
        #  "July": 5, "Aug": 6, "Sep": 7, "Oct": 8, "Nov": 9, "Dec": 0},
        # {"id": 2, "Phase": "FVT", "Jan": 0, "Feb": 0, "Mar": 1, "Apr": 2, "May": 3, "Jun": 4,
        #  "July": 5, "Aug": 6, "Sep": 7, "Oct": 8, "Nov": 9, "Dec": 0},
        # {"id": 3, "Phase": "FVT", "Jan": 0, "Feb": 0, "Mar": 1, "Apr": 2, "May": 3, "Jun": 4,
        #  "July": 5, "Aug": 6, "Sep": 7, "Oct": 8, "Nov": 9, "Dec": 0},

    ]
    mock_data5 = []
    mock_data6 = []
    mock_data7 = []
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
        if 'admin' == i or 'DQA_LNV_CapitalExpenditure_admin' in i:
            permission = 1

    if request.method == "POST":
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
                    # for i in responseData['params']:
                    #     CapitalExpenditure.objects.get(id=i).delete()
                    try:
                        with transaction.atomic():
                            CapitalExpenditure.objects.filter(id__in=responseData['params']).delete()
                    except Exception as e:
                        # alert = '此数据正被其他使用者编辑中...'
                        alert = str(e)
                        print(alert)
                    # mock_data
                    yearOptions = [
                        # "2020", "2021", "2023"
                    ]
                    for i in CapitalExpenditure.objects.all().values("Year").distinct().order_by("Year"):
                        yearOptions.append(i["Year"])

                    datatypeOption = [
                        # "Actual", "w/o OOC", "with OOC"
                    ]
                    for i in CapitalExpenditure.objects.all().values("DataType").distinct().order_by("DataType"):
                        datatypeOption.append(i["DataType"])
                    Check_dic_CapitalExpenditure = {}
                    YearSearch = request.POST.get('Year')
                    DataTypeSearch = request.POST.get('DataType')
                    if YearSearch:
                        Check_dic_CapitalExpenditure["Year"] = YearSearch
                    if DataTypeSearch:
                        Check_dic_CapitalExpenditure["DataType"] = DataTypeSearch
                    # print(Check_dic_CapitalExpenditure)
                    for i in CapitalExpenditure.objects.filter(**Check_dic_CapitalExpenditure):
                        # print(i)
                        mock_data.append(
                            {
                                "id": i.id, "PlanYear": i.PlanYear, "Customer": i.Customer, "BudgetCode": i.BudgetCode, "Investment_Nature": i.Investment_Nature,
                                "Attribute_Code": i.Attribute_Code,
                                "Application_Department": i.Application_Department,
                                "Device_Name": i.Device_Name,
                                "Usage_Description": i.Usage_Description,
                                "Specifications": i.Specifications,
                                "Acceptance_Month": i.Acceptance_Month,
                                "Budget_Quantity": i.Budget_Quantity,
                                "Estimated_Original_Currency": i.Estimated_Original_Currency,
                                "Estimated_Original_Price": i.Estimated_Original_Price,
                                "Equivalent_To_RMB": i.Equivalent_To_RMB,
                                "Payment_Terms": i.Payment_Terms,
                                "Depreciation_Months": i.Depreciation_Months,
                                "Accounting_Subjects": i.Accounting_Subjects,
                                "Automated_Or_Not": i.Automated_Or_Not,
                                "Project_Code": i.Project_Code,
                                "Current_Situation": i.Current_Situation,
                                "Applicable_Scope": i.Applicable_Scope,
                                "Investment_Purpose": i.Investment_Purpose,
                                "Investment_Purpose_Des": i.Investment_Purpose_Des,
                                "Potential_Issues": i.Potential_Issues,
                                "Potential_Issues_Des": i.Potential_Issues_Des,
                                "Tighten_Expenses": i.Tighten_Expenses,
                                "Annual_Increase_PerYear": i.Annual_Increase_PerYear,
                                "Investment_Benefits_PerYear": i.Investment_Benefits_PerYear,
                                "Cash_Inflows_PerYear": i.Cash_Inflows_PerYear,
                                "Payback_Period": i.Payback_Period,
                                "Subscription_Status": i.Subscription_Status,
                                "Subscription_Quantity": i.Subscription_Quantity,
                                "Subscription_Amount": i.Subscription_Amount,
                                "Entry_Amount": i.Entry_Amount,
                            }
                        )

                elif 'upload' in str(request.body):

                    responseData = json.loads(request.body)
                    # print(responseData['historyYear'],type(responseData['historyYear']))
                    YearSearch = responseData['Year']
                    YearSearch_backup = ''

                    xlsxlist = json.loads(responseData['ExcelData'])
                    # print(xlsxlist)
                    # pprint.pprint(xlsxlist)
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
                                if key in headermodel_CapitalExpenditure.keys():
                                    # print(headermodel_CapitalExpenditure[key],value)
                                    modeldata[headermodel_CapitalExpenditure[key]] = value
                            # print(modeldata)

                            if 'PlanYear' in modeldata.keys():
                                startupload = 1
                            else:
                                # canEdit = 0
                                startupload = 0
                                err_msg = """
                                        第"%s"條數據，PlanYear不能爲空
                                                            """ % rownum
                                break
                            if 'BudgetCode' in modeldata.keys():
                                    startupload = 1
                            else:
                                # canEdit = 0
                                startupload = 0
                                err_msg = """
                                        第"%s"條數據，BudgetCode不能爲空
                                                            """ % rownum
                                break

                            create_list.append(CapitalExpenditure(**modeldata))  # object(**dict)
                            if rownum == 1:
                                YearSearch_backup = modeldata['PlanYear']
                                # print(modeldata['Year'])
                        # print(err_msg, startupload)
                        # print(create_list,)
                        # print(startupload)
                        # print(rownum, type(rownum))
                        if startupload:
                            try:
                                with transaction.atomic():
                                    CapitalExpenditure.objects.bulk_create(create_list)
                            except Exception as e:
                                # alert = '此数据正被其他使用者编辑中...'
                                alert = str(e)
                                print(alert)

                    # print('IssuesBreakdown')
                    # mock_data
                    yearOptions = [
                        # "2020", "2021", "2023"
                    ]
                    for i in CapitalExpenditure.objects.all().values("PlanYear").distinct().order_by("PlanYear"):
                        yearOptions.append(i["PlanYear"])


                    Check_dic_CapitalExpenditure = {}
                    if YearSearch:
                        Check_dic_CapitalExpenditure["Year"] = YearSearch
                    elif YearSearch_backup:
                        Check_dic_CapitalExpenditure["Year"] = YearSearch_backup

                    for i in CapitalExpenditure.objects.filter(**Check_dic_CapitalExpenditure):
                        # print(i)
                        mock_data.append(
                            {
                                "id": i.id, "PlanYear": i.PlanYear, "Customer": i.Customer, "BudgetCode": i.BudgetCode,
                                "Investment_Nature": i.Investment_Nature,
                                "Attribute_Code": i.Attribute_Code,
                                "Application_Department": i.Application_Department,
                                "Device_Name": i.Device_Name,
                                "Usage_Description": i.Usage_Description,
                                "Specifications": i.Specifications,
                                "Acceptance_Month": i.Acceptance_Month,
                                "Budget_Quantity": i.Budget_Quantity,
                                "Estimated_Original_Currency": i.Estimated_Original_Currency,
                                "Estimated_Original_Price": i.Estimated_Original_Price,
                                "Equivalent_To_RMB": i.Equivalent_To_RMB,
                                "Payment_Terms": i.Payment_Terms,
                                "Depreciation_Months": i.Depreciation_Months,
                                "Accounting_Subjects": i.Accounting_Subjects,
                                "Automated_Or_Not": i.Automated_Or_Not,
                                "Project_Code": i.Project_Code,
                                "Current_Situation": i.Current_Situation,
                                "Applicable_Scope": i.Applicable_Scope,
                                "Investment_Purpose": i.Investment_Purpose,
                                "Investment_Purpose_Des": i.Investment_Purpose_Des,
                                "Potential_Issues": i.Potential_Issues,
                                "Potential_Issues_Des": i.Potential_Issues_Des,
                                "Tighten_Expenses": i.Tighten_Expenses,
                                "Annual_Increase_PerYear": i.Annual_Increase_PerYear,
                                "Investment_Benefits_PerYear": i.Investment_Benefits_PerYear,
                                "Cash_Inflows_PerYear": i.Cash_Inflows_PerYear,
                                "Payback_Period": i.Payback_Period,
                                "Subscription_Status": i.Subscription_Status,
                                "Subscription_Quantity": i.Subscription_Quantity,
                                "Subscription_Amount": i.Subscription_Amount,
                                "Entry_Amount": i.Entry_Amount,
                            }
                        )
                    # except Exception as e:
                    #     err_msg = str(e)
        data = {
            "content1": mock_data1,
            "content2": mock_data2,
            "content3": mock_data3,
            "content4": mock_data4,
            "content5": mock_data5,
            "content6": mock_data6,
            "content7": mock_data7,

        }
        # print(data)
        return HttpResponse(json.dumps(data), content_type="application/json")
    return render(request, 'CapitalExpenditure/CapitalExpenditure_Summary.html', locals())
