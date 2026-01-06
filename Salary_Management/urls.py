
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Salary.views import  *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/',Employee_list , name='employee_list'),
    path('add/', Employee_create, name='employee_create'),
    path('edit/<int:id>/', Employee_update, name='employee_update'),
    path('delete/<int:id>/',Employee_delete, name='employee_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

