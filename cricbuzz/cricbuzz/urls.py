
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('api/admin/signup', views.signup),
    path('api/admin/login', views.login),
    path('api/test-token', views.test_token),
    # path('api/admin/<int:id>/squad', views.logout),

    path('api/', include('matches.urls')),
    path('api/', include('players.urls'))

]
