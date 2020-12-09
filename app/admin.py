from django.contrib import admin
#
# # Register your models here.
from djoser.conf import User
class AcrivedAdmin(admin.ModelAdmin):
    list_display = ('key','team_name','score','progress','number','active',)
    ordering = ('-active',)
    #list_display = ('get_active','user_is_active')
    # def get_active(self,obj):
    #     return obj.
from app.models import Actived, Question, Answer

admin.site.register(Actived,AcrivedAdmin)
admin.site.register(Question)
admin.site.register(Answer)