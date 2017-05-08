from django.contrib import admin
#from ipear.models import Profile, DispatcherInfo

# Register your models here.

'''
class UserInfoAdmin(admin.ModelAdmin):
	list_display = ["__str__","first_Name","last_Name","address","phone_Number"]
	search_fields = ["first_Name", "last_Name", "address", "phone_Number"]
	class Meta:
		model = Profile
	
class DispatcherInfoAdmin(admin.ModelAdmin):
	list_display = ["__str__","username","first_Name","last_Name"]
	search_fields = ["first_Name", "last_Name", "username"]
	class Meta:
		model = DispatcherInfo


admin.site.register(Profile, UserInfoAdmin)
admin.site.register(DispatcherInfo, DispatcherInfoAdmin)
'''
