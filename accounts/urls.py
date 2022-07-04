from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path(r'<str:username>', views.account_page, name='account'),
    path(r'register/', views.register_page, name='register'),
    path(r'login/', views.login_page, name='login'),
    path(r'verify/', views.verify_page, name='verify'),
    path(r'logout/', views.logout_page, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
