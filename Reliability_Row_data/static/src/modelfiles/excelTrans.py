# -*- coding:utf-8 -*-
import pandas as pd
import pprint
from pathlib import Path
import os
import warnings

# warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

current_work_dir = os.path.dirname(__file__)  # 当前文件所在的目录
os.path.abspath('.')
# print(current_work_dir)
# with open('current_work_dir.txt', 'w') as f:  # 设置文件对象
#     print(current_work_dir, os.path.abspath('.'), file=f)

try:
    src_file = os.path.abspath('.') + "\Project1.xlsx"
    # 每次都需要修改的路径
    # with open('src_file.txt', 'w') as f:  # 设置文件对象
    #     print(src_file, file=f)
    # sheet_name默认为0，即读取第一个sheet的数据
    # df = pd.read_excel(src_file, header=1, sheet_name='SW Test planning')
    Customer = "C38(NB)"
    sheetnum = input("请选择模板。B,C,phase模板请输入2，FFRT模板输入3：")
    # print(sheetnum)
    if sheetnum == '2':
        df = pd.read_excel(src_file, header=5, sheet_name=int(sheetnum)).iloc[:, 1:]#‘,’前面是行，后面是列，sheet_name指定sheet，可是是int第几个，可以是名称，header从第几行开始读取
        # print(df.shape)#获取行数列数
        if 'Unnamed: 26' in df.columns:
            # print(1)
            df = df.drop(labels='Unnamed: 26', axis=1)
            print(df.shape)  # 获取行数列数
        # # 显示所有列
        pd.set_option('display.max_columns', None)
        # # 显示所有行
        # pd.set_options('display.max_rows', None)
        # print(df.columns)
        # print(df.iloc[:1, :])
        # pprint.pprint(df)
        # sheet = pd.read_excel(src_file, sheet_name=0)
        # print(sheet)
        # print(df)
        # 转换字典
        # df_dict = df.to_dict(orient='records')
        # 转换列表
        # df_list = df.values
        # # pprint.pprint(df_list)
        # print(df_list[0])
        # 注意带上inplace=True参数用于更新作用于本数据集，而不是返回一个新的数据集。
        # df.rename(columns={'6-英语':'english'},inplace=True)
        # 如果需要重命名行索引，可以通过df.rename(index={‘原索引’:‘重命名索引’})的方式进行重命名。
        # 更多的，如果要重命名多个列，可以传入一个需要重命名的多个字典值，进行多个列的重命名。
        # df[['1-学号','2-姓名','3-年龄']].rename(columns={'1-学号':'ID','2-姓名':'name','3-年龄':'age'})
        columnsRename = {
                         'Case ID': 'ItemNo_d', 'Case name': 'Item_d', 'Test Items': 'TestItems', 'Version': 'Version', 'Release date': 'ReleaseDate', 'Owner': 'Owner', 'Priority': 'Priority',
                         'TDMS \nTotal time\n(A+U)': 'TDMSTotalTime', 'Base time': 'BaseTime', '(TDMS)\nUnattended \ntime': 'TDMSUnattendedTime',
                         'Base time-Automation\n(1SKU)': 'BaseAotomationTime1SKU', 'Chramshell': 'Chramshell', 'Convertible': 'ConvertibaleNBMode',
                         'Unnamed: 14': 'ConvertibaleYogaPadMode', 'Detachable': 'DetachablePadMode', 'Unnamed: 16': 'DetachableWDockmode',
                         'Phase': 'PhaseFVT', 'Unnamed: 18': 'PhaseSIT',#B,C 与FFRT不一样
                         'Coverage': 'Coverage', 'Feature Support': 'FeatureSupport', 'Base time-support': 'BaseTimeSupport', 'TE': 'TE', 'Schedule': 'Schedule',
                         'Project test SKU-follow matrix': 'ProjectTestSKUfollowMatrix', 'Time w/ Config-follow matrix\n(?SKU)': 'TimewConfigFollowmatrix',
                         'Config-Automation Item': 'ConfigAutomationItem', 'Config-Automation time': 'ConfigAutomationTime', 'Config-Leverage Item': 'ConfigLeverageItem',
                         'Config-Leverage time': 'ConfigLeverageTime', 'Comments': 'CommentsLeverage', 'Config-Smart Item': 'ConfigSmartItem',
                         'Config-Smart Item占总case比例': 'ConfigSmartItemPer', 'Config-Smart time': 'ConfigSmartTime', 'Comments.1': 'CommentsSmart', 'Project test SKU-Optimize': 'ProjectTestSKUOptimize',
                         'Attend time-Optimize': 'AttendTimeOptimize', 'Planning after Optimize': 'SKU1', 'Unnamed: 39': 'SKU2', 'Unnamed: 40': 'SKU3', 'Unnamed: 41': 'SKU4', 'Unnamed: 42': 'SKU5',
                         'Unnamed: 43': 'SKU6', 'Unnamed: 44': 'SKU7', 'Unnamed: 45': 'SKU8', 'Unnamed: 46': 'SKU9', 'Unnamed: 47': 'SKU10', 'Config-Retest Cycle': 'ConfigRetestCycle',
                         'Config-Retest SKU': 'ConfigRetestSKU', 'Config-Retest time': 'ConfigRetestTime',
                         }
        if 'Unnamed: 48' in df.columns:
            columnsRename["Unnamed: 48"] = "SKU11"
        if 'Unnamed: 49' in df.columns:
            columnsRename["Unnamed: 49"] = "SKU12"
        if 'Unnamed: 50' in df.columns:
            columnsRename["Unnamed: 50"] = "SKU13"
        if 'Unnamed: 51' in df.columns:
            columnsRename["Unnamed: 51"] = "SKU14"
        if 'Unnamed: 52' in df.columns:
            columnsRename["Unnamed: 52"] = "SKU15"
        if 'Unnamed: 53' in df.columns:
            columnsRename["Unnamed: 53"] = "SKU16"
        if 'Unnamed: 54' in df.columns:
            columnsRename["Unnamed: 54"] = "SKU17"
        if 'Unnamed: 55' in df.columns:
            columnsRename["Unnamed: 55"] = "SKU18"
        if 'Unnamed: 56' in df.columns:
            columnsRename["Unnamed: 56"] = "SKU19"
        if 'Unnamed: 57' in df.columns:
            columnsRename["Unnamed: 57"] = "SKU20"
        if 'Unnamed: 58' in df.columns:
            columnsRename["Unnamed: 58"] = "SKU21"
        if 'Unnamed: 59' in df.columns:
            columnsRename["Unnamed: 59"] = "SKU22"
        if 'Unnamed: 60' in df.columns:
            columnsRename["Unnamed: 60"] = "SKU23"
        if 'Unnamed: 61' in df.columns:
            columnsRename["Unnamed: 61"] = "SKU24"
        if 'Unnamed: 62' in df.columns:
            columnsRename["Unnamed: 62"] = "SKU25"
        if 'Unnamed: 63' in df.columns:
            columnsRename["Unnamed: 63"] = "SKU26"
        if 'Unnamed: 64' in df.columns:
            columnsRename["Unnamed: 64"] = "SKU27"
        if 'Unnamed: 65' in df.columns:
            columnsRename["Unnamed: 65"] = "SKU28"
        if 'Unnamed: 66' in df.columns:
            columnsRename["Unnamed: 66"] = "SKU29"
        if 'Unnamed: 67' in df.columns:
            columnsRename["Unnamed: 67"] = "SKU30"
        if 'Unnamed: 68' in df.columns:
            columnsRename["Unnamed: 68"] = "SKU31"
        if 'Unnamed: 69' in df.columns:
            columnsRename["Unnamed: 69"] = "SKU32"
        if 'Unnamed: 70' in df.columns:
            columnsRename["Unnamed: 70"] = "SKU33"
        if 'Unnamed: 71' in df.columns:
            columnsRename["Unnamed: 71"] = "SKU34"
        if 'Unnamed: 72' in df.columns:
            columnsRename["Unnamed: 72"] = "SKU35"
        if 'Unnamed: 73' in df.columns:
            columnsRename["Unnamed: 73"] = "SKU36"
        if 'Unnamed: 74' in df.columns:
            columnsRename["Unnamed: 74"] = "SKU37"
        if 'Unnamed: 75' in df.columns:
            columnsRename["Unnamed: 75"] = "SKU38"
        if 'Unnamed: 76' in df.columns:
            columnsRename["Unnamed: 76"] = "SKU39"
        if 'Unnamed: 77' in df.columns:
            columnsRename["Unnamed: 77"] = "SKU40"

        df.rename(columns=columnsRename, inplace=True)
        # print(df.iloc[:1, :])
        # print(df.columns) #获取表头
        # df = df.drop([0], axis=0)
        # df = df.drop([1], axis=0)
        # df = df.drop([2], axis=0)
        # 删除data中索引为0和1的行
        df = df.drop(index=[0, 1, 2])

        # 删除data中列名为“source”和“target”的列
        # df.drop(columns=['source', 'target'])
        # 参数axis为0表示在0轴（列）上搜索名为“姓名”的对象，然后删除对象“姓名”对应的行。
        # df.drop("姓名", axis=0)
        df = df.drop(index=df[(df.Owner == '.Mins')].index.tolist())
        # 会将标签重新从零开始顺序排序,使用参数设置drop=True删除旧的索引序列
        df = df.reset_index(drop=True)
        print(df.shape)  # 获取行数列数
        # print(df.iloc[2188:, :])

        # print(index)
        # print(range(0,len(index)))

        # 参数axis为1表示在1轴（行）上搜索名为“姓名”的对象，然后删除对象“姓名”对应的列。
        # df.drop("姓名", axis=1)

        # 插入列
        df.insert(5, "Category", value='')
        df.insert(6, "Category2", value='')
        # 合并单元格
        df['ItemNo_d'] = df['ItemNo_d'].ffill()
        df['Item_d'] = df['Item_d'].ffill()
        df['Version'] = df['Version'].ffill()
        df['ReleaseDate'] = df['ReleaseDate'].ffill()

        index = df[(df.Owner == '.Hrs')].index.tolist()
        print(len(index))
        # print(df[(df.Owner == '.Hrs')])
        sub_Category = ['Pre-Installed App', 'WiGig Dock', 'USB Dock', 'Folio Case(Draft)', 'USB-C Dock', 'Thunderbolt Dock', 'Hybrid Dock',
                        'Power USB-C  Travel Hub & USB-C Mini dock', 'BT Folio Case', 'Lenovo 3-IN-1 Hub', 'USB-C Travel Hub Gen2',
                        'Lenovo USB-C 7-in-1 Hub']
        for num in range(0, len(index)):
            # print(num)
            # print(data.loc[data['部门'] == 'A', ['姓名', '工资']])  # 部门为A，打印姓名和工资
            # print(data.loc[data['工资'] < 3000, ['姓名', '工资']])  # 查找工资小于3000的人
            # print(df['ItemNo_d'][index[num]])
            now_Category = '只记大类'
            if df['ItemNo_d'][index[num]] not in sub_Category:
                now_Category = df['ItemNo_d'][index[num]]
            if num != len(index)-1:
                df.loc[index[num]: index[num+1], 'Category'] = now_Category # 只记大类
                df.loc[index[num]: index[num + 1], 'Category2'] = df['ItemNo_d'][index[num]]
            else:#最后一个类别
                df.loc[index[num]:df.shape[0], 'Category'] = now_Category  # 只记大类
                df.loc[index[num]:df.shape[0], 'Category2'] = df['ItemNo_d'][index[num]]
        df = df.drop(index=df[(df.Owner == '.Hrs')].index.tolist())
        df = df.fillna('')# 替换
        df = df.drop(index=df[(df.Owner == '')].index.tolist())
        # df = df.drop(index=df[(df.TestItems == '')].index.tolist())
        # print(df.head(8))
        # 会将标签重新从零开始顺序排序,使用参数设置drop=True删除旧的索引序列
        df = df.reset_index(drop=True)

        phaseinexcel = pd.read_excel(src_file, header=1, sheet_name=int(sheetnum)).iloc[0:3, 1:3]  # ‘,’前面是行，后面是列，sheet_name指定sheet，可是是int第几个，可以是名称，header从第几行开始读取
        # print(phaseinexcel)
        # print(phaseinexcel.columns[0])
        Phase = ''
        if "B(FVT)" in phaseinexcel.columns[0]:
            Phase = "B(FVT)"
        elif "C(SIT)" in phaseinexcel.columns[0]:
            Phase = "C(SIT)"
        df.insert(0, "Customer", value=Customer)
        df.insert(1, "Phase", value=Phase)
        # wr_data = df.to_csv('out.csv')
        # 第一个参数为保存的文件名，注意，不能为空
        # sheet_name
        # 设置excel文件脚注
        # index = False
        # 这个意思是不将索引写入到文件中
        # print(df.iloc[1962:1965, :])
        df['ReleaseDate'] = df['ReleaseDate'].apply(
            lambda x: x.strftime('%Y-%m-%d') if 'datetime.datetime' in str(type(x)) else x)  # 批量类型转换
        print(df.shape)  # 获取行数列数
        with open('data.txt', 'w') as f:  # 设置文件对象
            print(df.shape, df.columns, file=f)
        df.to_excel('upload.xlsx', sheet_name="sheet1", index=False, engine='xlsxwriter')# engine默认是openpyxl， openpyxl生成的文件DDIS上传不了


        # write = pd.ExcelWriter("test.xlsx")  # 新建xlsx文件。
        # df.to_excel(write, sheet_name='Sheet1', index=False)  # 写入文件的Sheet1
        # write.save()  # 这里一定要保存
        # df.to_excel('upload.xlsx', sheet_name="sheet1", index=False, engine='openpyxl')

    if sheetnum == '3':
        df = pd.read_excel(src_file, header=5, sheet_name=int(sheetnum)).iloc[:, 1:]#‘,’前面是行，后面是列，sheet_name指定sheet，可是是int第几个，可以是名称，header从第几行开始读取
        # print(df.shape)#获取行数列数
        if 'Unnamed: 24' in df.columns:#比B,Cphase少了两栏'TDMS \nTotal time\n(A+U)': 'TDMSTotalTime','Unnamed: 18': 'PhaseSIT',
            # print(1)
            df = df.drop(labels='Unnamed: 24', axis=1)
            print(df.shape)  # 获取行数列数
        # # 显示所有列
        pd.set_option('display.max_columns', None)
        # # 显示所有行
        # pd.set_options('display.max_rows', None)
        # print(df.columns)
        # print(df.iloc[:1, :])
        # pprint.pprint(df)
        # sheet = pd.read_excel(src_file, sheet_name=0)
        # print(sheet)
        # print(df)
        # 转换字典
        # df_dict = df.to_dict(orient='records')
        # 转换列表
        # df_list = df.values
        # # pprint.pprint(df_list)
        # print(df_list[0])
        # 注意带上inplace=True参数用于更新作用于本数据集，而不是返回一个新的数据集。
        # df.rename(columns={'6-英语':'english'},inplace=True)
        # 如果需要重命名行索引，可以通过df.rename(index={‘原索引’:‘重命名索引’})的方式进行重命名。
        # 更多的，如果要重命名多个列，可以传入一个需要重命名的多个字典值，进行多个列的重命名。
        # df[['1-学号','2-姓名','3-年龄']].rename(columns={'1-学号':'ID','2-姓名':'name','3-年龄':'age'})
        columnsRename = {
                         'Case ID': 'ItemNo_d', 'Case name': 'Item_d', 'Test Items': 'TestItems', 'Version': 'Version', 'Release date': 'ReleaseDate', 'Owner': 'Owner', 'Priority': 'Priority',
                         # 'TDMS \nTotal time\n(A+U)': 'TDMSTotalTime',
                         'Base time': 'BaseTime', '(TDMS)\nUnattended \ntime': 'TDMSUnattendedTime',
                         'Base time-Automation\n(1SKU)': 'BaseAotomationTime1SKU', 'Chramshell': 'Chramshell', 'Convertible': 'ConvertibaleNBMode',
                         'Unnamed: 13': 'ConvertibaleYogaPadMode',
                         'Detachable': 'DetachablePadMode',
                         'Unnamed: 15': 'DetachableWDockmode',
                         'Phase': 'PhaseFFRT',
                         #'Unnamed: 18': 'PhaseSIT',#B,C 与FFRT不一样
                         'Coverage': 'Coverage', 'Feature Support': 'FeatureSupport', 'Base time-support': 'BaseTimeSupport', 'TE': 'TE', 'Schedule': 'Schedule',
                         'Project test SKU-follow matrix': 'ProjectTestSKUfollowMatrix', 'Time w/ Config-follow matrix\n(?SKU)': 'TimewConfigFollowmatrix',
                         'Config-Automation Item': 'ConfigAutomationItem', 'Config-Automation time': 'ConfigAutomationTime', 'Config-Leverage Item': 'ConfigLeverageItem',
                         'Config-Leverage time': 'ConfigLeverageTime', 'Comments': 'CommentsLeverage', 'Config-Smart Item': 'ConfigSmartItem',
                         'Config-Smart Item占总case比例': 'ConfigSmartItemPer', 'Config-Smart time': 'ConfigSmartTime', 'Comments.1': 'CommentsSmart', 'Project test SKU-Optimize': 'ProjectTestSKUOptimize',
                         'Attend time-Optimize': 'AttendTimeOptimize', 'Planning after Optimize': 'SKU1',
                         'Unnamed: 37': 'SKU2', 'Unnamed: 38': 'SKU3', 'Unnamed: 39': 'SKU4', 'Unnamed: 40': 'SKU5',
                         'Unnamed: 41': 'SKU6', 'Unnamed: 42': 'SKU7', 'Unnamed: 43': 'SKU8', 'Unnamed: 44': 'SKU9', 'Unnamed: 45': 'SKU10',
                         'Config-Retest Cycle': 'ConfigRetestCycle',
                         'Config-Retest SKU': 'ConfigRetestSKU', 'Config-Retest time': 'ConfigRetestTime',
                         }
        if 'Unnamed: 46' in df.columns:
            columnsRename["Unnamed: 46"] = "SKU11"
        if 'Unnamed: 47' in df.columns:
            columnsRename["Unnamed: 47"] = "SKU12"
        if 'Unnamed: 48' in df.columns:
            columnsRename["Unnamed: 48"] = "SKU13"
        if 'Unnamed: 49' in df.columns:
            columnsRename["Unnamed: 49"] = "SKU14"
        if 'Unnamed: 50' in df.columns:
            columnsRename["Unnamed: 50"] = "SKU15"
        if 'Unnamed: 51' in df.columns:
            columnsRename["Unnamed: 51"] = "SKU16"
        if 'Unnamed: 52' in df.columns:
            columnsRename["Unnamed: 52"] = "SKU17"
        if 'Unnamed: 53' in df.columns:
            columnsRename["Unnamed: 53"] = "SKU18"
        if 'Unnamed: 54' in df.columns:
            columnsRename["Unnamed: 54"] = "SKU19"
        if 'Unnamed: 55' in df.columns:
            columnsRename["Unnamed: 55"] = "SKU20"
        if 'Unnamed: 56' in df.columns:
            columnsRename["Unnamed: 56"] = "SKU21"
        if 'Unnamed: 57' in df.columns:
            columnsRename["Unnamed: 57"] = "SKU22"
        if 'Unnamed: 68' in df.columns:
            columnsRename["Unnamed: 58"] = "SKU23"
        if 'Unnamed: 59' in df.columns:
            columnsRename["Unnamed: 59"] = "SKU24"
        if 'Unnamed: 60' in df.columns:
            columnsRename["Unnamed: 60"] = "SKU25"
        if 'Unnamed: 61' in df.columns:
            columnsRename["Unnamed: 61"] = "SKU26"
        if 'Unnamed: 62' in df.columns:
            columnsRename["Unnamed: 62"] = "SKU27"
        if 'Unnamed: 63' in df.columns:
            columnsRename["Unnamed: 63"] = "SKU28"
        if 'Unnamed: 64' in df.columns:
            columnsRename["Unnamed: 64"] = "SKU29"
        if 'Unnamed: 65' in df.columns:
            columnsRename["Unnamed: 65"] = "SKU30"
        if 'Unnamed: 66' in df.columns:
            columnsRename["Unnamed: 66"] = "SKU31"
        if 'Unnamed: 67' in df.columns:
            columnsRename["Unnamed: 67"] = "SKU32"
        if 'Unnamed: 68' in df.columns:
            columnsRename["Unnamed: 68"] = "SKU33"
        if 'Unnamed: 69' in df.columns:
            columnsRename["Unnamed: 69"] = "SKU34"
        if 'Unnamed: 70' in df.columns:
            columnsRename["Unnamed: 70"] = "SKU35"
        if 'Unnamed: 71' in df.columns:
            columnsRename["Unnamed: 71"] = "SKU36"
        if 'Unnamed: 72' in df.columns:
            columnsRename["Unnamed: 72"] = "SKU37"
        if 'Unnamed: 73' in df.columns:
            columnsRename["Unnamed: 73"] = "SKU38"
        if 'Unnamed: 74' in df.columns:
            columnsRename["Unnamed: 74"] = "SKU39"
        if 'Unnamed: 75' in df.columns:
            columnsRename["Unnamed: 75"] = "SKU40"

        df.rename(columns=columnsRename, inplace=True)
        # print(df.iloc[:1, :])
        # print(df.columns) #获取表头
        # df = df.drop([0], axis=0)
        # df = df.drop([1], axis=0)
        # df = df.drop([2], axis=0)
        # 删除data中索引为0和1的行
        df = df.drop(index=[0, 1, 2])

        # 删除data中列名为“source”和“target”的列
        # df.drop(columns=['source', 'target'])
        # 参数axis为0表示在0轴（列）上搜索名为“姓名”的对象，然后删除对象“姓名”对应的行。
        # df.drop("姓名", axis=0)
        df = df.drop(index=df[(df.Owner == '.Mins')].index.tolist())
        # 会将标签重新从零开始顺序排序,使用参数设置drop=True删除旧的索引序列
        df = df.reset_index(drop=True)
        print(df.shape)  # 获取行数列数
        # print(df.iloc[2188:, :])

        # print(index)
        # print(range(0,len(index)))

        # 参数axis为1表示在1轴（行）上搜索名为“姓名”的对象，然后删除对象“姓名”对应的列。
        # df.drop("姓名", axis=1)

        # 插入列
        df.insert(5, "Category", value='')
        df.insert(6, "Category2", value='')
        # 合并单元格
        df['ItemNo_d'] = df['ItemNo_d'].ffill()
        df['Item_d'] = df['Item_d'].ffill()
        df['Version'] = df['Version'].ffill()
        df['ReleaseDate'] = df['ReleaseDate'].ffill()

        index = df[(df.Owner == '.Hrs')].index.tolist()
        print(len(index))
        # print(df[(df.Owner == '.Hrs')])
        sub_Category = ['Pre-Installed App', 'WiGig Dock', 'USB Dock', 'Folio Case(Draft)', 'USB-C Dock', 'Thunderbolt Dock', 'Hybrid Dock',
                        'Power USB-C  Travel Hub & USB-C Mini dock', 'BT Folio Case', 'Lenovo 3-IN-1 Hub', 'USB-C Travel Hub Gen2',
                        'Lenovo USB-C 7-in-1 Hub']
        for num in range(0, len(index)):
            # print(num)
            # print(data.loc[data['部门'] == 'A', ['姓名', '工资']])  # 部门为A，打印姓名和工资
            # print(data.loc[data['工资'] < 3000, ['姓名', '工资']])  # 查找工资小于3000的人
            # print(df['ItemNo_d'][index[num]])
            now_Category = '只记大类'
            if df['ItemNo_d'][index[num]] not in sub_Category:
                now_Category = df['ItemNo_d'][index[num]]
            if num != len(index)-1:
                df.loc[index[num]: index[num+1], 'Category'] = now_Category # 只记大类
                df.loc[index[num]: index[num + 1], 'Category2'] = df['ItemNo_d'][index[num]]
            else:#最后一个类别
                df.loc[index[num]:df.shape[0], 'Category'] = now_Category  # 只记大类
                df.loc[index[num]:df.shape[0], 'Category2'] = df['ItemNo_d'][index[num]]
        df = df.drop(index=df[(df.Owner == '.Hrs')].index.tolist())
        df = df.fillna('')# 替换
        df = df.drop(index=df[(df.Owner == '')].index.tolist())
        # df = df.drop(index=df[(df.TestItems == '')].index.tolist())
        # print(df.head(8))
        # 会将标签重新从零开始顺序排序,使用参数设置drop=True删除旧的索引序列
        df = df.reset_index(drop=True)

        phaseinexcel = pd.read_excel(src_file, header=1, sheet_name=int(sheetnum)).iloc[0:3, 1:3]  # ‘,’前面是行，后面是列，sheet_name指定sheet，可是是int第几个，可以是名称，header从第几行开始读取
        # print(phaseinexcel)
        # print(phaseinexcel.columns[0])
        Phase = ''
        if "FFRT" in phaseinexcel.columns[0]:
            Phase = "FFRT"
        df.insert(0, "Customer", value=Customer)
        df.insert(1, "Phase", value=Phase)
        # wr_data = df.to_csv('out.csv')
        # 第一个参数为保存的文件名，注意，不能为空
        # sheet_name
        # 设置excel文件脚注
        # index = False
        # 这个意思是不将索引写入到文件中
        # print(df.iloc[1962:1965, :])
        df['ReleaseDate'] = df['ReleaseDate'].apply(
            lambda x: x.strftime('%Y-%m-%d') if 'datetime.datetime' in str(type(x)) else x)  # 批量类型转换
        print(df.shape)  # 获取行数列数

        with open('data.txt', 'w') as f:  # 设置文件对象
            print(df.shape, df.columns, file=f)

        df.to_excel('upload.xlsx', sheet_name="sheet1", index=False, engine='xlsxwriter')                                                                                                       # engine默认是openpyxl， openpyxl生成的文件DDIS上传不了

        # write = pd.ExcelWriter("test.xlsx")  # 新建xlsx文件。
        # df.to_excel(write, sheet_name='Sheet1', index=False)  # 写入文件的Sheet1
        # write.save()  # 这里一定要保存
        # df.to_excel('upload.xlsx', sheet_name="data", index=False, engine='openpyxl')
        # df.to_excel('upload.xlsx', sheet_name="data", index=False, engine=None)
