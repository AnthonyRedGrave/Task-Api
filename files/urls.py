from django.urls import path
from .views import *
from django.urls import include
from rest_framework.routers import DefaultRouter


# urlpatterns = [
#     path('files/', FileView.as_view()),
#     path('files/create', FileCreateView.as_view()),
# ]



router = DefaultRouter()

router.register('files', FileViewSet)

files_list_view = FileViewSet.as_view({
    "get": "list",
    "post": "create"
})

urlpatterns = [
    path('', include(router.urls)),
]

