from django.contrib import admin
from .models import Example


class ExampleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Example, ExampleAdmin)