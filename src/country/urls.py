from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pays/', include('lespays.urls')),
    path('', include('bd.urls'))
]
