from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from album.views.album import (
    AlbumAPIUpdate,
    AlbumAPIDelete,
    AlbumAPICreate,
    AlbumAPIList,
)
from album.views.photo import PhotoViewSet
from album.views.profile import ProfileVIEWSet

router = routers.DefaultRouter()
router.register("photo", PhotoViewSet)
router.register("profile", ProfileVIEWSet, basename="profile")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/v1/profile/signup/", ProfileVIEWSet.as_view({"post": "create"})),
    path("api/v1/profile/list/", ProfileVIEWSet.as_view({"get": "list"})),
    path("api/v1/album/create/", AlbumAPICreate.as_view()),
    path("api/v1/album/", AlbumAPIList.as_view()),
    path("api/v1/album/<int:pk>/", AlbumAPIList.as_view()),
    path("api/v1/album/update/<int:pk>/", AlbumAPIUpdate.as_view()),
    path("api/v1/album/delete/<int:pk>/", AlbumAPIDelete.as_view()),
    path(
        "photo/upload/",
        PhotoViewSet.as_view({"post": "create"}),
        name="image-upload",
    ),
    path("photo/update/<int:pk>/", PhotoViewSet.as_view({"put": "update_image"})),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
