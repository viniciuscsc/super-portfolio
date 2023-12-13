from django.urls import include, path
from rest_framework import routers
from projects.views import ProfileViewSet, ProjectView

router = routers.DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"projects", ProjectView)

urlpatterns = [path("", include(router.urls))]
