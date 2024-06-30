from django.urls import path

from myApp import views
urlpatterns = [
    path('center/', views.center, name='center'),
]
