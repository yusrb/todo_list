from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include(('base.urls' , 'base') , namespace="base")),
    path('user/' , include(('user.urls' , 'user') , namespace="user")),
    path("__reload__/", include("django_browser_reload.urls")),
]
