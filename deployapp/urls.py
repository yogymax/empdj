
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Sample for Deploying and webapp..!')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('employee.urls')),#our
    url(r'^api/v2/', include('rest_framework.urls')),#drf provided
    url(r'swagger/', schema_view),
]
