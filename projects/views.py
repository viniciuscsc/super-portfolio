from django.shortcuts import render
from rest_framework import viewsets
from projects.models import Profile
from projects.serializers.profile_serializer import ProfileSerializer
from projects.serializers.project_serializer import ProjectSerializer


# Create your views here.
class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProjectView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProjectSerializer
