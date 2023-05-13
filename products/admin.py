from django.contrib import admin
from .models import products


class membersAdmin(admin.ModelAdmin):
    list_display = ("name", "price")

admin.site.register(products, membersAdmin)
