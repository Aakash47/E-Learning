from django.contrib import admin
from . models import *

# Register your models here.

class ProjectsAdmin(admin.TabularInline):
    model = Projects

class FreelanceAdmin(admin.ModelAdmin):
    inlines = [ProjectsAdmin,]

admin.site.register(Freelance, FreelanceAdmin)
admin.site.register(Fcontact)