from django.contrib import admin
from django.urls import path
from django.urls import include 
# (функция необходимая при множественном ветвлении адресов)

from start.views import index
from office.views import index2
from collection.views import index3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    # path('office/', index2),
    path('office/', include('office.urls')),
    path('collection/', index3),
]
