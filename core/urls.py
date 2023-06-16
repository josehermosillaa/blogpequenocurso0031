from django.contrib import admin
from django.urls import path
from .views import (
    home, 
    content_view , 
    login_view,
    logout_view,
    register_view
    )

from django.conf import settings

urlpatterns = [
    path("", home , name='home' ),
    path("content/<int:id>/", content_view , name='content' ),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    