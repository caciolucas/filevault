from rest_framework import viewsets, status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.decorators import action
from private_storage.views import PrivateStorageView

from core.models import File
from core.serializers import FileSerializer
from core.mixins import BasicAuthMixin


class FileViewSet(BasicAuthMixin, viewsets.ModelViewSet):
    """
    A viewset for handling file uploads and filtering files per client.
    """

    serializer_class = FileSerializer
    permission_classes = []

    def get_queryset(self):
        client = self.context.get("client")
        if not client:
            return File.objects.none()
        return File.objects.filter(client=client)

    def create(self, request, *args, **kwargs):
        serializer = FileSerializer(data=request.data, context=self.context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["get"])
    def download(self, request, pk=None):
        try:
            file = self.filter_queryset(self.get_queryset()).get(pk=pk)
        except File.DoesNotExist:
            raise APIException("File not found", status.HTTP_404_NOT_FOUND)

        format_type = request.GET.get(".format", "inline")
        view = PrivateStorageView.as_view(
            content_disposition=format_type, can_access_file=lambda x: True
        )

        response = view(request, path=str(file.path))

        ext = str(file.path).split(".")[-1]
        response["Content-Disposition"] = f'{format_type}; filename="{file.name}.{ext}"'

        return response
