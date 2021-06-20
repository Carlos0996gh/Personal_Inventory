from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Game)
admin.site.register(Platform)
admin.site.register(Developer)
admin.site.register(Publisher)
admin.site.register(Game_Genre)
admin.site.register(Game_Status)
admin.site.register(Game_Format)
admin.site.register(Purchase_Status)