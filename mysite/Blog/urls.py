from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Andere/',views.index1, name='index1'),
    path('Reisen/', views.index2, name='index2'),
    path('Arbeit/', views.index3, name='index3'),
    path('Freizeit/', views.index4, name='index4'),
    path('new/', views.index5, name='index5'),
]
