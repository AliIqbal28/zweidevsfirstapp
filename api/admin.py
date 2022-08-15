from django.contrib import admin
from easy_select2 import select2_modelform

from api.models import SoftwareHouse, Employee


@admin.register(SoftwareHouse)
class SoftwareHouseAdmin(admin.ModelAdmin):
    form = select2_modelform(SoftwareHouse, attrs={'width': '250px'})
    list_display = ["id", "name", "about"]
    search_fields = ["name"]
    list_filter = ["name"]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    form = select2_modelform(Employee, attrs={'width': '250px'})
    list_display = ["id", "first_name", "last_name", "software_house", "designation", "email", "birth_date"]
    search_fields = ["first_name", "last_name"]
    list_filter = ["first_name", "last_name", "software_house", "designation", "email", "birth_date"]
