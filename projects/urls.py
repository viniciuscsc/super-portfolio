from django.urls import include, path
from rest_framework import routers
from projects.views import ProfileView

router = routers.DefaultRouter()
router.register("profiles", ProfileView)

urlpatterns = [path("", include(router.urls))]
