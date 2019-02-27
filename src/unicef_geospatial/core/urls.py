from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import index

urlpatterns = [
    path(r'', index, name='home'),
    path(r'login/', LoginView.as_view(template_name='login.html'), name='login'),
    path(r'logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
