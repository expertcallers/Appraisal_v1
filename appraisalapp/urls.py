from django.urls import path
from .views import *

urlpatterns = [
    path('login', LoginPage),
    path('parta', part_a_save),
    path('manparta/<str:id>', manager_part_a_save),
    path('partb', part_b_save),
    path('manpartb/<str:id>', manager_part_b_save, name="manpartb"),
    path('partc', part_c_save),
    path('manpartc/<str:id>',manager_part_c_save,name="manpartc"),
    path('partd', part_d_save),
    path('manpartd/<str:id>',manager_part_d_save,name="manpartd"),
    path('notice', Notice),
    path('view/<str:id>',viewAppraisal,name="view"),
    path('manager-table', manager_Table),
]