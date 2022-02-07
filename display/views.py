from django.shortcuts import render
from .models import Human


def home(request):
    all = Human.objects.all()
    return render(request, "home.html", {'all': all})
