from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from schoolapp.views import addstudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addstudent/', addstudent),
]
