import base64

from rest_framework.exceptions import AuthenticationFailed, JsonResponse

from core.models import Client


class BasicAuthMixin:
    """
    A mixin to handle Basic Auth token and retrieve the Client.
    """

    def __init__(self, *args, **kwargs):
        self.context = {}
        super().__init__()

    def get_client_from_auth(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Basic "):
            raise AuthenticationFailed("Invalid Basic Token.")

        try:
            token = auth_header.split(" ")[1]
            decoded = base64.b64decode(token).decode("utf-8")
            client_id, client_secret = decoded.split(":")

            client = Client.objects.get(
                client_id=client_id, client_secret=client_secret
            )
            return client
        except (ValueError, Client.DoesNotExist):
            raise AuthenticationFailed("Invalid Basic Token.")

    def dispatch(self, request, *args, **kwargs):
        try:
            self.context["client"] = self.get_client_from_auth(request)
        except AuthenticationFailed as e:
            return JsonResponse({"error": e.detail}, status=e.status_code)

        return super().dispatch(request, *args, **kwargs)  # type: ignore
