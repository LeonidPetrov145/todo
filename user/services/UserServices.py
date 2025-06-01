from typing import Any, Dict
from rest_framework.response import Response
from rest_framework import status
from ..serializers import UserSerializer
from api.models import Task
from api.serializers import TaskSerializer


class ProfileService:
    def get_profile(self, user: Any) -> Response:
        serializer = UserSerializer(user)
        return Response(
            {"data": {"profile": serializer.data}},
            status=status.HTTP_200_OK
        )

    def update_profile(self, user: Any, data: Dict[str, Any]) -> Response:
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"data": {"profile": serializer.data}},
                status=status.HTTP_200_OK
            )
        return Response(
            {"data": {"errors": serializer.errors}},
            status=status.HTTP_400_BAD_REQUEST
        )

class UserTaskService:
    def get_tasks_user(self, user: Any) -> Response:
        tasks = Task.objects.filter(assignee=user)
        serialized_data = TaskSerializer(tasks, many=True).data
        return Response(
            {"data": {"tasks": serialized_data}},
            status=status.HTTP_200_OK
        )