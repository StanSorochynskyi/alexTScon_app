from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('work-metrics-chart/', views.work_metrics_chart, name='work_metrics_chart'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/new/', views.create_project, name='create_project'),
]
