from django import template
from django.conf import settings
import re, os
from django.utils.safestring import mark_safe

register = template.Library()


def get_structure_data(request):
    """处理菜单结构"""
    menu = request.session[settings.SESSION_MENU_KEY]
    all_menu = menu[settings.ALL_MENU_KEY]
    permission_url = menu[settings.PERMISSION_MENU_KEY]
    permission_url_account = str(menu[settings.PERMISSION_MENU_KEY1])
    # print (all_menu)
    # print(permission_url)
    # all_menu = [
    #     {'id': 1, 'title': '订单管理', 'parent_id': None},
    #     {'id': 2, 'title': '库存管理', 'parent_id': None},
    #     {'id': 3, 'title': '生产管理', 'parent_id': None},
    #     {'id': 4, 'title': '生产调查', 'parent_id': None}
    # ]

    # 定制数据结构
    all_menu_dict = {}
    # print("all menue:",all_menu)
    for item in all_menu:
        item['status'] = False#False,False表示不显示，True表示显示，初始默认不显示，后面判断有权限在改成True，要想不管有没有权限都显示，直接全设为True
        item['open'] = False
        item['children'] = []
        all_menu_dict[item['id']] = item
    # print(all_menu_dict)
    # print(permission_url)
    # all_menu_dict = {
    #     1: {'id': 1, 'title': '订单管理', 'parent_id': None, 'status': False, 'open': False, 'children': []},
    #     2: {'id': 2, 'title': '库存管理', 'parent_id': None, 'status': False, 'open': False, 'children': []},
    #     3: {'id': 3, 'title': '生产管理', 'parent_id': None, 'status': False, 'open': False, 'children': []},
    #     4: {'id': 4, 'title': '生产调查', 'parent_id': None, 'status': False, 'open': False, 'children': []}
    # }

    # permission_url = [
    #     {'title': '查看订单', 'url': '/order', 'menu_id': 1},
    #     {'title': '查看库存清单', 'url': '/stock/detail', 'menu_id': 2},
    #     {'title': '查看生产订单', 'url': '/produce/detail', 'menu_id': 3},
    #     {'title': '产出管理', 'url': '/survey/produce', 'menu_id': 4},
    #     {'title': '工时管理', 'url': '/survey/labor', 'menu_id': 4},
    #     {'title': '入库', 'url': '/stock/in', 'menu_id': 2},
    #     {'title': '排单', 'url': '/produce/new', 'menu_id': 3}
    # ]

    request_rul = request.path_info

    for url in permission_url:
        # 添加两个状态：显示 和 展开
        url['status'] = True
        pattern = url['url']
        if url['url'] in permission_url_account:
            url['per'] = True
        else:
            url['open'] = False
        if re.match(pattern, request_rul):
            url['open'] = True
        else:
            url['open'] = False

        # 将url添加到菜单下
        all_menu_dict[url['menu_id']]["children"].append(url)

        # 显示菜单：url 的菜单及上层菜单 status: true
        pid = url['menu_id']
        while pid:
            all_menu_dict[pid]['status'] = True
            pid = all_menu_dict[pid]['parent_id']

        # 展开url上层菜单：url['open'] = True, 其菜单及其父菜单open = True
        if url['open']:
            ppid = url['menu_id']
            while ppid:
                all_menu_dict[ppid]['open'] = True
                ppid = all_menu_dict[ppid]['parent_id']
    # print(permission_url)
    # 整理菜单层级结构：没有parent_id 的为根菜单， 并将有parent_id 的菜单项加入其父项的chidren内
    menu_data = []
    for i in all_menu_dict:
        if all_menu_dict[i]['parent_id']:
            pid = all_menu_dict[i]['parent_id']
            parent_menu = all_menu_dict[pid]
            parent_menu['children'].append(all_menu_dict[i])
        else:
            menu_data.append(all_menu_dict[i])
        # print(menu_data)#如果append括号里面的内容后面发生了变更，append前面的内容也会跟着发生变化
    # print(len(menu_data))
    # testdic = {"a":1,"b":2}
    # print(testdic.items())

    for i in menu_data:
        # print(len(i),i)
        # print(i["title"])
        # print(len(i["children"]), i["children"])
        #
        # for j in i["children"]:
        #     if "children" in j.keys():
        #         print(len(j['children']), j['children'])
        if i['children']:
            if "children" in i['children'][0].keys():#edwin：对有三级菜单，按照第三季级菜单的个数对二级菜单排序，只有二级的不需要排序
                i["children"].sort(key=lambda x: len(x["children"]))
                # for m in i["children"]:
                #     print(len(m["children"]), m["children"])
                for j in i['children']:#第三级菜单则按照title字母顺序排序
                    if j['children']:
                        if "children" in j['children'][0].keys():  # edwin：对有四级菜单，按照第三季级菜单的个数对二级菜单排序，只有二级的不需要排序
                            j["children"].sort(key=lambda x: len(x["children"]))
                    else:
                        j['children'].sort(key=lambda x: x["title"])
    menu_data.sort(key=lambda x: x["title"])  # 第一级菜单按照title字母顺序排序
    # print (menu_data)
    return menu_data


