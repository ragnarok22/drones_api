"""drones-api URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.core import views as core_views
from apps.accounts import views as accounts_views
from apps.drones import views as drones_views
from apps.logs import views as logs_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', accounts_views.UserViewSet, basename="user")
router.register(r'drones', drones_views.DroneViewSet, basename="drone")
router.register(r'medications', drones_views.MedicationViewSet, basename="medication")
router.register(r'logs', logs_views.LogViewSet, basename="log")

urlpatterns = [
    path('', core_views.IndexView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
