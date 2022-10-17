from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    Mahasiswa_id = models.CharField(max_length=10)
    Nama = models.CharField(max_length=100)
    Fakultas = models.CharField(max_length=50)

    class Meta:
        db_table = 'Mahasiswa'
