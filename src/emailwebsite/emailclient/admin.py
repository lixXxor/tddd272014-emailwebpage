from django.contrib import admin
from emailclient.models import emailclient, Choice

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 1

class EmailclientAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				 {'fields': ['question']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),	
	]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_recently')

admin.site.register(emailclient, EmailclientAdmin)