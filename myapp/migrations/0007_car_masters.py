# Generated by Django 4.2.6 on 2023-10-20 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_masters'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='masters',
            field=models.ManyToManyField(blank=True, null=True, to='myapp.masters', verbose_name='Repairmen'),
        ),
    ]
