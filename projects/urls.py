from django.urls import include, path
from rest_framework import routers
from projects.views import ProfileView, ProjectView

router = routers.DefaultRouter()
router.register("profiles", ProfileView)
router.register("projects", ProjectView)

urlpatterns = [path("", include(router.urls))]
