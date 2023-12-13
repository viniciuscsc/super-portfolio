from django.shortcuts import render
from rest_framework import viewsets
from projects.models import Profile, Project
from projects.serializers import ProfileSerializer, ProjectSerializer


# Create your views here.
class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
