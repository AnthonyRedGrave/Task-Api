from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib import messages
from .models import *
from django.conf import settings
from rest_framework import generics
from .serializers import *
from django.views.generic import View
from .forms import *
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .utils import *
from django.db.models import Q
from django.contrib.auth.models import AnonymousUser


def index(request):
    if request.user.is_authenticated and not request.user.is_staff:
        curr_user = AdvUser.objects.get(user=request.user)
        files = File.objects.filter(user = curr_user)
        context = {'files': files}
        return render(request, 'files/index.html', context)
    elif request.user.is_staff:
        users = AdvUser.objects.filter(engaged_size__gte=0)
        context = {'users': users}
        return render(request, 'files/index_admin.html', context)
    return render(request, 'files/index.html', {})


class StaffSearch(View):

    def get(self, request):
        file_info = request.GET.get('search_info')
        files = File.objects.filter(Q(name__icontains = file_info) | Q(content__icontains = file_info) |
                                    Q(user__user_name__icontains = file_info))
        print(files)
        context = {'files': files, 'file_info': file_info}
        return render(request, 'files/search.html', context)


class RegisterUser(View):
    def get(self, request):
        form = RegForm()
        context = {'form': form}
        return render(request, 'users/registration.html', context)

    def post(self, request):
        form = RegForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit = False)
            user_name = form.cleaned_data['username']
            phone = form.cleaned_data['phone']
            new_user.username = user_name
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            AdvUser.objects.create(user_name = user_name,  phone = phone, user = new_user)
            user = authenticate(username = user_name, password = form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'users/registration.html', context)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(request, 'users/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                return redirect('index')
        return render(request, 'users/login.html', {'form': form})


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/file')
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    raise Http404


class UploadFile(View):

    def get(self, request):
        form = UploadFileForm()
        context = {'form': form}
        return render(request, 'files/upload.html', context)

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            adv = AdvUser.objects.get(user = request.user)
            file.user = adv
            # if adv.max_size_of_files < file.size + adv.engaged_size:
            if file.size + adv.engaged_size > 512000:

                messages.error(request, 'Лимит загрузки файлов превышен!')
                return render(request, 'files/upload.html', context={'form': form})
            file.save()
            correct_engaged_size_advUser(adv)
            return redirect('index')
        return render(request, 'files/upload.html', context={'form': form})


class UpdateFileInfo(View):
    def get(self, request, id):
        file = File.objects.get(id = id)
        form = UploadFileForm(instance=file)
        context = {'form': form}
        return render(request, 'files/update.html', context)

    def post(self, request, id):
        file = File.objects.get(id = id)
        form = UploadFileForm(request.POST, instance=file)
        if form.is_valid():
            form.save()
        return redirect('index')


class DeleteFile(View):
    def get(self, request, id):
        file = File.objects.get(id = id)
        context = {'file': file}
        return render(request, 'files/delete.html', context)

    def post(self, request, id):
        file = File.objects.get(id = id)
        advUser = AdvUser.objects.get(file = file)
        file.delete()
        correct_engaged_size(advUser)
        return redirect('index')


# --------------------------------REST API FILES---------------------------------------


class FileListApiView(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


