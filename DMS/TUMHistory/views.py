from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
import datetime,os, json
from django.db.models import Max,Min,Sum,Count,Q
from django.http import JsonResponse
from service.init_permission import init_permission
from DMS import settings
from django.core.mail import send_mail, send_mass_mail
from django.core.mail import EmailMultiAlternatives
from app01 import tasks
from app01.models import UserInfo
from app01 import tasks
from .models import *
from django.db.models.functions import Trunc
# Create your views here.
@csrf_exempt
def SummaryTUM(request):
    if not request.session.get('is_login', None):
        # print(request.session.get('is_login', None))
        return redirect('/login/')
    weizhi = "TUMHistory/Unit"
    C38Table = [
        # {"Item": "領用", "Customer": "預算", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "領用", "Customer": "實際", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "領用", "Customer": "差異（實際-預算）", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "退還", "Customer": "預算", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "退還", "Customer": "實際", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "退還", "Customer": "差異（實際-預算）", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "領退差異（領用-退還）", "Customer": "差異", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
    ]
    T88Table = [
        # {"Item": "領用", "Customer": "預算", "Jan": "188", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "領用", "Customer": "實際", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "領用", "Customer": "差異（實際-預算）", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "退還", "Customer": "預算", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "退還", "Customer": "實際", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "退還", "Customer": "差異（實際-預算）", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "領退差異（領用-退還）", "Customer": "差異", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
    ]
    sectionCustomer = [
        "C38(NB)", "C38(AIO)", "C85", "T88(AIO)"
                       ]
    sectionCategory = [
        "領用", "退還"
    ]
    errMsgNumber = ""
    canEdit = 1
    canEdit = 0
    roles = []
    onlineuser = request.session.get('account')
    # print(UserInfo.objects.get(account=onlineuser))
    for i in UserInfo.objects.get(account=onlineuser).role.all():
        roles.append(i.name)
    for i in roles:
        if i == 'Sys_Admin':
            # editPpriority = 4
            canEdit = 1
    if request.method == "POST":
        if request.POST:
            try:
                if request.POST.get('isGetData') == 'first':
                    Year_now = str(datetime.datetime.now().year)
                    YearNow = str(datetime.datetime.now().year)
                    if (int(YearNow) % 4) == 0:
                        if (int(YearNow) % 100) == 0:
                            if (int(YearNow) % 400) == 0:
                                # print("{0} 是闰年".format(YearNow))  # 整百年能被400整除的是闰年
                                mounthlist = [("Jan", "-1-31"), ("Feb", "-2-29"), ("Mar", "-3-31"), ("Apr", "-4-30"),
                                              ("May", "-5-31"), ("Jun", "-6-30"),
                                              ("Jul", "-7-31"), ("Aug", "-8-31"), ("Sep", "-9-30"), ("Oct", "-10-31"),
                                              ("Nov", "-11-30"), ("Dec", "-12-31"), ]
                            else:
                                # print("{0} 不是闰年".format(YearNow))
                                mounthlist = [("Jan", "-1-31"), ("Feb", "-2-28"), ("Mar", "-3-31"), ("Apr", "-4-30"),
                                              ("May", "-5-31"), ("Jun", "-6-30"),
                                              ("Jul", "-7-31"), ("Aug", "-8-31"), ("Sep", "-9-30"), ("Oct", "-10-31"),
                                              ("Nov", "-11-30"), ("Dec", "-12-31"), ]
                        else:
                            # print("{0} 是闰年".format(YearNow))  # 非整百年能被4整除的为闰年
                            mounthlist = [("Jan", "-1-31"), ("Feb", "-2-29"), ("Mar", "-3-31"), ("Apr", "-4-30"),
                                          ("May", "-5-31"), ("Jun", "-6-30"),
                                          ("Jul", "-7-31"), ("Aug", "-8-31"), ("Sep", "-9-30"), ("Oct", "-10-31"),
                                          ("Nov", "-11-30"), ("Dec", "-12-31"), ]
                    else:
                        # print("{0} 不是闰年".format(YearNow))
                        mounthlist = [("Jan", "-1-31"), ("Feb", "-2-28"), ("Mar", "-3-31"), ("Apr", "-4-30"),
                                      ("May", "-5-31"),
                                      ("Jun", "-6-30"),
                                      ("Jul", "-7-31"), ("Aug", "-8-31"), ("Sep", "-9-30"), ("Oct", "-10-31"),
                                      ("Nov", "-11-30"), ("Dec", "-12-31"), ]
                    mounthnow = datetime.datetime.now().month
                    # C38Table 领用
                    sectionCustomer_C38 = [
                        "C38(NB)", "C38(AIO)", "C85"
                    ]
                    Jan_Unitbudget_Num = Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="領用").aggregate(Sum('Jan'))['Jan__sum']
                    Feb_Unitbudget_Num = Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="領用").aggregate(Sum('Feb'))['Feb__sum']
                    Mar_Unitbudget_Num = Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="領用").aggregate(Sum('Mar'))['Mar__sum']
                    Apr_Unitbudget_Num = Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="領用").aggregate(Sum('Apr'))['Apr__sum']
                    May_Unitbudget_Num = Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="領用").aggregate(Sum('May'))['May__sum']
                    Jun_Unitbudget_Num = Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="領用").aggregate(Sum('Jun'))['Jun__sum']
                    Jul_Unitbudget_Num = Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="領用").aggregate(Sum('Jul'))['Jul__sum']
                    Aug_Unitbudget_Num = Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="領用").aggregate(Sum('Aug'))['Aug__sum']
                    Sep_Unitbudget_Num = Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="領用").aggregate(Sum('Sep'))['Sep__sum']
                    Oct_Unitbudget_Num = Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="領用").aggregate(Sum('Oct'))['Oct__sum']
                    Nov_Unitbudget_Num = Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="領用").aggregate(Sum('Nov'))['Nov__sum']
                    Dec_Unitbudget_Num = Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="領用").aggregate(Sum('Dec'))['Dec__sum']
                    C38_yusuan_dic = {"Item": "領用", "Customer": "預算", "Jan": Jan_Unitbudget_Num, "Feb": Feb_Unitbudget_Num, "Mar": Mar_Unitbudget_Num,
                                     "Apr": Apr_Unitbudget_Num, "May": May_Unitbudget_Num, "Jun": Jun_Unitbudget_Num, "Jul": Jul_Unitbudget_Num,
                                     "Aug": Aug_Unitbudget_Num, "Sep": Sep_Unitbudget_Num, "Oct": Oct_Unitbudget_Num, "Nov": Nov_Unitbudget_Num, "Dec": Dec_Unitbudget_Num,
                     }
                    C38_shiji_dic = {"Item": "領用", "Customer": "實際"}
                    C38_chayi_dic = {"Item": "領用", "Customer": "差異（實際-預算）"}
                    C38_yusuan_dic_summary_mounth = 0
                    C38_yusuan_dic_summary = 0
                    C38_shiji_dic_summary_mounth = 0
                    mounthnum = 1
                    for i in mounthlist:
                        if i[0] in C38_yusuan_dic.keys() and C38_yusuan_dic[i[0]]:
                            C38_yusuan_dic_summary += C38_yusuan_dic[i[0]]
                            if mounthnum > mounthnow:
                                pass
                            else:
                                DateNow_begin = datetime.datetime.strptime(YearNow + "-" + i[1].split("-")[1] + "-1",
                                                                           '%Y-%m-%d')
                                # print(DateNow_begin)
                                DateNow = datetime.datetime.strptime(YearNow + i[1], '%Y-%m-%d')
                                Test_Endperiod = [DateNow_begin, DateNow]
                                C38_shiji_dic[i[0]] = UnitInDQA_Tum.objects.filter(CustomerCode__in=sectionCustomer_C38, InData__range=Test_Endperiod).aggregate(Sum("QTY"))['QTY__sum']
                                C38_chayi_dic[i[0]] = C38_shiji_dic[i[0]] - C38_yusuan_dic[i[0]]
                                C38_shiji_dic_summary_mounth += C38_shiji_dic[i[0]]
                                C38_yusuan_dic_summary_mounth += C38_yusuan_dic[i[0]]
                        mounthnum += 1
                    # print(C38_shiji_dic)
                    C38_yusuan_dic['Summary_Month'] = C38_yusuan_dic_summary_mounth
                    C38_yusuan_dic['Summary'] = C38_yusuan_dic_summary
                    C38_shiji_dic['Summary_Month'] = C38_shiji_dic_summary_mounth
                    C38_shiji_dic['Summary'] = C38_shiji_dic_summary_mounth
                    C38_chayi_dic['Summary_Month'] = C38_shiji_dic_summary_mounth - C38_yusuan_dic_summary_mounth
                    C38_chayi_dic['Summary'] = C38_shiji_dic_summary_mounth - C38_yusuan_dic_summary
                    C38Table.append(C38_yusuan_dic)
                    C38Table.append(C38_shiji_dic)
                    C38Table.append(C38_chayi_dic)
                    # C38Table 退還
                    tuihuan_Jan_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="退還").aggregate(
                        Sum('Jan'))['Jan__sum']
                    tuihuan_Feb_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="退還").aggregate(
                        Sum('Feb'))['Feb__sum']
                    tuihuan_Mar_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="退還").aggregate(
                        Sum('Mar'))['Mar__sum']
                    tuihuan_Apr_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="退還").aggregate(
                        Sum('Apr'))['Apr__sum']
                    tuihuan_May_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="退還").aggregate(
                        Sum('May'))['May__sum']
                    tuihuan_Jun_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="退還").aggregate(
                        Sum('Jun'))['Jun__sum']
                    tuihuan_Jul_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="退還").aggregate(
                        Sum('Jul'))['Jul__sum']
                    tuihuan_Aug_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="退還").aggregate(
                        Sum('Aug'))['Aug__sum']
                    tuihuan_Sep_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="退還").aggregate(
                        Sum('Sep'))['Sep__sum']
                    tuihuan_Oct_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="退還").aggregate(
                        Sum('Oct'))['Oct__sum']
                    tuihuan_Nov_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="退還").aggregate(
                        Sum('Nov'))['Nov__sum']
                    tuihuan_Dec_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_C38, Year=Year_now, Category="退還").aggregate(
                        Sum('Dec'))['Dec__sum']
                    tuihuan_C38_yusuan_dic = {"Item": "退還", "Customer": "預算", "Jan": tuihuan_Jan_Unitbudget_Num, "Feb": tuihuan_Feb_Unitbudget_Num,
                                      "Mar": tuihuan_Mar_Unitbudget_Num,
                                      "Apr": tuihuan_Apr_Unitbudget_Num, "May": tuihuan_May_Unitbudget_Num, "Jun": tuihuan_Jun_Unitbudget_Num,
                                      "Jul": tuihuan_Jul_Unitbudget_Num,
                                      "Aug": tuihuan_Aug_Unitbudget_Num, "Sep": tuihuan_Sep_Unitbudget_Num, "Oct": tuihuan_Oct_Unitbudget_Num,
                                      "Nov": tuihuan_Nov_Unitbudget_Num, "Dec": tuihuan_Dec_Unitbudget_Num,
                                      }
                    tuihuan_C38_shiji_dic = {"Item": "退還", "Customer": "實際"}
                    tuihuan_C38_chayi_dic = {"Item": "退還", "Customer": "差異（實際-預算）"}
                    lingtui_C38_chayi_dic = {"Item": "領退差異（領用-退還）", "Customer": "差異"}
                    tuihuan_C38_yusuan_dic_summary_mounth = 0
                    tuihuan_C38_yusuan_dic_summary = 0
                    tuihuan_C38_shiji_dic_summary_mounth = 0
                    mounthnum = 1
                    for i in mounthlist:
                        if i[0] in tuihuan_C38_yusuan_dic.keys() and tuihuan_C38_yusuan_dic[i[0]]:
                            tuihuan_C38_yusuan_dic_summary += tuihuan_C38_yusuan_dic[i[0]]
                            if mounthnum > mounthnow:
                                pass
                            else:
                                DateNow_begin = datetime.datetime.strptime(YearNow + "-" + i[1].split("-")[1] + "-1",
                                                                           '%Y-%m-%d')
                                # print(DateNow_begin)
                                DateNow = datetime.datetime.strptime(YearNow + i[1], '%Y-%m-%d')
                                Test_Endperiod = [DateNow_begin, DateNow]
                                tuihuan_C38_shiji_dic[i[0]] = DQAUnit_TUMHistory.objects.filter(CustomerCode__in=sectionCustomer_C38,
                                                                                                ReturnData__range=Test_Endperiod).aggregate(
                                    Sum("QTY"))['QTY__sum']
                                tuihuan_C38_chayi_dic[i[0]] = tuihuan_C38_shiji_dic[i[0]] - tuihuan_C38_yusuan_dic[i[0]]
                                lingtui_C38_chayi_dic[i[0]] = C38_chayi_dic[i[0]] - tuihuan_C38_chayi_dic[i[0]]
                                tuihuan_C38_shiji_dic_summary_mounth += tuihuan_C38_shiji_dic[i[0]]
                                tuihuan_C38_yusuan_dic_summary_mounth += tuihuan_C38_yusuan_dic[i[0]]
                        mounthnum += 1
                    # print(C38_shiji_dic)
                    tuihuan_C38_yusuan_dic['Summary_Month'] = tuihuan_C38_yusuan_dic_summary_mounth
                    tuihuan_C38_yusuan_dic['Summary'] = tuihuan_C38_yusuan_dic_summary
                    tuihuan_C38_shiji_dic['Summary_Month'] = tuihuan_C38_shiji_dic_summary_mounth
                    tuihuan_C38_shiji_dic['Summary'] = tuihuan_C38_shiji_dic_summary_mounth
                    tuihuan_C38_chayi_dic['Summary_Month'] = tuihuan_C38_shiji_dic_summary_mounth - tuihuan_C38_yusuan_dic_summary_mounth
                    tuihuan_C38_chayi_dic['Summary'] = tuihuan_C38_shiji_dic_summary_mounth - tuihuan_C38_yusuan_dic_summary
                    lingtui_C38_chayi_dic[
                        'Summary_Month'] = C38_chayi_dic['Summary_Month'] - tuihuan_C38_chayi_dic['Summary_Month']
                    lingtui_C38_chayi_dic['Summary'] = C38_chayi_dic['Summary'] - tuihuan_C38_chayi_dic['Summary']
                    C38Table.append(tuihuan_C38_yusuan_dic)
                    C38Table.append(tuihuan_C38_shiji_dic)
                    C38Table.append(tuihuan_C38_chayi_dic)
                    C38Table.append(lingtui_C38_chayi_dic)

                    #T88Table 领用
                    sectionCustomer_T88 = [
                        "T88(AIO)"
                    ]
                    Year_now = str(datetime.datetime.now().year)
                    Jan_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="領用").aggregate(
                        Sum('Jan'))['Jan__sum']
                    Feb_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="領用").aggregate(
                        Sum('Feb'))['Feb__sum']
                    Mar_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="領用").aggregate(
                        Sum('Mar'))['Mar__sum']
                    Apr_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="領用").aggregate(
                        Sum('Apr'))['Apr__sum']
                    May_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="領用").aggregate(
                        Sum('May'))['May__sum']
                    Jun_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="領用").aggregate(
                        Sum('Jun'))['Jun__sum']
                    Jul_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="領用").aggregate(
                        Sum('Jul'))['Jul__sum']
                    Aug_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="領用").aggregate(
                        Sum('Aug'))['Aug__sum']
                    Sep_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="領用").aggregate(
                        Sum('Sep'))['Sep__sum']
                    Oct_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="領用").aggregate(
                        Sum('Oct'))['Oct__sum']
                    Nov_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="領用").aggregate(
                        Sum('Nov'))['Nov__sum']
                    Dec_Unitbudget_Num = \
                    Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="領用").aggregate(
                        Sum('Dec'))['Dec__sum']
                    T88_yusuan_dic = {"Item": "領用", "Customer": "預算", "Jan": Jan_Unitbudget_Num, "Feb": Feb_Unitbudget_Num,
                                      "Mar": Mar_Unitbudget_Num,
                                      "Apr": Apr_Unitbudget_Num, "May": May_Unitbudget_Num, "Jun": Jun_Unitbudget_Num,
                                      "Jul": Jul_Unitbudget_Num,
                                      "Aug": Aug_Unitbudget_Num, "Sep": Sep_Unitbudget_Num, "Oct": Oct_Unitbudget_Num,
                                      "Nov": Nov_Unitbudget_Num, "Dec": Dec_Unitbudget_Num,
                                      }

                    T88_shiji_dic = {"Item": "領用", "Customer": "實際"}
                    T88_chayi_dic = {"Item": "領用", "Customer": "差異（實際-預算）"}
                    YearNow = str(datetime.datetime.now().year)

                    T88_yusuan_dic_summary_mounth = 0
                    T88_yusuan_dic_summary = 0
                    T88_shiji_dic_summary_mounth = 0
                    mounthnum = 1
                    for i in mounthlist:
                        if i[0] in T88_yusuan_dic.keys() and T88_yusuan_dic[i[0]]:
                            T88_yusuan_dic_summary += T88_yusuan_dic[i[0]]
                            if mounthnum > mounthnow:
                                pass
                            else:
                                DateNow_begin = datetime.datetime.strptime(YearNow + "-" + i[1].split("-")[1] + "-1",
                                                                           '%Y-%m-%d')
                                # print(DateNow_begin)
                                DateNow = datetime.datetime.strptime(YearNow + i[1], '%Y-%m-%d')
                                Test_Endperiod = [DateNow_begin, DateNow]
                                T88_shiji_dic[i[0]] = UnitInDQA_Tum.objects.filter(CustomerCode__in=sectionCustomer_T88,
                                                                                   InData__range=Test_Endperiod).aggregate(
                                    Sum("QTY"))['QTY__sum']
                                T88_chayi_dic[i[0]] = T88_shiji_dic[i[0]] - T88_yusuan_dic[i[0]]
                                T88_shiji_dic_summary_mounth += T88_shiji_dic[i[0]]
                                T88_yusuan_dic_summary_mounth += T88_yusuan_dic[i[0]]
                        mounthnum += 1
                    # print(T88_shiji_dic)
                    T88_yusuan_dic['Summary_Month'] = T88_yusuan_dic_summary_mounth
                    T88_yusuan_dic['Summary'] = T88_yusuan_dic_summary
                    T88_shiji_dic['Summary_Month'] = T88_shiji_dic_summary_mounth
                    T88_shiji_dic['Summary'] = T88_shiji_dic_summary_mounth
                    T88_chayi_dic['Summary_Month'] = T88_shiji_dic_summary_mounth - T88_yusuan_dic_summary_mounth
                    T88_chayi_dic['Summary'] = T88_shiji_dic_summary_mounth - T88_yusuan_dic_summary
                    T88Table.append(T88_yusuan_dic)
                    T88Table.append(T88_shiji_dic)
                    T88Table.append(T88_chayi_dic)
                    # T88Table 退还
                    tuihuan_Jan_Unitbudget_Num = \
                        Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="退還").aggregate(
                            Sum('Jan'))['Jan__sum']
                    tuihuan_Feb_Unitbudget_Num = \
                        Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="退還").aggregate(
                            Sum('Feb'))['Feb__sum']
                    tuihuan_Mar_Unitbudget_Num = \
                        Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="退還").aggregate(
                            Sum('Mar'))['Mar__sum']
                    tuihuan_Apr_Unitbudget_Num = \
                        Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="退還").aggregate(
                            Sum('Apr'))['Apr__sum']
                    tuihuan_May_Unitbudget_Num = \
                        Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="退還").aggregate(
                            Sum('May'))['May__sum']
                    tuihuan_Jun_Unitbudget_Num = \
                        Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="退還").aggregate(
                            Sum('Jun'))['Jun__sum']
                    tuihuan_Jul_Unitbudget_Num = \
                        Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="退還").aggregate(
                            Sum('Jul'))['Jul__sum']
                    tuihuan_Aug_Unitbudget_Num = \
                        Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="退還").aggregate(
                            Sum('Aug'))['Aug__sum']
                    tuihuan_Sep_Unitbudget_Num = \
                        Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="退還").aggregate(
                            Sum('Sep'))['Sep__sum']
                    tuihuan_Oct_Unitbudget_Num = \
                        Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="退還").aggregate(
                            Sum('Oct'))['Oct__sum']
                    tuihuan_Nov_Unitbudget_Num = \
                        Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="退還").aggregate(
                            Sum('Nov'))['Nov__sum']
                    tuihuan_Dec_Unitbudget_Num = \
                        Unitbudget.objects.filter(Customer__in=sectionCustomer_T88, Year=Year_now, Category="退還").aggregate(
                            Sum('Dec'))['Dec__sum']
                    tuihuan_T88_yusuan_dic = {"Item": "退還", "Customer": "預算", "Jan": tuihuan_Jan_Unitbudget_Num,
                                              "Feb": tuihuan_Feb_Unitbudget_Num,
                                              "Mar": tuihuan_Mar_Unitbudget_Num,
                                              "Apr": tuihuan_Apr_Unitbudget_Num, "May": tuihuan_May_Unitbudget_Num,
                                              "Jun": tuihuan_Jun_Unitbudget_Num,
                                              "Jul": tuihuan_Jul_Unitbudget_Num,
                                              "Aug": tuihuan_Aug_Unitbudget_Num, "Sep": tuihuan_Sep_Unitbudget_Num,
                                              "Oct": tuihuan_Oct_Unitbudget_Num,
                                              "Nov": tuihuan_Nov_Unitbudget_Num, "Dec": tuihuan_Dec_Unitbudget_Num,
                                              }
                    tuihuan_T88_shiji_dic = {"Item": "退還", "Customer": "實際"}
                    tuihuan_T88_chayi_dic = {"Item": "退還", "Customer": "差異（實際-預算）"}
                    lingtui_T88_chayi_dic = {"Item": "領退差異（領用-退還）", "Customer": "差異"}
                    tuihuan_T88_yusuan_dic_summary_mounth = 0
                    tuihuan_T88_yusuan_dic_summary = 0
                    tuihuan_T88_shiji_dic_summary_mounth = 0
                    mounthnum = 1
                    for i in mounthlist:
                        if i[0] in tuihuan_T88_yusuan_dic.keys() and tuihuan_T88_yusuan_dic[i[0]]:
                            tuihuan_T88_yusuan_dic_summary += tuihuan_T88_yusuan_dic[i[0]]
                            if mounthnum > mounthnow:
                                pass
                            else:
                                DateNow_begin = datetime.datetime.strptime(YearNow + "-" + i[1].split("-")[1] + "-1",
                                                                           '%Y-%m-%d')
                                # print(DateNow_begin)
                                DateNow = datetime.datetime.strptime(YearNow + i[1], '%Y-%m-%d')
                                Test_Endperiod = [DateNow_begin, DateNow]
                                tuihuan_T88_shiji_dic[i[0]] = \
                                DQAUnit_TUMHistory.objects.filter(CustomerCode__in=sectionCustomer_T88,
                                                                  ReturnData__range=Test_Endperiod).aggregate(
                                    Sum("QTY"))['QTY__sum']
                                tuihuan_T88_chayi_dic[i[0]] = tuihuan_T88_shiji_dic[i[0]] - tuihuan_T88_yusuan_dic[i[0]]
                                lingtui_T88_chayi_dic[i[0]] = T88_chayi_dic[i[0]] - tuihuan_T88_chayi_dic[i[0]]
                                tuihuan_T88_shiji_dic_summary_mounth += tuihuan_T88_shiji_dic[i[0]]
                                tuihuan_T88_yusuan_dic_summary_mounth += tuihuan_T88_yusuan_dic[i[0]]
                        mounthnum += 1
                    # print(T88_shiji_dic)
                    tuihuan_T88_yusuan_dic['Summary_Month'] = tuihuan_T88_yusuan_dic_summary_mounth
                    tuihuan_T88_yusuan_dic['Summary'] = tuihuan_T88_yusuan_dic_summary
                    tuihuan_T88_shiji_dic['Summary_Month'] = tuihuan_T88_shiji_dic_summary_mounth
                    tuihuan_T88_shiji_dic['Summary'] = tuihuan_T88_shiji_dic_summary_mounth
                    tuihuan_T88_chayi_dic[
                        'Summary_Month'] = tuihuan_T88_shiji_dic_summary_mounth - tuihuan_T88_yusuan_dic_summary_mounth
                    tuihuan_T88_chayi_dic['Summary'] = tuihuan_T88_shiji_dic_summary_mounth - tuihuan_T88_yusuan_dic_summary
                    lingtui_T88_chayi_dic[
                        'Summary_Month'] = T88_chayi_dic['Summary_Month'] - tuihuan_T88_chayi_dic['Summary_Month']
                    lingtui_T88_chayi_dic['Summary'] = T88_chayi_dic['Summary'] - tuihuan_T88_chayi_dic['Summary']
                    T88Table.append(tuihuan_T88_yusuan_dic)
                    T88Table.append(tuihuan_T88_shiji_dic)
                    T88Table.append(tuihuan_T88_chayi_dic)
                    T88Table.append(lingtui_T88_chayi_dic)
            except Exception as e:
                print('first',str(e))
            try:
                if request.POST.get('action') == 'addSubmit':
                    Input_dic = {}
                    Check_dic = {}
                    if request.POST.get('Customer'):
                        Input_dic['Customer'] = request.POST.get('Customer')
                        Check_dic['Customer'] = request.POST.get('Customer')
                    if request.POST.get('Year'):
                        Input_dic['Year'] = request.POST.get('Year')
                        Check_dic['Year'] = request.POST.get('Year')
                    if request.POST.get('Category'):
                        Input_dic['Category'] = request.POST.get('Category')
                        Check_dic['Category'] = request.POST.get('Category')
                    if request.POST.get('Jan'):
                        Input_dic['Jan'] = request.POST.get('Jan')
                    if request.POST.get('Feb'):
                        Input_dic['Feb'] = request.POST.get('Feb')
                    if request.POST.get('Mar'):
                        Input_dic['Mar'] = request.POST.get('Mar')
                    if request.POST.get('Apr'):
                        Input_dic['Apr'] = request.POST.get('Apr')
                    if request.POST.get('May'):
                        Input_dic['May'] = request.POST.get('May')
                    if request.POST.get('Jun'):
                        Input_dic['Jun'] = request.POST.get('Jun')
                    if request.POST.get('Jul'):
                        Input_dic['Jul'] = request.POST.get('Jul')
                    if request.POST.get('Aug'):
                        Input_dic['Aug'] = request.POST.get('Aug')
                    if request.POST.get('Sep'):
                        Input_dic['Sep'] = request.POST.get('Sep')
                    if request.POST.get('Oct'):
                        Input_dic['Oct'] = request.POST.get('Oct')
                    if request.POST.get('Nov'):
                        Input_dic['Nov'] = request.POST.get('Nov')
                    if request.POST.get('Dec'):
                        Input_dic['Dec'] = request.POST.get('Dec')
                    if Unitbudget.objects.filter(**Check_dic):
                        errMsgNumber = '该客户别：%s，该年份：%s的%s，数据已经存在。' % (Check_dic['Customer'], Check_dic['Year'], Check_dic['Category'])
                    else:
                        Unitbudget.objects.create(**Input_dic)
            except Exception as e:
                print('addSubmit',str(e))
            try:
                if request.POST.get('isGetData') == 'synchronous':
                    tasks.GetTumdata()
            except Exception as e:
                print('isGetData',str(e))

            data = {
                "C38Table": C38Table,
                "T88Table": T88Table,
                "sectionCustomer": sectionCustomer,
                "sectionCategory": sectionCategory,
                "errMsgNumber": errMsgNumber,
                "canEdit": canEdit,
            }
        return HttpResponse(json.dumps(data), content_type="application/json")
    return render(request, 'TUMHistory/TUMHistory.html', locals())

