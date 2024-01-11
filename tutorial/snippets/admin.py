from django.contrib import admin

from .models import Foo, Bar, BarOwner 
from rest_framework.authtoken.models import Token

admin.site.register(Foo)
admin.site.register(Bar)
admin.site.register(BarOwner)
