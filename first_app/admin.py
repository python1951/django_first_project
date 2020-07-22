from django.contrib import admin
from first_app.models import AccessRecord,WebPage,Topic,Login,UserProfileInfo,Student,School
# Register your models here.
admin.site.register(AccessRecord),
admin.site.register(Topic),
admin.site.register(WebPage),
admin.site.register(Login),
admin.site.register(UserProfileInfo),
admin.site.register(Student),
admin.site.register(School)
