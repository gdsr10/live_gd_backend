# Generated by Django 2.2.22 on 2024-02-21 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_itemlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlist',
            name='title',
            field=models.CharField(default='all title same', max_length=500),
            preserve_default=False,
        ),
    ]