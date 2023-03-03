from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from base.views import index, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('conversation/', include('conversation.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('', include('base.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
