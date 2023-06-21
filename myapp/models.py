import datetime
from django.utils import timezone
from django.db import models


# Create your models here.
class Pertanyaan(models.Model):
    pertanyaan_text = models.TextField(max_length=200)
    tanggal_post = models.DateTimeField("tanggal diposting")

    def __str__(self):
        return self.pertanyaan_text
    
    def diterbitkan_baru_ini(self):
        sekarang = timezone.now()
        return sekarang - datetime.timedelta(days=1) <= self.tanggal_post <= sekarang


class Pilihan(models.Model):
    pertanyaan = models.ForeignKey(Pertanyaan, on_delete=models.CASCADE)
    pilihan_text = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

        
    def __str__(self):
       return self.pilihan_text
