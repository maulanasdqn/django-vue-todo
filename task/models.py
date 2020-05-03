from django.db import models

class Task(models.Model):
    judul = models.CharField(max_length=200)
    tanggal = models.DateTimeField(auto_now_add=True)
    beres = models.BooleanField(default=False)

    #Buat Nyusun Dari yang sudah beres, disusun berdasarkan Waktu pas Bikin
    class Meta:
        ordering = ['beres', 'tanggal']
