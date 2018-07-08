from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
	list_display = [
		"id",
		"username",
		"email",
		"first_name",
		"last_name",
		"contact",
	]

	class Meta:
		model = User

admin.site.register(User, UserAdmin)