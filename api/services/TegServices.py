from rest_framework.response import Response
from rest_framework import status
from ..models import Tag
from ..serializers import TagSerializer
from django.shortcuts import get_object_or_404
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)


class TagService:
    def get_tag(self, pk: int) -> Tag:
        return get_object_or_404(Tag, pk=pk)

    def get_all_tags(self) -> Response:
        tags = Tag.objects.all()
        serialized_data = TagSerializer(tags, many=True).data
        return self.create_response(data={"tags": serialized_data}, status=status.HTTP_200_OK)

    def create_tag(self, data: Dict[str, Any]) -> Response:
        serializer = TagSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return self.create_response(data={"tag": serializer.data}, status=status.HTTP_201_CREATED)
        return self.create_error_response(serializer)

    def update_tag(self, pk: int, data: Dict[str, Any]) -> Response:
        tag = self.get_tag(pk)
        serializer = TagSerializer(tag, data=data)
        if serializer.is_valid():
            serializer.save()
            return self.create_response(data={"tag": serializer.data}, status=status.HTTP_200_OK)
        return self.create_error_response(serializer)

    def delete_tag(self, pk: int) -> Response:
        tag = self.get_tag(pk)
        tag.delete()
        return self.create_response(data={"message": "Тег успешно удален"}, status=status.HTTP_200_OK)

    def create_response(self, data: Dict[str, Any], status: int) -> Response:
        return Response({"data": data}, status=status)

    def create_error_response(self, serializer: TagSerializer) -> Response:
        logger.error(f"Validation errors: {serializer.errors}")
        return Response({"data": {"errors": serializer.errors}}, status=status.HTTP_400_BAD_REQUEST)