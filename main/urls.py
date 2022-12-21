from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.birthday_card, name="birthday_card"),
    path("birthday_cake", views.birthday_cake, name="birthday_cake"),
    path("birthday_balloons", views.birthday_balloons, name="birthday_balloons"),
]
