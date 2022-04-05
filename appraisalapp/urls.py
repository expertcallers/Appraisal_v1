from django.urls import path
from .views import *

urlpatterns = [
    path('', LogoutFunc),
    path('login', LoginPage),
    path('indexing', IndexPage),
    path('parta', part_a_save),
    path('manparta', managerPartAView),
    path('manparta-save', managerPartASave),
    path('partb', part_b_save),
    path('manpartb/<str:id>', manager_part_b_save, name="manpartb"),
    path('partc', part_c_save),
    path('manpartc/<str:id>',manager_part_c_save,name="manpartc"),
    path('partd', part_d_save),
    path('manpartd/<str:id>',manager_part_d_save,name="manpartd"),
    path('notice', Notice),
    path('view/<str:id>',viewAppraisal,name="view"),
    path('manager-dashboard', managerDashboard),
    path('add-parameters', addParameters),
    path('dashboard', dashboardRedirect),
    path('self-appraisal', selfAppraisal),
    path('under-agents', underAgents),
    path('change-emp-password', changeEmpPassword),
    path('settings',Settings),
    path('change-password',change_password),
]