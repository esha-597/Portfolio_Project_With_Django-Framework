from django.contrib import admin
from .models import Education, Skill, Project, Contact, Experience, Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name','introduction','background_img')
# Register your models here.
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(Experience)
admin.site.register(Profile,ProfileAdmin)