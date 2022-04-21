from django.contrib import admin
from .models import Asset


class AssetAdmin(admin.ModelAdmin):
    model = Asset
    readonly_fields = ("update_date",)


admin.site.register(Asset, AssetAdmin)
