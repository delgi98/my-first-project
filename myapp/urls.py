from django.urls import path
from . import views 

app_name = "myapp"
urlpatterns = [
    path("", views.home, name="home"),
    
# url untuk sesi autentifikasi respondent 
    path("daftar/", views.daftar_respondent, name="daftar"),
    path("login/", views.login_respondent, name="login"),
    path("logout/", views.logout_respondent, name="logout"),
    
#url untuk sesi survey
    path("<int:pertanyaan_id>/", views.rincian, name="rincian"),
    path("<int:pertanyaan_id>/hasil/", views.hasil, name="hasil"),
    path("<int:pertanyaan_id>/vote/", views.vote, name="vote"),
]