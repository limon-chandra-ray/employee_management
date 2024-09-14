from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Custom login view
    path('logout/', views.logout_view, name='logout'),  # Custom logout view
    path('signup/', views.signup_view, name='signup'),  # Custom signup view
]