"""drones-api URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.urlpatterns import format_suffix_patterns


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('accounts:user-list', request=request, format=format),
        'drones': reverse('drones:drones-list', request=request, format=format),
        'medications': reverse('drones:medications-list', request=request, format=format),
    })


urlpatterns = format_suffix_patterns([
    path('admin/', admin.site.urls),
    path('api/', api_root),
    path('api/', include('apps.accounts.urls')),
    path('api/', include('apps.drones.urls')),
    path('api-auth/', include('rest_framework.urls')),
])
