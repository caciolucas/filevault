import magic
from rest_framework import serializers

from core.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
            "client",
            "mime_type",
            "size",
        )

    def create(self, validated_data) -> File:
        f = File()
        f.client = self.context["client"]
        f.name = validated_data["name"]
        f.path = validated_data["path"]

        f.save()
        return f
