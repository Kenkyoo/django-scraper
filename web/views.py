import ssl
import urllib.request
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .models import Favorite, Image


@login_required
def save_favorite(request):
    if request.method == "POST":
        image_url = request.POST.get("image_url")

        if image_url:
            image, _ = Image.objects.get_or_create(url=image_url)
            Favorite.objects.create(user=request.user, image=image)

    return redirect("favorites")


@login_required
def delete_favorite(request):
    if request.method == "POST":
        image_url = request.POST.get("image_url")

        if image_url:
            image = Image.objects.get(url=image_url)
            Favorite.objects.filter(user=request.user, image=image).delete()

    return redirect("favorites")


def home(request):
    imagenes = []
    url = request.GET.get("url")

    if url:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

        html = urllib.request.urlopen(req, context=ctx).read()
        sopa = BeautifulSoup(html, "html.parser")

        for img in sopa("img"):
            src = img.get("src")
            if not src:
                continue

            src = urljoin(url, src)
            imagenes.append(src)

    return render(request, "home.html", {"imagenes": imagenes, "url": url})


def registro(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
    return render(request, "login.html")


@login_required
def favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, "favorites.html", {"favorites": favorites})
