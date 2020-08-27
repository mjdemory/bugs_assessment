from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import  authenticate, login, logout

# from custom_user.models import MyUser
from custom_user.forms import LoginForm
# from django.conf import settings

# Create your views here.


def index(request):
    return render(request, "index.html")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'), password=data.get('password'))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))

    form = LoginForm()
    return render(request, "basic.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))