from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from core.models import Client


class ClientAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Basic "):
            return None

        try:
            import base64

            encoded_credentials = auth_header.split(" ")[1]
            decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8")
            client_id, client_secret = decoded_credentials.split(":")
        except (ValueError, IndexError):
            raise AuthenticationFailed("Invalid authentication credentials.")

        try:
            client = Client.objects.get(
                client_id=client_id, client_secret=client_secret, is_active=True
            )
        except Client.DoesNotExist:
            raise AuthenticationFailed("Invalid client credentials.")

        return client, None
