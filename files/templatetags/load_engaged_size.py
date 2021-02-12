from django import template
from ..models import *

register = template.Library()


@register.filter
def get_engaged_size(user):
    advUser = AdvUser.objects.get(user=user)
    print(advUser)
    total_size = 0
    for file in advUser.file.all():
        total_size += file.size
    AdvUser.objects.filter(user = user).update(engaged_size=total_size,
                                              correct_engaged_size=filesizeformat(total_size))
    return advUser.correct_engaged_size