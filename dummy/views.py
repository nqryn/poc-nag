from django.shortcuts import render

from models import DummyModel


def dummies(request):
    qs = DummyModel.objects.all()
    return render(request, 'dummies.html', {'qs': qs})