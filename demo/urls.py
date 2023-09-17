from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

from django.contrib import admin
urlpatterns = [
    path('', include('dataBaseApp.urls')),
    path('admin/', admin.site.urls),
    path('pdf/', views.pdf_viewer, name='pdf')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 添加静态文件和媒体文件的URL配置
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
