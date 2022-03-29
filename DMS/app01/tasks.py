from celery.task import task
# from .views import ImportProjectinfoFromDCT
from AdapterPowerCode.models import AdapterPowerCodeBR
from .models import UserInfo
# 自定义要执行的task任务
#在项目manage.py统计目录下cmd或pycharmTerminal运行celery worker -A mydjango -l info -P eventlet，celery -A mydjango beat -l info
#窗口不能关闭
from django.core.mail import send_mail, send_mass_mail
from django.core.mail import EmailMultiAlternatives
import datetime
def mailattach(subject,from_email, to_email, message, attachname):
    # subject 主题 content 内容 to_addr 是一个列表，发送给哪些人
    # msg = EmailMultiAlternatives('邮件标题', '邮件内容', '发送方', ['接收方'])
    msg = EmailMultiAlternatives(subject, message, from_email, [to_email])
    msg.content_subtype = "html"
    # 添加附件（可选）
    # msg.attach_file('test.txt')
    msg.attach_file(attachname)
    # 发送
    msg.send()

def send_email(subject,from_email, to_email, message):
    #send_mail 每次发邮件都会建立一个连接，发多封邮件时建立多个连接。而 send_mass_mail 是建立单个连接发送多封邮件，所以一次性发送多封邮件时 send_mass_mail 要优于 send_mail。
    # subject = 'C语言中文网链接'  # 主题
    # from_email = settings.EMAIL_FROM  # 发件人，在settings.py中已经配置
    # to_email = 'xxxxx@qq.com'  # 邮件接收者列表
    # # 发送的消息
    # message = 'c语言中文网欢迎你点击登录 http://c.biancheng.net/'  # 发送普通的消息使用的时候message
    # meg_html = '<a href="http://www.baidu.com">点击跳转</a>'  # 发送的是一个html消息 需要指定
    send_mail(subject, message, from_email, [to_email])
    # subject：邮件主题；
    # message：邮件正文内容；
    # from_email：发送邮件者；
    # recipient_list：邮件接受者列表；
    # html_message：带有标签格式的HTML文本。
    # return HttpResponse('OK,邮件已经发送成功!')

def sendmass_email(messages):
    #我们还可以调用 mail 的 send_mass_mail 方法实现一次性发送多条消息，demo 如下：
    # message1 = ('Subject here', 'Here is the message', 'from@example.com', ['first@example.com', 'other@example.com'])
    # message2 = ('Another Subject', 'Here is another message', 'from@example.com', ['second@test.com'])
    # 接收元组作为参数
    # send_mass_mail((message1, message2), fail_silently=False)  # 开始发送多封邮件
    send_mass_mail(messages, fail_silently=False)  # fail_silentl运行异常的时候是否报错，默认为True不报错

@task
def ProjectSync():
    print("Start")
    mock_data = []
    mock_datalist = AdapterPowerCodeBR.objects.all()
    for i in mock_datalist:
        Photolist = []
        for h in i.Photo.all():
            Photolist.append(
                {'name': '', 'url': '/media/' + h.pic.name})  # fileListO需要的是对象列表而不是字符串列表
        if i.Predict_return and not i.Return_date:
            if datetime.datetime.now().date() > i.Predict_return:
                Exceed_days = round(
                    float(
                        str((datetime.datetime.now().date() - i.Predict_return)).split(' ')[
                            0]),
                    0)
            else:
                Exceed_days = ''
        else:
            Exceed_days = ''
        Predict_return_str = ''
        if i.Predict_return:
            Predict_return_str = str(i.Predict_return)
        else:
            Predict_return_str = ''
        Borrow_date_str = ''
        if i.Borrow_date:
            Borrow_date_str = str(i.Borrow_date)
        else:
            Borrow_date_str = ''
        Return_date_str = ''
        if i.Return_date:
            Return_date_str = str(i.Return_date)
        else:
            Return_date_str = ''
        Last_Borrow_date_str = ''
        if i.Last_Borrow_date:
            Last_Borrow_date_str = str(i.Last_Borrow_date)
        else:
            Last_Borrow_date_str = ''
        Last_Return_date_str = ''
        if i.Last_Return_date:
            Last_Return_date_str = str(i.Last_Return_date)
        else:
            Last_Return_date_str = ''
        mock_data.append(
            {"id": i.id, "Changjia": i.Changjia, "MaterialPN": i.MaterialPN,
             "Description": i.Description,
             "Power": i.Power,
             "Number": i.Number, "Location": i.Location,
             "Customer": i.Customer,
             "Project_Code": i.Project_Code,
             "Phase": i.Phase,
             "OAP": i.OAP,
             "Device_Status": i.Device_Status, "BR_Status": i.BR_Status, "BR_per": i.BR_per, "BR_per_code": i.BR_per_code,
             "Predict_return": Predict_return_str,
             "Borrow_date": Borrow_date_str, "Return_date": Return_date_str,
             "Last_BR_per": i.Last_BR_per,
             "Last_Borrow_date": Last_Borrow_date_str,
             "Last_Return_date": Last_Return_date_str, "Exceed_days": Exceed_days,
             "fileListO": Photolist},
        )
    # print(mock_data)
    for i in mock_data:
        # print(i)
        if i['Exceed_days']:
            Exceed_day = i['Exceed_days']
            devicechaoqi = i['Number']
            chaoqizhe = i['BR_per']

            subject = '【DMS】设备超期提醒'
            message = """Dear %s:
    您的設備：%s, 已經超期%s天， 請儘快處理
    注：此郵件由系統自動發出，請勿直接回復
            """ % (chaoqizhe, devicechaoqi, Exceed_day)
            from_email = '416434871@qq.com'
            to_email = []
            if UserInfo.objects.filter(account=i['BR_per_code']).first():
                if UserInfo.objects.filter(account=i['BR_per_code']).first().email:
                    to_email.append(UserInfo.objects.filter(account=i['BR_per_code']).first().email)
                    message1 = (subject, message, from_email, to_email)
                    message2 = ('邮件标题2', '邮件标题2测试内容', '416434871@qq.com', ['brotherxd@126.com'])
                    messages = (
                        message1,
                        # message2
                    )
                    print(messages)
                    sendmass_email(messages)
    # importPrjResult = ImportProjectinfoFromDCT()
    # if True:
    #     return "OK"
    # else:
    #     return "无超期"

