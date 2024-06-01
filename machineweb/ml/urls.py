from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome,name='home'),
    path('user', views.user),
    path('result',views.predict_failure)
]