def get_menu_html(menu_data, indexnum):
    """显示：菜单 + [子菜单] + 权限(url)"""
    '''
    el-menu需要router来路由，不识别django的路由，适合前后端分离项目。url路由使用a标签
    '''
    '''
            <el-submenu index=1>
                    <el-menu-item-group title={Group_title}>
                        <a href="/index/"><el-menu-item index="1-1">选项1</el-menu-item></a>
                        <el-submenu index="1-2">
                          <span slot="title">选项4</span>
                          <el-menu-item index="1-2-1">选项1</el-menu-item>
                        </el-submenu>
                    </el-menu-item-group>
        '''
    option_str = """
          <el-submenu index="{index}">
                <span slot="title">{spanname}</span>
                    {sub_menu}
          </el-submenu>
    """

    url_str = """
        <a href="{permission_url}"><el-menu-item index="{index_sub}">{permission_title}</el-menu-item></a>
    """
    url_str_noper = """
            <el-menu-item index="{index_sub}" disabled>{permission_title}</el-menu-item>
        """

    """
     menu_data = [
        {'id': 1, 'title': '订单管理', 'parent_id': None, 'status': True, 'open': False,
         'children': [{'title': '查看订单', 'url': '/order', 'menu_id': 1, 'status': True, 'open': False}]},
        {'id': 2, 'title': '库存管理', 'parent_id': None, 'status': True, 'open': True,
         'children': [{'title': '查看库存清单', 'url': '/stock/detail', 'menu_id': 2, 'status': True, 'open': False},
                      {'title': '入库', 'url': '/stock/in', 'menu_id': 2, 'status': True, 'open': True}]},
        {'id': 3, 'title': '生产管理', 'parent_id': None, 'status': True, 'open': False,
         'children': [{'title': '查看生产订单', 'url': '/produce/detail', 'menu_id': 3, 'status': True, 'open': False},
                      {'title': '排单', 'url': '/produce/new', 'menu_id': 3, 'status': True, 'open': False}]},
        {'id': 4, 'title': '生产调查', 'parent_id': None, 'status': True, 'open': False,
         'children': [{'title': '产出管理', 'url': '/survey/produce', 'menu_id': 4, 'status': True, 'open': False},
                      {'title': '工时管理', 'url': '/survey/labor', 'menu_id': 4, 'status': True, 'open': False}]}
    ]
    """
    # print("menu_data:",menu_data)
    menu_html = ''
    indexnum_sub = 0
    # print(indexnum,"index")
    for item in menu_data:
        indexnum_sub += 1
        if not item['status']: # 如果用户权限不在某个菜单下，即item['status']=False, 不显示
            continue
        else:
            if item.get('url'): # 说明循环到了菜单最里层的url
                if item.get('per'):
                    print(item)
                    menu_html += url_str.format(permission_url=item['url'],
                                                # active="rbac-active" if item['open'] else "",
                                                index_sub=str(indexnum) + "-" + str(indexnum_sub),
                                                permission_title=item['title'].split("_")[2] if len(item['title'].split("_")) >= 2 else item['title'],
                                                # permission_title=item['title'][4:],
                                                )
                else:
                    menu_html += url_str_noper.format(
                                                # active="rbac-active" if item['open'] else "",
                                                index_sub=str(indexnum) + "-" + str(indexnum_sub),
                                                permission_title=item['title'].split("_")[2] if len(
                                                    item['title'].split("_")) >= 2 else item['title'],
                                                # permission_title=item['title'][4:],
                                                )
                # print (menu_html)
                # print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            else:
                # print(item['title'])
                if item.get('children'):
                    # print(item['title'])
                    sub_menu = get_menu_html(item['children'], str(indexnum) + "-" + str(indexnum_sub))

                    menu_html += option_str.format(index=str(indexnum) + "-" + str(indexnum_sub), spanname=item['title'].split("_")[2] if len(item['title'].split("_"))>=2 else item['title'],
                                                   sub_menu=sub_menu)  # ,
                    # display="" if item['open'] else "rbac-hide",
                    # status="open" if item['open'] else "close")
                else:
                    sub_menu = ""


                # print(menu_html)
                # print('================================================================================================')
    # print(menu_html)
    # print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    return menu_html


@register.simple_tag
def rbac_menu(request):
    """
    显示多级菜单：请求过来 -- 拿到session中的菜单，权限数据 -- 处理数据 -- 作显示
    返回多级菜单：数据处理部分抽象出来由单独的函数处理；渲染部分也抽象出来由单独函数处理
    :param request:
    :return:
    """
    # print(request.session[settings.SESSION_MENU_KEY])
    menu_data = get_structure_data(request)
    # print(menu_data)
    menu_html = get_menu_html(menu_data, 2)
    # print(menu_html,111)

    return mark_safe(menu_html)
    # 因为标签无法使用safe过滤器，这里用mark_safe函数来实现


@register.simple_tag
def rbac_css():
    """
    rabc要用到的css文件路径，并读取返回；注意返回字符串用mark_safe，否则传到模板会转义
    :return: 
    """
    css_path = os.path.join('app01', 'style_script','rbac.css')
    css = open(css_path,'r',encoding='utf-8').read()
    return mark_safe(css)


@register.simple_tag
def rbac_js():
    """
    rabc要用到的js文件路径，并读取返回
    :return: 
    """
    js_path = os.path.join('app01', 'style_script', 'rbac.js')
    js = open(js_path, 'r', encoding='utf-8').read()
    return mark_safe(js)



