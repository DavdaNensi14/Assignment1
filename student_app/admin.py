from django.contrib import admin
from student_app.models import *

# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
	actions=['enable']

	fieldsets=(
		('School',{'fields':('name','address','email','contact_no','rating')}),
		)

	exclude=('published_date',)
	search_fields=('name',)
	ordering=('-created_date',)
	list_display = ('name',)
	list_filter = ('rating', )
	list_display_links = ('name',)

	def enable(self,request,queryset):
		queryset.update(enabled=True)
		
admin.site.register(School,SchoolAdmin)
admin.site.register(Student)		


