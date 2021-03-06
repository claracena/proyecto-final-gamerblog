from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'), name='home'),
    path('account/', include('account.urls'), name='account'),
    path('contact/', include('contact.urls'), name='contact'),
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls'), name='about'),
    path('api/', include('api.urls'), name='api'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "gamerblog.views.page_not_found_view"
handler401 = "gamerblog.views.page_unauthorized"
handler400 = "gamerblog.views.page_bad_request"
handler403 = "gamerblog.views.page_forbidden"
handler500 = "gamerblog.views.internal_server_error"
