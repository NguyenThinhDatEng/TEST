from email.headerregistry import Group
from django.contrib import admin
from .models import Question, Choice, User
from django.contrib.auth.models import Group
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(User)
admin.site.unregister(Group)
admin.site.site_header = 'Admin Dashboard'
