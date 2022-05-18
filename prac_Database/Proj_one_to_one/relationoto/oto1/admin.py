from django.contrib import admin
from .models import Page
# Register your models here.


class PageAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'page_publish_date', 'puser']

admin.site.register(Page, PageAdmin)