@csrf_exempt
def SummaryMateria(request):
    if not request.session.get('is_login', None):
        # print(request.session.get('is_login', None))
        return redirect('/login/')
    weizhi = "TUMHistory/Materia"
    C38Table = [
        # {"Item": "領用", "Customer": "預算", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "領用", "Customer": "實際", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "領用", "Customer": "差異（實際-預算）", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "退還", "Customer": "預算", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "退還", "Customer": "實際", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "退還", "Customer": "差異（實際-預算）", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "領退差異（領用-退還）", "Customer": "差異", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
    ]
    T88Table = [
        # {"Item": "領用", "Customer": "預算", "Jan": "188", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "領用", "Customer": "實際", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "領用", "Customer": "差異（實際-預算）", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "退還", "Customer": "預算", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "退還", "Customer": "實際", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "退還", "Customer": "差異（實際-預算）", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
        # {"Item": "領退差異（領用-退還）", "Customer": "差異", "Jan": "168", "Feb": "178", "Mar": "233", "Apr": "233", "May": "233",
        #  "Jun": "233", "Jul": "233", "Aug": "233", "Sep": "233", "Oct": "233", "Nov": "233", "Dec": "233",
        #  "Summary_Month": "233", "Summary": "233"},
    ]
    sectionCustomer = [
        "C38(NB)", "C38(AIO)", "C85", "T88(AIO)"
                       ]
    sectionCategory = [
        "領用", "退還"
    ]
    errMsgNumber = ""
    canEdit = 1
    canEdit = 0
    roles = []
    onlineuser = request.session.get('account')
    # print(UserInfo.objects.get(account=onlineuser))
    for i in UserInfo.objects.get(account=onlineuser).role.all():
        roles.append(i.name)
    for i in roles:
        if i == 'Sys_Admin':
            # editPpriority = 4
            canEdit = 1
    if request.method == "POST":
        if request.POST:

            data = {
                "C38Table": C38Table,
                "T88Table": T88Table,
                "sectionCustomer": sectionCustomer,
                "sectionCategory": sectionCategory,
                "errMsgNumber": errMsgNumber,
                "canEdit": canEdit,
            }
        return HttpResponse(json.dumps(data), content_type="application/json")
    return render(request, 'TUMHistory/MateriaHistory.html', locals())