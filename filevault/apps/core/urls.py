from rest_framework import routers

from core.views import FileViewSet

router = routers.DefaultRouter()

router.register(r"files", FileViewSet, basename="file")

urlpatterns = router.urls
