from django.db import models

# Create your models here.

class Map(models.Model):
  gid = models.AutoField(primary_key=True)
  emd_cd = models.CharField(max_length=10, blank=True, null=True)
  emd_nm = models.CharField(max_length=40, blank=True, null=True)
  emd_eng_nm = models.CharField(max_length=40, blank=True, null=True)
  esri_pk = models.IntegerField(blank=True, null=True)
  shape_area = models.DecimalField(decimal_places=100, max_digits=100)
  shape_len = models.DecimalField(decimal_places=100, max_digits=100)
  geom = models.BinaryField(blank=True, null=True)

  def __str__(self):
    return self.gid