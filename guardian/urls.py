from django.contrib import admin
from django.urls import path,include
import index.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('accounts/', include('allauth.urls')),
]
