
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import set_language

from core.swagger.schema import swagger_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/', include('apps.common.urls')),
    path('blog/', include('apps.blog.urls')),
    path('i18n/', set_language, name='set_language')
]

urlpatterns += swagger_urlpatterns

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
