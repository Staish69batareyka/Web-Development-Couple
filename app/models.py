from django.db import models

class HeartRateRecord(models.Model):
    time = models.CharField(max_length=8, unique=True, verbose_name='Время записи')
    heart_rate = models.CharField(verbose_name='Частота сердечных сокращений')

    def __str__(self):
        return f'{self.time} -> {self.heart_rate} уд/мин.'
