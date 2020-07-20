from django.contrib import admin
from first_app.models import AccessRecord,WebPage,Topic,Login,UserProfileInfo
# Register your models here.
admin.site.register(AccessRecord),
admin.site.register(Topic),
admin.site.register(WebPage),
admin.site.register(Login),
admin.site.register(UserProfileInfo)
