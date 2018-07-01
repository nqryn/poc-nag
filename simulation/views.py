from django.shortcuts import render

from models import NoName


def no_names(request):
    qs = NoName.objects.all()
    return render(request, 'no_names.html', {'qs': qs})