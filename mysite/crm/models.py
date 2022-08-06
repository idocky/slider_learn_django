from django.db import models

class Status(models.Model):
    new_status = models.CharField(max_length=50)

    def __str__(self):
        return self.new_status



class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200)
    order_phone = models.CharField(max_length=50)
    order_status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True, blank=True)


    def __str__(self):
        return self.order_name


class Comment(models.Model):
    com_name = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Имя')
    com_text = models.TextField()
    com_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.com_name
