from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.static import serve

from app_ifoundadog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.LicenseLookUpView.as_view()),
    url(r'^dog/(?P<id>[\w\-]+)/$', views.DogDetailView.as_view()),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view())
]

if settings.DEBUG:
    urlpatterns + static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )

    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]