from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ProfileResource(resources.ModelResource):
  class Meta:
     model = Profile
     # fields = ['emp_name', 'emp_id', 'emp_desi', 'emp_process', "emp_rm1", "emp_rm2", "emp_rm3"]

class ProfileSearch(ImportExportModelAdmin):
    search_fields = ('emp_name', 'emp_id', "emp_desi", 'emp_process')
    list_display = ('emp_name', 'emp_id', 'emp_desi', 'emp_process', "emp_rm1", "emp_rm2", "emp_rm3")
    resource_class = ProfileResource


class DataSearchResource(resources.ModelResource):
  class Meta:
     model = Data
     fields = ['emp_id', 'emp_name', 'emp_desi', 'emp_rm1_id', 'emp_rm2_id', 'emp_rm3_id', 'emp_process', "emp_rm1", "emp_rm2", "emp_rm3",'emp_doj']
     import_id_fields = ('emp_id',)

class DataSearch(ImportExportModelAdmin):
    search_fields = ('emp_name', 'emp_id', "emp_desi", 'emp_process')
    list_display = ('emp_name', 'emp_id', 'emp_desi', 'emp_process', "emp_rm1", "emp_rm2", "emp_rm3")
    resource_class = DataSearchResource


class TableSearch(ImportExportModelAdmin):
    search_fields = ('emp_name', 'emp_id')
    list_display = ('emp_name', 'emp_id', "agent_score", "mgr_score")


class PartDSearch(ImportExportModelAdmin):
    search_fields = ('emp_name', 'emp_id')
    list_display = ('emp_name', 'emp_id')
    resource_class = ProfileResource


# Register your models here.
admin.site.register(Profile, ProfileSearch)
admin.site.register(PartA_Appraisee, TableSearch)
admin.site.register(PartB_Appraisee, TableSearch)
admin.site.register(PartC_Appraisee, TableSearch)
admin.site.register(PartD_Appraisee, PartDSearch)
admin.site.register(Data, DataSearch)
