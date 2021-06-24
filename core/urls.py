# core.urls.py

from django.conf import settings
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.conf.urls.static import static

from blog import views as blog_views

admin.site.site_header = "Taleeb INFO"
admin.site.site_title = "Taleeb INFO"
admin.site.index_title = "Welcome to Taleeb INFO"


def handler403(request, exception, template_name='403.html'):
    context = {'page_title': 'Permission non accordée'}
    return render(request, template_name, context, status=403)

def handler404(request, exception, template_name='404.html'):
    context = {'page_title': 'Page non trouvée'}
    return render(request, template_name, context, status=404)


def handler500(request, template_name='500.html'):
    context = {'page_title': 'Erreur interne'}
    return render(request, template_name, context, status=500)


urlpatterns = [
    # url home
    path(route='', view=blog_views.home_view, name='home'),
    path('', include('blog.urls', namespace='blog')),

    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path(settings.ADMIN_URL, admin.site.urls),
]

handler404 = handler404
handler403 = handler403
handler201600 = handler500

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('404/', handler404, {'exception': Exception("Page non trouvée !")}),
        path('403/', handler403, {'exception': Exception("Permission non accordée !")}),
        path('500/', handler500),
    ]
