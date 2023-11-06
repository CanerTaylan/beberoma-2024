
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from appAdmin.views import *
from appCart.views import *
from appPage.views import *
from appProduct.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    path('admin_paneli/', include('appAdmin.urls'), ),
    path('pages/', include('appPage.urls'), ),
    path('products/', include('appProduct.urls'), ),
    path('cart/', include('appCart.urls'), ),
    path('user/', include('appUser.urls'), ),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = "Beberoma Admin"
admin.site.site_header = "Beberoma Yönetim Paneli"
