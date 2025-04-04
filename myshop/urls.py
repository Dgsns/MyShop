from django.contrib import admin
from django.urls import path, include


admin.site.site_header= 'MyCaffee and Store "Sunshine"'
admin.site.site_title= 'MyShop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls'))
]
