"""adminUTM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from inicio import views
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.principal,name="Principal"),
    path("contacto/",views_registros.contacto,name="Contacto"),
    path("registrar/",views_registros.registrar,name="Registrar"),
    path("solicitud/",views_registros.solicitud,name="Solicitud"),
    path("registrarSolicitud/",views_registros.registrarSolicitud,name="RegistrarSolicitud"),
    path("consultarSolicitud/",views_registros.consultarSolicitud,name="ConsultarSolicitud"),
    path("eliminarSolicitud/<int:id>/",views_registros.eliminarSolicitud,name="EliminarSolicitud"),
    path("formEditarSolicitud/<int:id>/",views_registros.consultarSolicitudIndividual,name="ConsultaIndividual"),
    path("editarSolicitud/<int:id>/",views_registros.editarSolicitud,name="Editar"),
]


if settings.DEBUG: 
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)