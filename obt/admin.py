from django.contrib import admin
from obt.models import Obt


class ObtAdmin(admin.ModelAdmin):
    list_display = ('pk', 'v1', 'v2', 'v3', 'v4', )
    list_display_links = ('pk', )


admin.site.register(Obt, ObtAdmin)

