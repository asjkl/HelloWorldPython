"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import HelloWorld.views as views
import libreria.views as Lv

# Bisogna importare le viste tramite views.[qualcosa] e non
# tramite una stringa "views.benvenuto"
#

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^benvenuto/$', views.benvenuto),
    url(r'^libri/$', Lv.tuttiLibri),
    url(r'^libri/(\d*)/$', Lv.restiuisciLibro),
    url(r'libri/acquisti/(?P<anno>\d{4})/$', Lv.restituisciPerDataAcquisto),
    url(r'libri/autori/(\d+)/$', Lv.restituisciTuttiIlibriDiQuestoAutore),
    url(r'libri/generi/(\d+)/$', Lv.restituisciTuttiILibriPerQuelGenere),
]
