from django.urls import path
from . import views

urlpatterns = [
    path('', views.StaffView.as_view()),
    path('detail/<int:pk>', views.StaffDetailView.as_view())
]
