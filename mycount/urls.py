
from django.contrib import admin
from django.urls import path

import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('count/', views.count, name='count1'),
    path('about/', views.about)
]
