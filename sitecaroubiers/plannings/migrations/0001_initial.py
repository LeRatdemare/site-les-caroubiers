# Generated by Django 4.2.3 on 2023-07-16 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('has_child_in_college', models.BooleanField(default=True)),
                ('has_child_in_school', models.BooleanField(default=True)),
            ],
        ),
    ]