from django.core.mail import EmailMultiAlternatives
@task
def MailhtmlSync():
    print("Starthtmlmail")
    # subject 主题 content 内容 to_addr 是一个列表，发送给哪些人
    # msg = EmailMultiAlternatives('邮件标题', '邮件内容', '发送方', ['接收方'])
    BR_perinfo = {}
    for i in AdapterPowerCodeBR.objects.all().values("BR_per_code").distinct().order_by("BR_per_code"):
        # print(i["BR_per_code"])
        if i["BR_per_code"]:  # 不要None
            BR_perinfo_byper = []
            for j in AdapterPowerCodeBR.objects.filter(BR_per_code=i["BR_per_code"], BR_Status__in=["已借出"]):
                if j.Predict_return and not j.Return_date:
                    if datetime.datetime.now().date() > j.Predict_return:
                        Exceed_days = round(
                            float(
                                str((datetime.datetime.now().date() - j.Predict_return)).split(' ')[
                                    0]),
                            0)
                    else:
                        Exceed_days = ''
                else:
                    Exceed_days = ''
                if Exceed_days:
                    BR_perinfo_byper.append(
                        {"id": j.id, "Changjia": j.Changjia, "MaterialPN": j.MaterialPN,
                         "Description": j.Description,
                         "Power": j.Power,
                         "Number": j.Number, "Location": j.Location,
                         "Customer": j.Customer,
                         "Project_Code": j.Project_Code,
                         "Phase": j.Phase,
                         "OAP": j.OAP,
                         "Device_Status": j.Device_Status, "BR_Status": j.BR_Status, "BR_per": j.BR_per,
                         "BR_per_code": j.BR_per_code,
                         "Exceed_days": Exceed_days,
                         },
                    )
            if BR_perinfo_byper:
                BR_perinfo[i["BR_per_code"]] = BR_perinfo_byper
            message = ""
    # print(BR_perinfo,len(BR_perinfo))
    for key, value in BR_perinfo.items():
        # print(value)
        messagecontend = """<p>Dear %s:</p>
            <p>您的如下設備已經超期， 請儘快處理：</p>
            <a href="http://127.0.0.1:8000/index/" style="font-size: 20px;background-color: yellow;font-weight: bolder;" target="_blank">点击此处，处理设备</a>
            <p>超期设备详情：</p>
              <p></p>
              <table border="1" cellpadding="0" cellspacing="0" width="1800" style="border-collapse: collapse;">
               <tbody>
                <tr>
                 <th style="background-color: #8c9eff">设备编号</th>
                 <th style="background-color: #8c9eff">廠家</th>
                 <th style="background-color: #8c9eff">MaterialPN</th>
                 <th style="background-color: #8c9eff">超期天数（天）</th>
                </tr>
                {sub_td}
              </tbody>
              </table> 
            <p style="color:red;">注：此郵件由系統自動發出，請勿直接回復</p>
                                    """ % UserInfo.objects.filter(account=key).first().CNname
        sub_td = ""
        sub_td_items = """
            <tr>
             <td  style="text-align:center"> {sub_item_PN} </td>
             <td  style="text-align:center"> {sub_item_changjia} </td>
             <td  style="text-align:center"> {sub_item_MaterialPN} </td>
             <td  style="text-align:center;color:red;"> {sub_item_Exceedday} </td>
            </tr>
            """
        for j in value:
            # print(j)
            sub_td += sub_td_items.format(sub_item_PN=j["Number"], sub_item_changjia=j["Changjia"],
                                          sub_item_MaterialPN=j["MaterialPN"], sub_item_Exceedday=j["Exceed_days"],)
        message = messagecontend.format(sub_td=sub_td)
        # print(message)
        subject = '【DMS】设备超期提醒'
        from_email = '416434871@qq.com'
        to_email = []
        to_email.append(UserInfo.objects.filter(account=key).first().email)
        # print(key)
        msg = EmailMultiAlternatives(subject, message, from_email, to_email)
        msg.content_subtype = "html"
        # 添加附件（可选）
        # msg.attach_file('test.txt')
        # 发送
        msg.send()
from celery import shared_task,task


@shared_task()
def add(x,y):
    # return x + y
    print (x + y)

@shared_task()
def mul(x,y):
    print ("%d * %d = %d" %(x,y,x*y))
    return x*y

@shared_task()
def sub(x,y):
    print ("%d - %d = %d"%(x,y,x-y))
    return x - y

@task(ignore_result=True,max_retries=1,default_retry_delay=10)
def just_print():
    print ("Print from celery task")