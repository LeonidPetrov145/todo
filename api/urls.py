from django.urls import path
from .views import TaskListCreateView, TaskDetailView, TagListCreateView, TagDetailView, UserDeleteView

urlpatterns = [
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete')
]