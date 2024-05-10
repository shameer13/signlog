from django.urls import path

from signapp import views

urlpatterns = [
    path('',views.loginfun,name='log'),
    path('signin/',views.signinfun),

]