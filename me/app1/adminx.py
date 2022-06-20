import xadmin
from .models import TestLog
class TestLogAdmin(object):
  list_display = ['Project', 'Unit', 'Phase', 'Testitem', 'Tester', 'Comments', 'Start_time', 'End_time','Result_time','Result']
  search_fields = ['Project', ]
  list_editable = ['Project', 'Unit', 'Phase', 'Testitem', 'Tester', 'Comments', 'Start_time', 'End_time','Result_time','Result']
  list_filter = ['Project', 'Unit', 'Phase', 'Testitem', 'Tester', 'Comments', 'Start_time', 'End_time','Result_time','Result']

# class OrderDetailAdmin(object):
#     list_display = ['goods', 'price', 'count', ]
#     list_editable = ['goods', 'price', 'count',]
#     list_filter = ['goods']
xadmin.site.register(TestLog,TestLogAdmin)
# xadmin.site.register(OrderDetail,OrderDetailAdmin)