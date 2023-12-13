from django.urls import include, path
from rest_framework import routers
from projects.views import (
    ProfileViewSet,
    ProjectView,
    CertificateView,
    CertifyingInstitutionView,
)

router = routers.DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"projects", ProjectView)
router.register(r"certifying-institutions", CertifyingInstitutionView)
router.register(r"certificates", CertificateView)

urlpatterns = [path("", include(router.urls))]
