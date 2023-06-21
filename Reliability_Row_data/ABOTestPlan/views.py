from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
import datetime,os

from app01.models import ProjectinfoinDCT, UserInfo
# from .models import DriverList_M
# from .models import ToolList_M
from django.http import HttpResponse
import datetime,json,simplejson,requests,time
import pandas as pd
import pprint
from pathlib import Path
import os, sys
from django.conf import settings
# Create your views here.

def read_excel(src_file,header=0,sheetnum=0):
    df = pd.read_excel(src_file, header=header, sheet_name=int(sheetnum)).iloc[:,
         0:]  # ‘,’前面是行，后面是列，sheet_name指定sheet，可是是int第几个，可以是名称，header从第几行开始读取
    # # 显示所有列
    pd.set_option('display.max_columns', None)
    # # 显示所有行
    # pd.set_options('display.max_rows', None)
    # pprint.pprint(df)
    dataexcel = df.values[:, :]
    # datatest = []
    # for i in dataexcel:
    #     ls = []
    #     for j in i:
    #         ls.append(j)
    #     datatest.append(ls)
    # print(list(df.columns))
    # pprint.pprint(datatest)
    df = df.fillna('')  # 替换 Nan, 否则没有双引号的Nan，json.dumps(data)时虽然不报错，但是传到前端反序列化后无法获取数据
    excel_dic = df.to_dict('records')
    print("111", excel_dic)
    hangnum = 1
    for i in excel_dic:
        i["dataid"] = hangnum
        hangnum += 1
    key_data = list(df.columns)
    # pprint.pprint(excel_dic)
    # df.to_excel('C:/media/ABOTestPlan/upload.xlsx', sheet_name="sheet1", index=False,
    #             engine='openpyxl')
    # with pd.ExcelWriter(src_file, engine="openpyxl", mode='a', if_sheet_exists='replace') as writer:
    #     df.to_excel(writer, sheet_name='Sheet1', index=False)  # engine="openpyxl"
    from openpyxl import load_workbook
    #读取所有批注
    workbook = load_workbook(src_file)
    first_sheet = workbook.get_sheet_names()[0]
    worksheet = workbook.get_sheet_by_name(first_sheet)

    comments = []
    rownum = 0
    for row in worksheet.rows:
        cellnum = 0
        for cell in row:
            if cell.comment:
                comments.append([rownum, cellnum, cell.comment.text])
            cellnum += 1
        rownum += 1
    print(comments)
    return excel_dic,key_data
from openpyxl import load_workbook
def save_exel(save_data,src_file,header=0,sheetnum=0):
    df1 = pd.read_excel(src_file, sheet_name=None)
    sheetname = list(df1)
    df2 = pd.DataFrame(save_data)
    print("2222", df2)
    foo = pd.DataFrame({
        'temp': ['message1', 'message2', 'message3'],
        'var2': [1, 2, 3],
        'col3': [4, 5, 6]
    })

    # Setup a DataFrame with corresponding hover values
    # tooltips_df = pd.DataFrame({
    #     'temp': ['i am message 1', 'i am foo', 'i am lala'],
    #     'var2': ' another random message',
    #     'col3': 'more random messages'
    # })
    #
    # # Assign tooltips
    # foo.style.set_tooltips(tooltips_df)
    # foo.to_excel('C:/media/ABOTestPlan/tips.xlsx', sheet_name="sheet1", index=False)
    # print("333", foo)
    # excel_writer = pd.ExcelWriter(r'C:\Users\Administrator\Desktop\test2.xlsx')  # 定义writer，选择文件（文件可以不存在,相当于新建文件)
    # data1.to_excel(excel_writer, sheet_name='sheet_data1')
    # data2.to_excel(excel_writer, sheet_name='sheet_data2')
    # excel_writer.save()  # 保存文件   ---data1和data2都在，原数据被覆盖
    #无法保证打结果的始终在最左列
    # with pd.ExcelWriter(src_file, mode='a', engine='openpyxl') as writer:
    #     wb = writer.book  # openpyxl.workbook.workbook.Workbook 获取所有sheet
    #     wb.remove(wb[sheetname[0]])  # 删除需要覆盖的sheet
    #     # print(wb.sheetnames)
    #     # df2.to_excel(writer, sheet_name=sheetname[0], index=True)  ##sheet st3的内容更新成st1值
    # with pd.ExcelWriter(src_file, mode='a', engine='openpyxl') as writer:
    #     df2.to_excel(writer, sheet_name=sheetname[0], index=False)  ##sheet st3的内容更新成st1值

    #无法保存公式，样式，注解
    excel_list = [df2]
    for i in sheetname:
        if i != sheetname[0]:
            excel_list.append(pd.read_excel(src_file, sheet_name=i))
    with pd.ExcelWriter(src_file, engine='openpyxl') as writer:
        num = 0
        for i in excel_list:
            i.to_excel(writer, sheet_name=sheetname[num], index=False)  ##sheet st3的内容更新成st1值
            num += 1

