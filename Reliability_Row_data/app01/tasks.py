from celery.task import task
from .views import ImportProjectinfoFromDCT
from app01.models import UserInfo
from TestPlanSW.models import TestProjectSW, TestPlanSW
from CQM.models import CQM
from DriverTool.models import DriverList_M, ToolList_M
import datetime
from django.core.mail import EmailMultiAlternatives

# 自定义要执行的task任务
#在项目manage.py统计目录下cmd或pycharmTerminal运行celery worker -A mydjango -l info -P eventlet，celery -A mydjango beat -l info
#窗口不能关闭
@task
def ProjectSync():
    print("Start")
    importPrjResult = ImportProjectinfoFromDCT()
    if importPrjResult:
        return "OK"
    else:
        return "Fail"

@task
def MailhtmlSync():
    print("Starthtmlmail")
    # subject 主题 content 内容 to_addr 是一个列表，发送给哪些人
    # msg = EmailMultiAlternatives('邮件标题', '邮件内容', '发送方', ['接收方'])
    Projectinfo_TestPlanSWMail = {}
    for i in TestProjectSW.objects.all().values("Project").distinct().order_by("Project"):
        # print(i["BR_per_code"])
        if i["Project"]:  # 不要None
            Projectinfo_TestPlanSW = []
            eachProj = TestProjectSW.objects.filter(Project=i["Project"]).first()
            if eachProj.ScheduleEnd:
                if datetime.datetime.now().date() > eachProj.ScheduleEnd:
                    Exceed_days = round(
                        float(
                            str((datetime.datetime.now().date() - eachProj.ScheduleEnd)).split(' ')[
                                0]),
                        0)
                else:
                    Exceed_days = ''
            else:
                Exceed_days = ''
            if Exceed_days and (TestPlanSW.objects.filter(Projectinfo=eachProj) or CQM.objects.filter(Project=i["Project"])):
                # print(list(eachProj.Owner.all()),1)
                to_emails = []
                for k in eachProj.Owner.all():
                    to_emails.append(k.email)
                Projectinfo_TestPlanSW.append(
                    {"id": eachProj.id, "Customer": eachProj.Customer, "Project": eachProj.Project,
                     "Phase": eachProj.Phase,
                     "ScheduleBegin": eachProj.ScheduleBegin,
                     "ScheduleEnd": eachProj.ScheduleEnd, "Full_Function_Duration": eachProj.Full_Function_Duration,
                     "Gerber": eachProj.Gerber,
                     "Project_Code": eachProj.Project,
                     "Owner": list(eachProj.Owner.all()),
                     "to_emails": to_emails,
                     "Exceed_days": Exceed_days,
                     },
                )
                # print(Projectinfo_TestPlanSW)
            if Projectinfo_TestPlanSW:
                Projectinfo_TestPlanSWMail[i["Project"]] = Projectinfo_TestPlanSW
            message = ""
    # print(BR_perinfo,len(BR_perinfo))
    # print(Projectinfo_TestPlanSWMail)
    for key, value in Projectinfo_TestPlanSWMail.items():
        # print(value)
        messagecontend = """<p>Dear %s:</p>
            <p>您的如下机种已經超期， 請儘快更新CQM，TestPlan：</p>
            <a href="http://10.129.83.21:8002/index/" style="font-size: 20px;background-color: yellow;font-weight: bolder;" target="_blank">点击此处，处理设备</a>
            <p>超期详情：</p>
              <p></p>
              <table border="1" cellpadding="0" cellspacing="0" width="1800" style="border-collapse: collapse;">
               <tbody>
                <tr>
                 <th style="background-color: #8c9eff">机种信息</th>
                 <th style="background-color: #8c9eff">超期天数（天）</th>
                </tr>
                {sub_td}
              </tbody>
              </table> 
            <p style="color:red;">注：此郵件由系統自動發出，請勿直接回復</p>
                                    """ % value[0]["Owner"]
        sub_td = ""
        sub_td_items = """
            <tr>
             <td  style="text-align:center"> {sub_item_Project} </td>
             <td  style="text-align:center;color:red;"> {sub_item_Exceedday} </td>
            </tr>
            """
        for j in value:
            # print(j)
            sub_td += sub_td_items.format(sub_item_Project=j["Project"], sub_item_Exceedday=j["Exceed_days"],)
        message = messagecontend.format(sub_td=sub_td)
        # print(message)
        subject = '【DDIS】数据上传提醒'
        from_email = '416434871@qq.com'
        to_email = []
        # to_email.append(UserInfo.objects.filter(account=key).first().email)
        to_email.append('edwin_cao@compal.com')
        # print(key)
        # print(to_email)
        msg = EmailMultiAlternatives(subject, message, from_email, to_email)
        msg.content_subtype = "html"
        # 添加附件（可选）
        # msg.attach_file('test.txt')
        # 发送
        msg.send()