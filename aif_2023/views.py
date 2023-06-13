from _datetime import datetime
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.urls.base import reverse_lazy
from aif_2023.forms import UserRegisterForm


class SignUpView(
        SuccessMessageMixin,
        CreateView):
    template_name = "register.html"
    success_url = reverse_lazy("login")
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"


def index(request):
    return render(request=request,
                  template_name="index.html",
                  context={"date_time": datetime.today(),
                           "name": "Janusz Biznesu"})
