from typing import Any, Dict
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .services.UserServices import ProfileService, UserTaskService

User = get_user_model()
profile_service = ProfileService()
task_service = UserTaskService()

class RegisterView(APIView):
    def post(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Any) -> Response:
        return profile_service.get_profile(user=request.user)

    def put(self, request: Any) -> Response:
        return profile_service.update_profile(user=request.user, data=request.data)


class UserTasksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Any) -> Response:
        return task_service.get_tasks_user(user=request.user)