# Generated by Django 4.2.3 on 2023-08-07 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plannings', '0004_periode_nb_semaines'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periode',
            name='planning',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
