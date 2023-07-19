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
    path('gestion/inscription-perisco/enfant/<int:periodNum>/', views.inscription_perisco_enfant, name='inscription-perisco-enfant'),
    path('gestion/inscription-perisco/equipier/<int:periodNum>/', views.inscription_perisco_equipier, name='inscription-perisco-equipier'),
    # JSON
    path('gestion/plannings/get-base-plannings/', views.get_base_plannings, name='get-base-plannings'),
]
