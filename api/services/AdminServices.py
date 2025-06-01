from rest_framework.response import Response
from rest_framework import status
from user.models import CustomUser
from django.shortcuts import get_object_or_404
import logging

logger = logging.getLogger(__name__)

class UserService:
    def get_user(self, pk):
        return get_object_or_404(CustomUser, pk=pk)

    def delete_user(self, pk, request_user):
        user = self.get_user(pk)

        if user:
            user.delete()
            logger.info(f"Пользователь успешно удален ")
            return self.create_response(data={"message": "Пользователь успешно удален"}, status=status.HTTP_200_OK)
        else:
            logger.warning(f"Попытка удалить несуществующего пользователя")
            return self.create_error_response({"error": "Пользователь не найден"})
        
    def create_response(self, data, status):
        return Response({"data": data}, status=status)

    def create_error_response(self, errors):
        logger.error(f"Validation or runtime errors: {errors}")
        return Response({"data": {"errors": errors}}, status=status.HTTP_400_BAD_REQUEST)