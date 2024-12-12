from django.urls import path

from . import views

urlpatterns = [
    path('menu/', views.MenuListView.as_view()),
    path('menu/<int:pk>/detail/', views.MenuDetailView.as_view()),

]