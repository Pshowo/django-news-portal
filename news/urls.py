from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPageView.as_view()),
    path('news/', views.News.as_view()),
    path('news/create/', views.Create.as_view()),
    path('news/<int:link>/', views.article),
]