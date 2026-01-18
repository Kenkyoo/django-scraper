from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import urllib.request, ssl
from bs4 import BeautifulSoup

def home(request):
    imagenes = []
    url = request.GET.get("url")

    if url:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        html = urllib.request.urlopen(req, context=ctx).read()
        sopa = BeautifulSoup(html, "html.parser")

        for img in sopa("img"):
            src = img.get("src")
            imagenes.append(src)

    return render(request, "home.html", {
        "imagenes": imagenes,
        "url": url
    })

def registro(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')
        else:
            form = UserCreationForm()
        return render(request, 'registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')
