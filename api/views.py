from typing import Any, Dict, Optional, Union
from rest_framework.views import APIView
from rest_framework.response import Response
from .services.AdminServices import UserService
from .services.TaskServices import TaskService
from .services.TegServices import TagService
from .permissions import IsAdmin

task_service = TaskService()
tag_service = TagService()
user_service = UserService()

class TaskListCreateView(APIView):
    def get(self, request: Any) -> Response:
        return task_service.get_all_tasks()

    def post(self, request: Any) -> Response:
        return task_service.create_task(data=request.data)


class TaskDetailView(APIView):
    def get(self, request: Any, pk: int) -> Response:
        return task_service.get_task(pk=pk)

    def put(self, request: Any, pk: int) -> Response:
        return task_service.update_task(pk=pk, data=request.data)

    def delete(self, request: Any, pk: int) -> Response:
        return task_service.delete_task(pk=pk)


class TagListCreateView(APIView):
    def get(self, request: Any) -> Response:
        return tag_service.get_all_tags()

    def post(self, request: Any) -> Response:
        return tag_service.create_tag(data=request.data)


class TagDetailView(APIView):
    def get(self, request: Any, pk: int) -> Response:
        return tag_service.get_tag(pk)

    def put(self, request: Any, pk: int) -> Response:
        return tag_service.update_tag(pk=pk, data=request.data)

    def delete(self, request: Any, pk: int) -> Response:
        return tag_service.delete_tag(pk)


class UserDeleteView(APIView):
    permission_classes = [IsAdmin]

    def delete(self, request: Any, pk: int) -> Response:
        return user_service.delete_user(pk=pk, request_user=request.user)