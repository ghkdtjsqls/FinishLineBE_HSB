from django.urls import path, include
from . import views
from django.conf import settings  # settings 모듈 임포트
from django.conf.urls.static import static  # static 모듈 임포트
from rest_framework.routers import DefaultRouter
from .views import MySubjectListViewSet

router = DefaultRouter()
router.register(r'mysubjectlist', MySubjectListViewSet)

urlpatterns = [
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)