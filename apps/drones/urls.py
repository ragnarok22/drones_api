from django.urls import path

from . import views

app_name = 'drones'
urlpatterns = [
    path('drones/', views.DroneList.as_view(), name="drones-list"),
    path('drones/<int:pk>/', views.DroneDetail.as_view(), name="drones-detail"),
    path('medications/', views.MedicationList.as_view(), name="medications-list"),
    path('medications/<int:pk>/', views.MedicationDetail.as_view(), name="medications-detail"),
]
