from django.urls import path

from myApp import views
urlpatterns = [
    path('center/', views.center, name='center'),
    path('centerLeft/', views.centerLeft, name='centerLeft'),
    path('bottomLeft/', views.bottomLeft, name='bottomLeft'),
]
