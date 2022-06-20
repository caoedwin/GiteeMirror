from django.db import models


class Menu(models.Model):
    """
    菜单
    """
    title = models.CharField(max_length=32, unique=True)
    parent = models.ForeignKey("Menu", null=True, blank=True,on_delete=models.SET_NULL ,)
    # 定义菜单间的自引用关系
    # 权限url 在 菜单下；菜单可以有父级菜单；还要支持用户创建菜单，因此需要定义parent字段（parent_id）
    # blank=True 意味着在后台管理中填写可以为空，根菜单没有父级菜单

    def __str__(self):
        # 显示层级菜单
        title_list = [self.title]
        p = self.parent
        while p:
            title_list.insert(0, p.title)
            p = p.parent
        return '-'.join(title_list)


class Permission(models.Model):
    """
    权限
    """
    title = models.CharField(max_length=32, unique=True)
    url = models.CharField(max_length=128, null=True,default='')
    menu = models.ForeignKey("Menu", null=True, blank=True,on_delete=models.SET_NULL)
    Proj_perm=models.ManyToManyField("Project_Spec")
    def __str__(self):
        # 显示带菜单前缀的权限
        # return '{menu}---{permission}'.format(menu=self.menu, permission=self.title)
        return '{Proj_perm}---{permission}'.format(Proj_perm=self.Proj_perm, permission=self.title)


class Role(models.Model):
    """
    角色：绑定权限
    """
    title = models.CharField(max_length=32, unique=True)

    permissions = models.ManyToManyField("Permission")
    # 定义角色和权限的多对多关系

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """
    用户：划分角色
    """
    account = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=64)
    username = models.CharField(max_length=32)
    email = models.EmailField()

    roles = models.ManyToManyField("Role", blank=True,)
    perm = models.ManyToManyField("Permission", blank=True,)
    # 定义用户和角色的多对多关系

    class Meta:
        verbose_name = 'UserInfo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class Item_Spec(models.Model):
    """
    角色：绑定权限
    """
    Cus_I = models.CharField('Cus_I',max_length=32,default="")

    Item_I = models.CharField('Item_I',max_length=200,default="",unique=True)
    Category = models.CharField('Catgory', max_length=20, null=True, blank=True, default="")
    Item_Description = models.CharField('Item_Description', max_length=200, default="")
    Sample_Demand=models.CharField('Sample_Demand', max_length=100, null=True, blank=True, default="")
    # 定义角色和权限的多对多关系

    def __str__(self):
        # return '{Cus_I}---{Item_I}'.format(Cus_I=self.Cus_I, Item_I=self.Item_I)
        return self.Item_I


class Project_Spec(models.Model):
    """
    角色：绑定权限
    """
    Cus_P = models.CharField('Cus_P',max_length=32,default="")
    Project_P = models.CharField('Project_P', max_length=32, default="")
    Phase_P = models.CharField('Phase_P', max_length=20, default="")
    Item_P = models.ManyToManyField('Item_Spec')
    Owner_P = models.ManyToManyField('UserInfo')
    # 定义角色和权限的多对多关系

    def __str__(self):
        # return self.Project_P
        return '{Cus_P}---{Project_P}---{Phase_P}'.format(Cus_P=self.Cus_P, Project_P=self.Project_P, Phase_P=self.Phase_P)