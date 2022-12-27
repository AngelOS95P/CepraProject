"""cepraproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path ,include
from dashboard import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/',include('sesion.urls')),
    path('api/Reco/',include('recomendacion.urls')),
    path('apiEst/v1.0/',include('estudiante.urls')),
    # Path DashBoard
    path('dashboard/',include('dashboard.urls')),
    # Path Page
    path('',include('page.urls')),
    # Dinamico
    path('',include('dinamico.urls')),
    #Login
    path('', include('usuarios.urls')),

]

admin.site.site_header = "Proyecto CEPRA"
admin.site.site_title = "Proyecto CEPRA Portal de Administracion"
admin.site.index_title = "Bienvenido al Portal de Administracion"