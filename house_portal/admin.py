from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "TKPStays Admin"  
admin.site.site_title = "My Admin Portal"   
admin.site.index_title = "Welcome to the TKP Portal"  


admin.site.register(Area)
admin.site.register(Owner)
admin.site.register(House)
