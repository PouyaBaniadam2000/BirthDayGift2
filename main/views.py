from django.shortcuts import render
from .models import *


def birthday_card(request):
    general_info = GeneralInfo.objects.last()
    return render(request, "main/birthday_card.html", context={"general_info": general_info})


def birthday_cake(request):
    return render(request, "main/birthday_cake.html")


def birthday_balloons(request):
    return render(request, "main/birthday_balloons.html")
