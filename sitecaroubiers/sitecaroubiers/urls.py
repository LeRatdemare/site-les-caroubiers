"""
URL configuration for sitecaroubiers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from plannings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('gestion/familles/', views.gestion_familles, name='gestion-familles'),
    path('gestion/plannings/', views.gestion_plannings, name='gestion-plannings'),
    path('gestion/inscription-perisco/<int:num_periode>/<str:cible_inscription>/', views.inscription_perisco, name='inscription-perisco'),
    path('gestion/plannings/selection_periode/', views.selection_periode, name='selection-periode'),
    path('gestion/plannings/gestion_periode/<int:num_periode>/', views.gestion_periode, name='gestion-periode'),
    # JSON
    path('gestion/plannings/get-base-plannings/', views.get_base_plannings, name='get-base-plannings'),
]
