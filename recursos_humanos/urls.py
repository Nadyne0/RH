from django.urls import path
import recursos_humanos.views as views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home_view, name="home"),
    path("register/", views.register_view, name="register"),
]
