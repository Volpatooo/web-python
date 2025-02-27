"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sistema', include("sistema.urls")),
    # path('', RedirectView.as_view(url='/sistema', permanent=False)), # faz com que só acessando olocal host já apareça a função index
    path('steamfake/', include('steamfake.urls')),
    path('', RedirectView.as_view(url='/steamfake', permanent=False)) # qundo acessamos o local host ele ja redireciona o steamfake automaticamente
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)