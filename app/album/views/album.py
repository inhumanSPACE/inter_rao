from rest_framework import generics
from rest_framework.generics import get_object_or_404
from album.models import Album
from album.serializers import AlbumSerializer, AlbumCreateSerializer


class AlbumAPICreate(generics.CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumCreateSerializer


class AlbumAPIList(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj


class AlbumAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumAPIDelete(generics.DestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