except Exception as e:
    with open('error.txt', 'w') as f:  # 设置文件对象
        print(e, file=f)
# designer 设计的界面
# import sys
# import excel
# from PyQt5.QtWidgets import QApplication, QMainWindow
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     MainWindow = QMainWindow()
#     ui = excel.Ui_Dialog()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
def show_messagebox():
    choice = QMessageBox.information(None, 'Excel转化', '%s-%s模板转换已完成' % ("C38(NB)", Phase),
                         QMessageBox.Ok)  # 1



if __name__ == '__main__':
    app = QApplication(sys.argv) #没有无法使用
    demo = show_messagebox()
#
# '''
#
# 消息对话框：QMessageBox
#
#
# 1. 关于对话框
# 2. 错误对话框
# 3. 警告对话框
# 4. 提问对话框
# 5. 消息对话框
#
#
# 有2点差异
# 1. 显示的对话框图标可能不同
# 2. 显示的按钮是不一样的
#
# '''
# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
#
#
# class QMessageBoxDemo(QWidget):
#     def __init__(self):
#         super(QMessageBoxDemo, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('QMessageBox案例')
#         self.resize(300, 400)
#         layout = QVBoxLayout()
#         self.button1 = QPushButton()
#         self.button1.setText('显示关于对话框')
#         self.button1.clicked.connect(self.showDialog)
#         self.button2 = QPushButton()
#         self.button2.setText('显示消息对话框')
#         self.button2.clicked.connect(self.showDialog)
#         self.button3 = QPushButton()
#         self.button3.setText('显示警告对话框')
#         self.button3.clicked.connect(self.showDialog)
#         self.button4 = QPushButton()
#         self.button4.setText('显示错误对话框')
#         self.button4.clicked.connect(self.showDialog)
#         self.button5 = QPushButton()
#         self.button5.setText('显示提问对话框')
#         self.button5.clicked.connect(self.showDialog)
#         layout.addWidget(self.button1)
#         layout.addWidget(self.button2)
#         layout.addWidget(self.button3)
#         layout.addWidget(self.button4)
#         layout.addWidget(self.button5)
#         self.setLayout(layout)
#
#     def showDialog(self):
#         text = self.sender().text()
#         if text == '显示关于对话框':
#             QMessageBox.about(self, '关于', '这是一个关于对话框')
#         elif text == '显示消息对话框':
#             reply = QMessageBox.information(self, '消息', '这是一个消息对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
#             print(reply == QMessageBox.Yes)
#         elif text == '显示警告对话框':
#             QMessageBox.warning(self, '警告', '这是一个警告对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
#         elif text == '显示错误对话框':
#             QMessageBox.critical(self, '警告', '这是一个警告对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
#         elif text == '显示提问对话框':
#             QMessageBox.question(self, '警告', '这是一个警告对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = QMessageBoxDemo()
#     window.show()
#
#     sys.exit(app.exec_())