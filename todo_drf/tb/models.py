from django.db import models

# Create your models here.

class Gltf_json(models.Model):
  id =  models.AutoField(primary_key=True)
  siteid = models.IntegerField()
  bimid = models.IntegerField()
  data = models.JSONField(null=True)

  class Meta:
    constraints = [
    models.UniqueConstraint(fields=['siteid', 'bimid'], name='unique_json_id')
    ]

  def __str__(self):
    return self.id

class Gltf_buffer(models.Model):
  id = models.AutoField(primary_key=True)
  siteid = models.IntegerField()
  bimid = models.IntegerField()
  buffer = models.JSONField(null=True)
  name = models.CharField(max_length=50)

  class Meta:
    constraints = [
    models.UniqueConstraint(fields=['siteid', 'bimid', 'name'], name='unique_buffer_id')
    ]

  def __str__(self):
    return self.id

class Gltf_buffer2(models.Model):
  id = models.AutoField(primary_key=True)
  siteid = models.IntegerField()
  bimid = models.IntegerField()
  buffer = models.BinaryField(null=True, blank=True)
  name = models.CharField(max_length=50)
  file = models.FileField(upload_to="%m", null=True, blank=True)

  class Meta:
    constraints = [
    models.UniqueConstraint(fields=['siteid', 'bimid', 'name'], name='unique_buffer_id2')
    ]

  def __str__(self):
    return self.id