def recursion_dir_all_file(path):
    '''
    :param path: 文件夹目录
    '''
    file_list = []
    for dir_path, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(dir_path, file)
            if "\\" in file_path:
                file_path = file_path.replace('\\', '/')
            file_list.append(file_path)
        for dir in dirs:
            file_list.extend(recursion_dir_all_file(os.path.join(dir_path, dir)))
    return file_list

@csrf_exempt
def ABOTestPlan_edit(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    Skin = request.COOKIES.get('Skin_raw')
    # print(Skin)
    if not Skin:
        Skin = "/static/src/blue.jpg"
    weizhi="ABOTestPlan/edit"
    # status='0'

    excel_dic = []
    key_list = []
    canExport = 1
    canEdit = 1


    if request.method == "POST":

        # print(request.POST, request.method)
        # print(request.body)
        # print(type(request.body),type(request.POST))
        # responseData = json.loads(request.body)
        # print(responseData)
        # if request.POST.get('isGetData') == 'first':

        # test = request.POST
        # for i in test:
        #     print(test[i])
        if request.POST.get('isGetData') == 'SEARCH':
            src_file = "C:/media/ABOTestPlan/do.xlsx"
            excel_dic = read_excel(src_file)[0]
            # print(type(excel_dic))
            key_list = read_excel(src_file)[1]
            save_exel(excel_dic,src_file)


        data = {
            "err_ok": "0",
            "excel_dic": excel_dic,
            "key_list": key_list,
            "canExport": canExport,
            "canEdit": canEdit,
            # "status":status
        }
        # print(type(json.dumps(data)),json.dumps(data))
        return HttpResponse(json.dumps(data), content_type="application/json")
    return render(request, 'ABOTestPlan/ABOTestPlan_edit.html', locals())

@csrf_exempt
def ABOTestPlan_summary(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    Skin = request.COOKIES.get('Skin_raw')
    # print(Skin)
    if not Skin:
        Skin = "/static/src/blue.jpg"
    weizhi="ABOTestPlan/Summary"
    # status='0'
    selectItem = {
        # "C38(NB)": [{"Project": "EL531", "Phase0": ["B(FVT)", "C(SIT)", "INV"]},
        #                       {"Project": "EL532", "Phase0": ["B(FVT)", "C(SIT)", "INV"]},
        #                       {"Project": "EL533", "Phase0": ["B(FVT)", "C(SIT)", "INV"]},
        #                       {"Project": "EL534", "Phase0": ["B(FVT)", "C(SIT)", "INV"]}],
        #           "C38(AIO)": [{"Project": "EL535", "Phase0": ["B(FVT)", "C(SIT)", "INV"]},
        #                        {"Project": "EL536", "Phase0": ["B(FVT)", "C(SIT)", "INV"]},
        #                        {"Project": "EL537", "Phase0": ["B(FVT)", "C(SIT)", "INV"]},
        #                        {"Project": "EL538", "Phase0": ["B(FVT)", "C(SIT)", "INV"]}],
        #           "A39": [{"Project": "EL531", "Phase0": ["B(FVT)", "C(SIT)", "INV"]},
        #                   {"Project": "EL532", "Phase0": ["B(FVT)", "C(SIT)", "INV"]},
        #                   {"Project": "EL533", "Phase0": ["B(FVT)", "C(SIT)", "INV"]},
        #                   {"Project": "EL534", "Phase0": ["B(FVT)", "C(SIT)", "INV"]}],
        #           "Other": [{"Project": "ELMV2", "Phase0": ["B(FVT)", "C(SIT)", "INV"]},
        #                     {"Project": "ELMV3", "Phase0": ["B(FVT)", "C(SIT)", "INV"]},
        #                     {"Project": "ELMV4", "Phase0": ["B(FVT)", "C(SIT)", "INV"]}]
    }
    excel_dic = []
    key_list = []
    canExport = 1
    canEdit = 1

    folder_path = settings.MEDIA_ROOT + '/ABOTestPlan/'  # 指定文件夹路径
    subforders = []
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for dirname in dirnames:
            subforders.append(os.path.join(dirpath, dirname).replace(folder_path, "").replace("\\", "/"))
            # print(os.path.join(dirpath, dirname).replace(folder_path, ""))
    subforders_name1 = []
    subforders_name2 = []
    subforders_name3 = []
    for i in subforders:
        if len(i.split("/")) == 1:
            subforders_name1.append(i)
        elif len(i.split("/")) == 2:
            subforders_name2.append(i)
        elif len(i.split("/")) == 3:
            subforders_name3.append(i)
        else:
            print(i)
    for i in subforders_name1:
        projectincustomer = []
        for j in subforders_name2:
            phaseinproject = []
            {"Project": "EL531", "Phase0": ["B(FVT)", "C(SIT)", "INV"]}
            if i in j:
                for k in subforders_name3:
                    if j in k:
                        phaseinproject.append(k.replace(j + "/", ""))
                projectincustomer.append({"Project": j.replace(i + "/", ""), "Phase0": phaseinproject})
        selectItem[i] = projectincustomer
    # print(selectItem)

    if request.method == "POST":
        if request.POST.get('isGetData') == 'first':
            pass


        if request.POST.get('isGetData') == 'SEARCH':
            Customer = request.POST.get('Customer')
            Project = request.POST.get('Project')
            Phase = request.POST.get('Phase')
            Category = request.POST.get('Category')
            print(Customer)
            folder_path = settings.MEDIA_ROOT + '/ABOTestPlan/' + Customer + "/" + Project + "/" + Phase + "/" + Category
            folder_path = folder_path.replace("\\", "/").replace("//", "/")

            file_ext = ['.xls', '.xlsx']

            i = 0
            for path in os.listdir(folder_path):
                path_list = os.path.join(folder_path, path)  # 连接当前目录及文件或文件夹名称
                if os.path.isfile(path_list):  # 判断当前文件或文件夹是否是文件，把文件夹排除
                    if (os.path.splitext(path_list)[1]) in file_ext:  # 判断取得文件的扩展名是否是.xls、.xlsx
                        print(path_list)  # 打印输出
                        i += 1  # 对.xls、.xlsx文件进行计数
            print('目录下共有' + str(i) + '个xls、xlsx文件')
            # excel_dic = read_excel(src_file)[0]
            # print(type(excel_dic))
            # key_list = read_excel(src_file)[1]
            # save_exel(excel_dic,src_file)


        data = {
            "err_ok": "0",
            "select": selectItem,
            "excel_dic": excel_dic,
            "key_list": key_list,
            "canExport": canExport,
            "canEdit": canEdit,
            # "status":status
        }
        # print(type(json.dumps(data)),json.dumps(data))
        return HttpResponse(json.dumps(data), content_type="application/json")
    return render(request, 'ABOTestPlan/ABOTestPlan_Summary.html', locals())