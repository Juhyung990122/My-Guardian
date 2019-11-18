from django.contrib import admin
from django.urls import path,include
import index.views
import adopt.views
from rest_framework import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('accounts/', include('allauth.urls')),
    path('adopt/',include('adopt.urls')),
    path('api-auth/',include('rest_framework.urls'))
]
