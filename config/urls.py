"""drones-api URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.accounts import views as accounts_views
from apps.drones import views as drones_views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', accounts_views.UserViewSet, basename="user")
router.register(r'drones', drones_views.DroneViewSet, basename="drone")
router.register(r'medications', drones_views.MedicationViewSet, basename="medication")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
