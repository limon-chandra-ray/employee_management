from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employee-list'),
    path('add/', views.EmployeeCreateView.as_view(), name='employee-add'),
    path('edit/<int:pk>/', views.EmployeeUpdateView.as_view(), name='employee-edit'),
    path('delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='employee-delete'),
]