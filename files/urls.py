from django.urls import path
from .views import *
from django.urls import include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import LogoutView
from django.conf import settings


urlpatterns = [
    path('', index, name = 'index'),
    path('search/', StaffSearch.as_view(), name = 'search'),
    path('download/<str:path>/', download, {'document_root': settings.MEDIA_ROOT}),
    path('upload/', UploadFile.as_view(), name='upload'),
    path('update/<int:id>/', UpdateFileInfo.as_view(), name = 'update'),
    path('delete/<int:id>/', DeleteFile.as_view(), name = 'delete'),
    path('users/registration/', RegisterUser.as_view(), name = 'register'),
    path('users/login/', LoginView.as_view(), name = 'login'),
    path('users/logout/', LogoutView.as_view(next_page = '/'), name = 'logout'),

    path('files/', FileListApiView.as_view()),
    #path('files/create', FileCreateView.as_view()),
]


