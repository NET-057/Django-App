# Generated by Django 2.0.1 on 2018-01-12 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DileepImage', '0004_auto_20180112_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DileepImage.AlbumModel'),
        ),
    ]
