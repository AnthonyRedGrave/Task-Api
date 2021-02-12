from .models import *


def correct_engaged_size(user):
    total_size = 0
    for file in user.file.all():
        total_size += file.size
    AdvUser.objects.filter(user=user).update(engaged_size=total_size,
                                             correct_engaged_size=filesizeformat(total_size))


def correct_engaged_size_advUser(advUser):
    total_size = 0
    for file in advUser.file.all():
        total_size += file.size
    AdvUser.objects.filter(id = advUser.id).update(engaged_size=total_size, correct_engaged_size=filesizeformat(total_size))