from rest_framework import serializers
from projects.models import (
    Profile,
    Project,
    CertifyingInstitution,
    Certificate,
)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "id",
            "name",
            "github",
            "linkedin",
            "bio",
        ]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "github_url",
            "keyword",
            "key_skill",
            "profile",
        ]


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = [
            "id",
            "name",
            "certifying_institution",
            "timestamp",
            "profiles",
        ]


class NestedCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = [
            "id",
            "name",
            "timestamp",
            "profiles",
        ]


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = NestedCertificateSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = [
            "id",
            "name",
            "url",
            "certificates",
        ]

    def create(self, validated_data):
        data = validated_data.pop("certificates")
        institution = CertifyingInstitution.objects.create(**validated_data)

        for certificate in data:
            Certificate.objects.create(
                certifying_institution=institution,
                **certificate,
            )

        return institution
