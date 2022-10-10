from rest_framework import viewsets

from rest_framework.response import Response

from album.models import Profile
from album.serializers import CreateProfileSerializer


class ProfileVIEWSet(viewsets.ViewSet):
    def create(self, request):
        profile_data = request.data
        serializer = CreateProfileSerializer(data=profile_data)
        if serializer.is_valid():
            profile = Profile(
                name=profile_data["name"],
                login=profile_data["login"],
                password=profile_data["password"],
            )
            profile.save()
            return Response({"id": profile.id})
        return Response({"msg": "data is not valid"})

    def list(self, request):
        profile_data = Profile.objects.all()
        return Response([{"id": profile.id} for profile in profile_data])
