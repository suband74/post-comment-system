from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models import Articles, Comments

admin.site.register(Articles)
admin.site.register(Comments, MPTTModelAdmin)
