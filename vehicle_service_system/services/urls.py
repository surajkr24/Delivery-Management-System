from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('services.urls')),
    path('', include('vehicle_service_system.urls')),

]