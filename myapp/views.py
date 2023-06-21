from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib.auth.models import User

# import dari folder lain
from .forms import RespondentForm
from .models import Pertanyaan, Pilihan


# Create your views here
# fungsi untuk autentikasi, daftar, login, dan logout
def daftar_respondent(request):
    title = "Daftar"
    if request.method == "POST":
        form = RespondentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "registrasi berhasil.")
            return redirect("myapp:login")
        messages.error(
            request, "hai registrasi anda tidak berhasil, masukkan data valid"
        )
    form = RespondentForm()
    return render(
        request=request,
        template_name="registrasi/daftar.html",
        context={
            "title": title,
            "daftar_form": form,
        },
    )


def login_respondent(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(
                    request, f"selamat datang !! anda telah login sebagai {username}"
                )
                return redirect("myapp:home")
            else:
                messages.error(
                    request, "data yang anda masukkan tidak ada di data kami"
                )
        else:
            messages.error(
                request,
                "data yang anda masukkan tidak ada di database silahkan daftar ulang stau coba lagi",
            )
    form = AuthenticationForm()
    title = "Login"
    return render(
        request=request,
        template_name="registrasi/login.html",
        context={
            "title": title,
            "login_form": form,
        },
    )


def logout_respondent(request):
    logout(
        request,
    )
    messages.info(request, "anda berhasil keluar akun")
    return redirect("myapp:home")


# Fungsi Untuk Survey
def home(request):
    title = "Home"
    daftar_pertanyaan = Pertanyaan.objects.all()
    context = {"title": title, "daftar_pertanyaan": daftar_pertanyaan}
    return render(request, "survey/home.html", context)


def rincian(request, pertanyaan_id):
    title = "Rincian"
    pertanyaan = get_object_or_404(Pertanyaan, pk=pertanyaan_id)
    context = {
        "title": title,
        "pertanyaan": pertanyaan,
    }
    return render(request, "survey/rincian.html", context)


def hasil(request, pertanyaan_id):
    title = "Hasil"
    jumlah_pertanyaan = Pertanyaan.objects.all().count()
    total_respondent  = User.objects.all().count()
    pertanyaan = get_object_or_404(Pertanyaan, pk=pertanyaan_id)
    context = {
        "title": title,
        "jumlah_pertanyaan": jumlah_pertanyaan,
        "total_respondent":total_respondent,
        "pertanyaan": pertanyaan,
    }
    return render(request, "survey/hasil.html", context)


def vote(request, pertanyaan_id):
    pertanyaan = get_object_or_404(Pertanyaan, pk=pertanyaan_id)
    try:
        pilihan_dipilih = pertanyaan.pilihan_set.get(pk=request.POST["pilihan"])
    except (KeyError, Pilihan.DoesNotExist):
        context = {
            "pertanyaan": pertanyaan,
            "error_message": "anda belum memilih salah satu",
        }
        return render(request, "survey/rincian.html", context)
    else:
        pilihan_dipilih.votes += 1
        pilihan_dipilih.save()
        return HttpResponseRedirect(reverse("myapp:hasil", args=(pertanyaan_id,)))
