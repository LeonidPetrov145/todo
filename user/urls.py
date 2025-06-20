from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, LoginView, ProfileView, UserTasksView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('my/tasks/', UserTasksView.as_view(), name='user-tasks'),
    path('register/', RegisterView.as_view(), name='register')
]