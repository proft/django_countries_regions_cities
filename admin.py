from django.contrib import admin
from models import Country, Region, City, TestModel

admin.site.register(Country, admin.ModelAdmin)
admin.site.register(Region, admin.ModelAdmin)
admin.site.register(City, admin.ModelAdmin)
admin.site.register(TestModel, admin.ModelAdmin)
