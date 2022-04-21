from django.contrib import admin
from .models import *


class ProfileSearch(admin.ModelAdmin):
    search_fields = ('emp_name', 'emp_id', "emp_desi", 'emp_process')
    list_display = ('emp_name', 'emp_id', 'emp_desi', 'emp_process', "emp_rm1", "emp_rm2", "emp_rm3",'agent_score','final_score')


class TableSearch(admin.ModelAdmin):
    search_fields = ('emp_name', 'emp_id')
    list_display = ('emp_name', 'emp_id', "agent_score", "mgr_score")


class PartDSearch(admin.ModelAdmin):
    search_fields = ('emp_name', 'emp_id')
    list_display = ('emp_name', 'emp_id')


# Register your models here.
admin.site.register(Profile, ProfileSearch)
admin.site.register(PartA_Appraisee, TableSearch)
admin.site.register(PartB_Appraisee, TableSearch)
admin.site.register(PartC_Appraisee, TableSearch)
admin.site.register(PartD_Appraisee, PartDSearch)
admin.site.register(Data, ProfileSearch)
