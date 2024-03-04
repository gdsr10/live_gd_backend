from django.db import models

# Create your models here.
class AccountDetails(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=15)
    dob = models.CharField(max_length=15)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)
    is_admin = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, blank=True)
    otp_created_at = models.DateTimeField(null=True, blank=True)


class OrderList(models.Model):
    id = models.AutoField(primary_key=True)
    customername = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    image_url = models.CharField(max_length=250)
    order_type_name = models.CharField(max_length=150)
    order_type = models.CharField(max_length=150)
    file_upload = models.CharField(max_length=150)
    material_name = models.CharField(max_length=150)
    size = models.CharField(max_length=150)
    bust = models.CharField(max_length=150)
    waist = models.CharField(max_length=150)
    hips = models.CharField(max_length=150)
    status = models.CharField(max_length=150)


class ItemList(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500)
    price = models.CharField(max_length=150)
    description = models.CharField(max_length=150)