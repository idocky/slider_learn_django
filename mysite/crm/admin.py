from django.contrib import admin
from .models import Order, Status, Comment

admin.site.register(Status)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('com_name', 'com_date')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_name', 'order_dt', 'order_phone', 'order_status')