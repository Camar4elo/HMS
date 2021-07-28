from django.urls import path
from . import views

urlpatterns = [
    path('', views.TasksView.as_view()),
    path('detail/<int:pk>', views.TaskDetailView.as_view()),
]
