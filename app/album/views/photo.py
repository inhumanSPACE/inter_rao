from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from album.models import Photo
from album.serializers import PhotoSerializer, UpdatePhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()

    def get_serializer_class(self):
        if self.action == "update_image":
            return UpdatePhotoSerializer
        else:
            return PhotoSerializer

    @action(methods=["post"], detail=False)
    def upload_image(self, request):
        data = request.data
        photo = Photo.objects.create(
            name=data["name"],
            album_id=data["album_id"],
            author_id=data["profile_id"],
            image=request.FILES.get("image"),
        )

        return Response(photo)

    @action(methods=["put"], detail=False)
    def update_image(self, request, **kwargs):
        data = request.data
        serializer = UpdatePhotoSerializer(data=data)

        pk = self.kwargs.get("pk")
        print(data)
        print(serializer)
        if not pk:
            return Response("Not valid")

        if serializer.is_valid():
            Photo.objects.filter(id=pk).update(name=data["name"])
            return Response(data["name"])

    @action(detail=True)
    def get_image(self, request):
        album_id = request.GET.get("album_id")
        profile_id = request.GET.get("profile_id")
        if not profile_id:
            raise PermissionDenied()

        album_data = Photo.objects.all().filter(album_id=album_id, author_id=profile_id)
        return Response(album_data)
