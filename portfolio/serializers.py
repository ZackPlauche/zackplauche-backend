from rest_framework import serializers

from .models import Image, Project, Contribution


class ContributionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contribution
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    contributions = ContributionSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'
        depth = 2