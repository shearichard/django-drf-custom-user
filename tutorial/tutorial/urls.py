from django.urls import re_path, path, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('snippets.urls')),
]
