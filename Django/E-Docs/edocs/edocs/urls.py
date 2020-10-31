from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('DLock/', include('doclocker_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='homepage.html'), name='homepage'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "DLock Admin"
admin.site.site_title = "DLock Admin Portal"
admin.site.index_tile = "Welcome to DLOCK portal"
