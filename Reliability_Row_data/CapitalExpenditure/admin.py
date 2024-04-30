from django.contrib import admin

# Register your models here.
from .models import CapitalExpenditure

@admin.register(CapitalExpenditure)
class CapitalExpenditureAdmin(admin.ModelAdmin):

    list_display = (
        'PlanYear', 'BudgetCode', 'Investment_Nature', 'Attribute_Code', 'Application_Department', 'Device_Name', 'Usage_Description',
        'Specifications', 'Acceptance_Month', 'Budget_Quantity', 'Estimated_Original_Currency', 'Estimated_Original_Price', 'Equivalent_To_RMB', 'Payment_Terms', 'Depreciation_Months', 'Accounting_Subjects',
        'Automated_Or_Not', 'Project_Code', 'Current_Situation', 'Applicable_Scope', 'Investment_Purpose', 'Investment_Purpose_Des',
        'Potential_Issues', 'Potential_Issues_Des', 'Tighten_Expenses', 'Annual_Increase_PerYear', 'Investment_Benefits_PerYear', 'Cash_Inflows_PerYear',
        'Payback_Period', 'Subscription_Status', 'Subscription_Quantity', 'Subscription_Amount', 'Entry_Amount',
                    )
    # 列表里显示想要显示的字段
    list_per_page = 500
    # 满50条数据就自动分页
    ordering = ('-PlanYear',)
    #后台数据列表排序方式
    list_display_links = (
         'PlanYear', 'BudgetCode', 'Investment_Nature', 'Attribute_Code', 'Application_Department', 'Device_Name', 'Usage_Description',
        'Specifications', 'Acceptance_Month', 'Budget_Quantity', 'Estimated_Original_Currency', 'Estimated_Original_Price', 'Equivalent_To_RMB', 'Payment_Terms', 'Depreciation_Months', 'Accounting_Subjects',
        'Automated_Or_Not', 'Project_Code', 'Current_Situation', 'Applicable_Scope', 'Investment_Purpose', 'Investment_Purpose_Des',
        'Potential_Issues', 'Potential_Issues_Des', 'Tighten_Expenses', 'Annual_Increase_PerYear', 'Investment_Benefits_PerYear', 'Cash_Inflows_PerYear',
        'Payback_Period', 'Subscription_Status', 'Subscription_Quantity', 'Subscription_Amount', 'Entry_Amount',
                    )
    # 设置哪些字段可以点击进入编辑界面
    # list_editable = ('Object',)
    # 筛选器
    list_filter = (
        'PlanYear',
        'BudgetCode',
        'Application_Department',
        # ('Customer', UnionFieldListFilter),
        # ('Phase', UnionFieldListFilter),
    )
    search_fields = ('PlanYear', 'BudgetCode', 'Application_Department',)  # 搜索字段
    # date_hierarchy = 'Start_time'  # 详细时间分层筛选