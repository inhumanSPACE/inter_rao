from rest_framework import serializers

from .models import Album, Photo


class CreateProfileSerializer(serializers.Serializer):
    name = serializers.CharField()
    login = serializers.CharField()
    password = serializers.CharField()


class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    profile = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Album
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"


class UpdatePhotoSerializer(serializers.Serializer):
    name = serializers.CharField()
