
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('KYC',views.KYC, name='KYC'),
    path('KYC2',views.KYC2 , name="KYC2"),
    path('KYC3',views.KYC3 , name="KYC3"),
    path('KYC4',views.KYC4 , name="KYC4"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
