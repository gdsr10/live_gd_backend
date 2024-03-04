# Generated by Django 2.2.22 on 2024-02-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customername', models.CharField(max_length=150)),
                ('order_type_name', models.CharField(max_length=150)),
                ('order_type', models.CharField(max_length=150)),
                ('file_upload', models.CharField(max_length=150)),
                ('material_name', models.CharField(max_length=150)),
                ('size', models.CharField(max_length=150)),
                ('bust', models.CharField(max_length=150)),
                ('waist', models.CharField(max_length=150)),
                ('hips', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
            ],
        ),
    ]
