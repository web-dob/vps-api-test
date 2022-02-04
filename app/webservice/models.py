#-*- coding: utf-8 -*-
import uuid
from django.db import models

STATUS = [
  (0, 'stopped'),
  (1, 'started'),
  (2,'blocked')
]

# Create your models here.
class UUIDModel(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Vps(UUIDModel):
    class Meta:
        verbose_name = 'VPS'
        verbose_name_plural = 'VPS'

    cpu = models.PositiveSmallIntegerField(verbose_name='количество ядер')
    ram = models.PositiveSmallIntegerField(verbose_name='объем RAM')
    hdd = models.PositiveSmallIntegerField(verbose_name='объем HDD')
    status = models.PositiveSmallIntegerField(verbose_name='статус сервера (started, blocked, stopped)', choices=STATUS)

    def __str__(self):
        return f"cpu: {self.cpu} / ram: {self.ram} / hdd: {self.hdd} / status: {self.status}"
