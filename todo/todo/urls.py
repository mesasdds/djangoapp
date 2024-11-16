
from django.contrib import admin
from django.urls import path, include
from users.views import custom_logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', custom_logout, name='logout'),
]
