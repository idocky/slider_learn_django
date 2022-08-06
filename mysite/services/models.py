from django.db import models


class ServiceCards(models.Model):
    card_descr = models.CharField(max_length=200)
    card_price = models.CharField(max_length=50)

    def __str__(self):
        return self.card_descr

    class Meta:
        verbose_name = 'PriceCard'
        verbose_name_plural = 'PriceCards'


class ServiceTable(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')
    old_price = models.CharField(max_length=50, verbose_name='old price')
    new_price = models.CharField(max_length=50, verbose_name='new price')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'PriceTable'
        verbose_name_plural = 'PriceTable'
