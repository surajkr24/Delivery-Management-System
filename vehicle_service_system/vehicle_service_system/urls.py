from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, IssueViewSet, TransactionViewSet
from django.utils.module_loading import import_string

ComponentViewSet = import_string('vehicle_service_system.views.ComponentViewSet')


router = DefaultRouter()
router.register(r'components', ComponentViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'issues', IssueViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
]