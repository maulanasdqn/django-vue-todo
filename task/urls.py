from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskView.as_view(), name="task"),
    path('<str:id>/beres/', views.Taskberes.as_view(), name="beres"),
    path('<str:id>/hapus/', views.hapus.as_view(), name="hapus")
]
