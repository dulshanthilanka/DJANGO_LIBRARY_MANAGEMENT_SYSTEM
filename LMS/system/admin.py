from django.contrib import admin
from . models import bookdtails, userdetails

# Register your models here.
admin.site.register(userdetails)
admin.site.register(bookdtails)