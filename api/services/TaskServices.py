from rest_framework import status
from rest_framework.response import Response
from ..models import Task
from ..serializers import TaskSerializer
from django.shortcuts import get_object_or_404
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)


class TaskService:
    def get_task(self, pk: int) -> Task:
        return get_object_or_404(Task, pk=pk)

    def get_all_tasks(self) -> Response:
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return self.create_response(data={"tasks": serializer.data}, status=status.HTTP_200_OK)

    def create_task(self, data: Dict[str, Any]) -> Response:
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return self.create_response(data={"task": serializer.data}, status=status.HTTP_201_CREATED)
        return self.create_error_response(serializer)

    def update_task(self, pk: int, data: Dict[str, Any]) -> Response:
        task = self.get_task(pk)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return self.create_response(data={"task": serializer.data}, status=status.HTTP_200_OK)
        return self.create_error_response(serializer)

    def delete_task(self, pk: int) -> Response:
        task = self.get_task(pk)
        task.delete()
        return self.create_response(data={"message": "Задача успешно удалена"}, status=status.HTTP_200_OK)

    def create_response(self, data: Dict[str, Any], status: int) -> Response:
        return Response({"data": data}, status=status)

    def create_error_response(self, serializer: TaskSerializer) -> Response:
        logger.error(f"Validation errors: {serializer.errors}")
        return Response({"data": {"errors": serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)