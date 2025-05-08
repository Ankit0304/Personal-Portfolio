from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(About)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(Experience)
admin.site.register(Projects)
admin.site.register(Contact)
admin.site.register(Link)
