from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_view
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_view.LoginView.as_view(template_name='system/login.html'), name='loginroute'),
    path('signup-user/', views.signup, name='signup-page'),
    path('signup-book/', views.signupBook, name='signup-page-book')
]